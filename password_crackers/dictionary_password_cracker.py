import itertools
from .base_password_cracker import BasePasswordCracker
from .utils import load_credentials_from_file
from typing import Tuple, List, Generator, override


PASSWORD_FILE_NAME = "passwords.txt"


class DictionaryPasswordCracker(BasePasswordCracker):

    def __init__(self, address: Tuple[str, int]):
        super().__init__(address)
        self.passwords = load_credentials_from_file(PASSWORD_FILE_NAME)

    @override
    def crack_credentials(self) -> str:
        return super().crack_credentials()

    @override
    def _credentials_generator(self) -> Generator[str, None, None]:
        for password in self.passwords:
            letters = _create_upper_and_lowercase_for_iteration(password)
            candidate_passwords = itertools.product(*letters)
            for candidate_password in candidate_passwords:
                yield "".join(candidate_password)


def _create_upper_and_lowercase_for_iteration(password: str) -> List[List[str]]:
    letters = [[letter.lower(), letter.upper()] if letter.isalpha() else [letter]
               for letter in password]
    return letters
