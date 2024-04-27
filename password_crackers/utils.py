import os
from typing import List


def load_credentials_from_file(file_name: str) -> List[str]:
    file_path = _find_file_path(file_name)
    passwords = []
    with open(file_path, "r") as f:
        for line in f:
            passwords.append(line.strip())
    return passwords


def _find_file_path(file_name: str) -> str:
    for root, dirs, files in os.walk(os.getcwd()):
        if file_name in files:
            return os.path.join(root, file_name)