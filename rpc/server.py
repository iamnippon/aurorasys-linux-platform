"""
AuroraSys RPC Module
Lightweight JSON-Based RPC Server

Implements:
- TCP socket server
- JSON request/response protocol
- Procedure dispatching
- Structured error handling
"""

import socket
import json
import threading
from typing import Callable, Dict, Any

HOST = "127.0.0.1"
PORT = 5000


class RPCServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.procedures: Dict[str, Callable[..., Any]] = {}

    def register(self, name: str, func: Callable[..., Any]):
        """Register an RPC procedure."""
        self.procedures[name] = func

    def handle_client(self, client_socket: socket.socket, address):
        print(f"[INFO] Connection established from {address}")

        try:
            data = client_socket.recv(4096)
            if not data:
                return

            request = json.loads(data.decode("utf-8"))
            print(f"[DEBUG] Received request: {request}")

            method = request.get("method")
            params = request.get("params", [])

            if method not in self.procedures:
                response = {
                    "status": "error",
                    "message": f"Method '{method}' not found"
                }
            else:
                try:
                    result = self.procedures[method](*params)
                    response = {
                        "status": "success",
                        "result": result
                    }
                except Exception as e:
                    response = {
                        "status": "error",
                        "message": str(e)
                    }

            client_socket.sendall(json.dumps(response).encode("utf-8"))

        except json.JSONDecodeError:
            error_response = {
                "status": "error",
                "message": "Invalid JSON request"
            }
            client_socket.sendall(json.dumps(error_response).encode("utf-8"))

        finally:
            client_socket.close()
            print(f"[INFO] Connection closed: {address}")

    def start(self):
        """Start the RPC server."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()

            print(f"[INFO] RPC Server running on {self.host}:{self.port}")

            while True:
                client_socket, address = server_socket.accept()
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, address),
                    daemon=True
                )
                client_thread.start()


# ------------------------
# Example RPC Procedures
# ------------------------

def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def ping() -> str:
    return "pong"


# ------------------------
# Main Execution
# ------------------------

if __name__ == "__main__":
    server = RPCServer(HOST, PORT)

    # Register procedures
    server.register("add", add)
    server.register("multiply", multiply)
    server.register("ping", ping)

    server.start()
