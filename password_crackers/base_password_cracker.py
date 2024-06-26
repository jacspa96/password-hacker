import socket
import timeit
from abc import ABC, abstractmethod
from typing import Tuple, Generator


class BasePasswordCracker(ABC):

    def __init__(self, address: Tuple[str, int]):
        self.BUFFER_SIZE = 32
        self.SUCCESS_MESSAGE = "Connection success!"
        self.TOO_MANY_ATTEMPTS_MESSAGE = "Too many attempts."
        
        self.socket = None
        self.address = address
        self.credentials = None
        self.credentials_gen = self._credentials_generator()

    def crack_credentials(self) -> str:
        server_response = ""
        with socket.socket() as self.socket:
            self.socket.connect(self.address)
            while server_response != self.SUCCESS_MESSAGE:
                self.credentials = next(self.credentials_gen)
                server_response = self._communicate_with_server()
                self._handle_server_response(server_response)

        return self.credentials

    @abstractmethod
    def _credentials_generator(self) -> Generator[str, None, None]:
        pass
    
    def _communicate_with_server(self) -> str:
        self.socket.send(self.credentials.encode())
        server_response = self.socket.recv(self.BUFFER_SIZE).decode()
        return self._deserialize_server_response(server_response)

    def _handle_server_response(self, server_response: str) -> None:
        if server_response == self.TOO_MANY_ATTEMPTS_MESSAGE:
            raise Exception(self.TOO_MANY_ATTEMPTS_MESSAGE)

    def _deserialize_server_response(self, server_response: str) -> str:
        return server_response
