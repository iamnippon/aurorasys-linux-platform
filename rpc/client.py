"""
AuroraSys RPC Module
Lightweight JSON-Based RPC Client

Implements:
- TCP connection to RPC server
- JSON request formatting
- Structured response handling
- CLI-based invocation
"""

import socket
import json
import sys
from typing import Any, List

HOST = "127.0.0.1"
PORT = 5000


class RPCClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def call(self, method: str, params: List[Any]) -> dict:
        """Send RPC request and return response."""
        request = {
            "method": method,
            "params": params
        }

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.sendall(json.dumps(request).encode("utf-8"))

            response_data = client_socket.recv(4096)

        response = json.loads(response_data.decode("utf-8"))
        return response


def print_usage():
    print("Usage:")
    print("  python3 client.py <method> [params...]")
    print()
    print("Examples:")
    print("  python3 client.py ping")
    print("  python3 client.py add 5 3")
    print("  python3 client.py multiply 4 6")


def parse_params(params: List[str]) -> List[Any]:
    """Attempt to convert parameters to int or float if possible."""
    parsed = []
    for param in params:
        try:
            if "." in param:
                parsed.append(float(param))
            else:
                parsed.append(int(param))
        except ValueError:
            parsed.append(param)
    return parsed


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    method = sys.argv[1]
    raw_params = sys.argv[2:]
    params = parse_params(raw_params)

    client = RPCClient(HOST, PORT)

    try:
        response = client.call(method, params)

        if response.get("status") == "success":
            print("[SUCCESS]")
            print("Result:", response.get("result"))
        else:
            print("[ERROR]")
            print("Message:", response.get("message"))

    except ConnectionRefusedError:
        print("[ERROR] Unable to connect to RPC server.")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")


if __name__ == "__main__":
    main()
