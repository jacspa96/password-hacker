import itertools
import string
from .base_password_cracker import BasePasswordCracker
from typing import Tuple, Generator


class BruteForcePasswordCracker(BasePasswordCracker):

    def __init__(self, address: Tuple[str, int]):
        super().__init__(address)
        self.CHARACTERS = string.ascii_lowercase + string.digits

    def crack_password(self) -> str:
        return super().crack_password()

    def _password_generator(self) -> Generator[str, None, None]:
        password_len = 1
        while True:
            for password in itertools.product(self.CHARACTERS, repeat=password_len):
                yield "".join(password)
            password_len += 1
