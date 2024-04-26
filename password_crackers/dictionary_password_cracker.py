import itertools
import os
from .base_password_cracker import BasePasswordCracker
from typing import Tuple, List, Generator


PASSWORD_FILE_NAME = "passwords.txt"


def _load_passwords_from_file(file_path: str = None) -> List[str]:
    file_path = file_path if file_path is not None else _find_password_file_path()
    passwords = []
    with open(file_path, "r") as f:
        for line in f:
            passwords.append(line.strip())
    return passwords


def _find_password_file_path() -> str:
    for root, dirs, files in os.walk(os.getcwd()):
        if PASSWORD_FILE_NAME in files:
            return os.path.join(root, PASSWORD_FILE_NAME)


def _create_upper_and_lowercase_for_iteration(password: str) -> List[List[str]]:
    letters = [[letter.lower(), letter.upper()] if letter.isalpha() else [letter]
               for letter in password]
    return letters


class DictionaryPasswordCracker(BasePasswordCracker):

    def __init__(self, address: Tuple[str, int]):
        super().__init__(address)
        self.passwords = _load_passwords_from_file()

    def crack_password(self) -> str:
        return super().crack_password()

    def _password_generator(self) -> Generator[str, None, None]:
        for password in self.passwords:
            letters = _create_upper_and_lowercase_for_iteration(password)
            candidate_passwords = itertools.product(*letters)
            for candidate_password in candidate_passwords:
                yield "".join(candidate_password)

