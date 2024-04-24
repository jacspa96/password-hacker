import sys
import socket
import itertools
import string
from typing import Tuple, Generator

BUFFER_SIZE = 32
CHARACTERS = string.ascii_lowercase + string.digits
SUCCESS_MESSAGE = "Connection success!"
TOO_MANY_ATTEMPTS_MESSAGE = "Too many attempts."


def parse_args() -> Tuple[str, int]:
    args = sys.argv
    assert len(args) == 3, f"Expected exactly 2 program arguments, received {len(args) - 1}!"
    ip_address, port = args[1], int(args[2])
    return ip_address, port


def password_generator() -> Generator[str, None, None]:
    password_len = 1
    while True:
        for password in itertools.product(CHARACTERS, repeat=password_len):
            yield "".join(password)
        password_len += 1


def main():
    ip_address, port = parse_args()
    passwords = password_generator()
    server_response = ""
    with socket.socket() as my_socket:
        my_socket.connect((ip_address, port))
        while server_response != SUCCESS_MESSAGE:
            password = next(passwords)
            my_socket.send(password.encode())
            server_response = my_socket.recv(BUFFER_SIZE).decode()
            if server_response == TOO_MANY_ATTEMPTS_MESSAGE:
                raise Exception(TOO_MANY_ATTEMPTS_MESSAGE)
    print(password)


if __name__ == "__main__":
    main()
