import itertools
import socket
from .base_password_cracker import BasePasswordCracker
from typing import Tuple, Generator


class BruteForcePasswordCracker(BasePasswordCracker):

    def __init__(self, address: Tuple[str, int]):
        super().__init__(address)

    def crack_password(self) -> str:
        passwords = self.__password_generator()
        server_response = ""
        with socket.socket() as my_socket:
            my_socket.connect(self.address)
            while server_response != self.SUCCESS_MESSAGE:
                password = next(passwords)
                my_socket.send(password.encode())
                server_response = my_socket.recv(self.BUFFER_SIZE).decode()
                if server_response == self.TOO_MANY_ATTEMPTS_MESSAGE:
                    raise Exception(self.TOO_MANY_ATTEMPTS_MESSAGE)

        return password

    def __password_generator(self) -> Generator[str, None, None]:
        password_len = 1
        while True:
            for password in itertools.product(self.CHARACTERS, repeat=password_len):
                yield "".join(password)
            password_len += 1
