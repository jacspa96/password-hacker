import sys
import socket
from typing import Tuple

BUFFER_SIZE = 1024


def parse_args() -> Tuple[str, int, str]:
    args = sys.argv
    assert len(args) == 4, f"Expected exactly 3 program arguments, received {len(args) - 1}!"
    ip_address, port, message = args[1], int(args[2]), args[3]
    return ip_address, port, message


def main():locals()
    ip_address, port, message = parse_args()
    with socket.socket() as my_socket:
        my_socket.connect((ip_address, port))
        my_socket.send(message.encode())
        response = my_socket.recv(1024)
        print(response.decode())


if __name__ == "__main__":
    main()
