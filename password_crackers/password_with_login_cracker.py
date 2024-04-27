import json
import string
from .base_password_cracker import BasePasswordCracker
from .utils import load_credentials_from_file
from typing import Tuple, Generator, override


LOGINS_FILE_NAME = "logins.txt"
RESPONSE_MESSAGE_KEY = "result"
DUMMY_PASSWORD = "password"
LOGIN_KEY = "login"
PASSWORD_KEY = "password"


class PasswordWithLoginCracker(BasePasswordCracker):

    def __init__(self, address: Tuple[str, int]):
        super().__init__(address)
        self.BUFFER_SIZE = 64
        self.LOGIN_FOUND_MESSAGE = "Wrong password!"
        self.LOGIN_EXCEPTION_MESSAGE = "Exception happened during login"
        self.CHARACTERS = string.ascii_letters + string.digits

        self.logins = load_credentials_from_file(LOGINS_FILE_NAME)
        self.correct_login = None

    @override
    def crack_credentials(self) -> str:
        return super().crack_credentials()

    @override
    def _credentials_generator(self) -> Generator[str, None, None]:
        for login in self.logins:
            request = {LOGIN_KEY: login, PASSWORD_KEY: DUMMY_PASSWORD}
            yield _serialize_server_request(request)

    @override
    def _handle_server_response(self, server_response: str) -> None:
        super()._handle_server_response(server_response)
        if self._is_correct_login_found(server_response):
            self.correct_login = json.loads(self.credentials)[LOGIN_KEY]
            self.credentials_gen = self._credentials_with_correct_login_generator("")
        elif server_response == self.LOGIN_EXCEPTION_MESSAGE:
            correct_password_beginning = json.loads(self.credentials)[PASSWORD_KEY]
            self.credentials_gen = self._credentials_with_correct_login_generator(correct_password_beginning)

    @override
    def _deserialize_server_response(self, server_response: str) -> str:
        response_dict = json.loads(server_response)
        return response_dict[RESPONSE_MESSAGE_KEY]

    def _is_correct_login_found(self, server_response: str):
        return server_response == self.LOGIN_FOUND_MESSAGE and self.correct_login is None

    def _credentials_with_correct_login_generator(self, password_beginning: str):
        for character in self.CHARACTERS:
            password = "".join([password_beginning, character])
            request = {LOGIN_KEY: self.correct_login, PASSWORD_KEY: password}
            yield _serialize_server_request(request)


def _serialize_server_request(reqeust: dict) -> str:
    return json.dumps(reqeust)
