import sys
from typing import Tuple
from password_crackers.password_with_login_cracker import PasswordWithLoginCracker


def parse_args() -> Tuple[str, int]:
    args = sys.argv
    assert len(args) == 3, f"Expected exactly 2 program arguments, received {len(args) - 1}!"
    ip_address, port = args[1], int(args[2])
    return ip_address, port


def main():
    ip_address, port = parse_args()
    address = ip_address, port
    password_cracker = PasswordWithLoginCracker(address)
    credentials = password_cracker.crack_credentials()
    print(credentials)


if __name__ == "__main__":
    main()
