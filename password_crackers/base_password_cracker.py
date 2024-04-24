import string
from abc import ABC, abstractmethod
from typing import Tuple


class BasePasswordCracker(ABC):

    def __init__(self, address: Tuple[str, int]):
        self.BUFFER_SIZE = 32
        self.CHARACTERS = string.ascii_lowercase + string.digits
        self.SUCCESS_MESSAGE = "Connection success!"
        self.TOO_MANY_ATTEMPTS_MESSAGE = "Too many attempts."

        self.address = address

    @abstractmethod
    def crack_password(self) -> str:
        pass
