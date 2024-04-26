import socket
from abc import ABC, abstractmethod
from typing import Tuple


class BasePasswordCracker(ABC):

    def __init__(self, address: Tuple[str, int], buffer_size: int = 32):
        self.BUFFER_SIZE = buffer_size
        self.SUCCESS_MESSAGE = "Connection success!"
        self.TOO_MANY_ATTEMPTS_MESSAGE = "Too many attempts."

        self.address = address

    def crack_password(self) -> str:
        passwords = self._password_generator()
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

    @abstractmethod
    def _password_generator(self):
        pass
