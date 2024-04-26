import sys
from typing import Tuple
from password_crackers.dictionary_password_cracker import DictionaryPasswordCracker


def parse_args() -> Tuple[str, int]:
    args = sys.argv
    assert len(args) == 3, f"Expected exactly 2 program arguments, received {len(args) - 1}!"
    ip_address, port = args[1], int(args[2])
    return ip_address, port


def main():
    ip_address, port = parse_args()
    address = ip_address, port
    password_cracker = DictionaryPasswordCracker(address)
    password = password_cracker.crack_password()
    print(password)


if __name__ == "__main__":
    main()
