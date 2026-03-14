"""
TCP Server - Python OOP Implementation
Handles multiple clients using threading
"""

import socket
import threading
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [SERVER] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S"
)


class ClientHandler(threading.Thread):
    """Handles communication with a single connected client."""

    def __init__(self, conn: socket.socket, address: tuple, server: "TCPServer"):
        super().__init__(daemon=True)
        self.conn = conn
        self.address = address
        self.server = server
        self.running = False

    def run(self):
        self.running = True
        logging.info(f"Client connected: {self.address}")

        try:
            while self.running:
                data = self.conn.recv(1024)
                if not data:
                    break

                message = data.decode("utf-8").strip()
                logging.info(f"Received from {self.address}: {message!r}")

                response = self._handle_message(message)
                self.send(response)

        except (ConnectionResetError, BrokenPipeError):
            logging.warning(f"Client {self.address} disconnected abruptly.")
        except Exception as e:
            logging.error(f"Error with client {self.address}: {e}")
        finally:
            self.disconnect()

    def _handle_message(self, message: str) -> str:
        """Process incoming message and return a response."""
        if message.lower() == "ping":
            return "PONG"
        elif message.lower() == "time":
            return f"Server time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        elif message.lower() == "clients":
            count = self.server.client_count()
            return f"Active clients: {count}"
        elif message.lower() == "quit":
            self.running = False
            return "BYE"
        else:
            return f"ECHO: {message}"

    def send(self, message: str):
        """Send a message to this client."""
        try:
            self.conn.sendall((message + "\n").encode("utf-8"))
        except Exception as e:
            logging.error(f"Failed to send to {self.address}: {e}")

    def disconnect(self):
        """Clean up and remove client from server registry."""
        self.running = False
        self.conn.close()
        self.server.remove_client(self)
        logging.info(f"Client disconnected: {self.address}")


class TCPServer:
    """
    OOP TCP Server that listens for connections and spawns
    a ClientHandler thread for each connected client.
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 9000):
        self.host = host
        self.port = port
        self.server_socket: socket.socket | None = None
        self.clients: list[ClientHandler] = []
        self._lock = threading.Lock()
        self.running = False

    def start(self):
        """Start the server and begin accepting connections."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.running = True

        logging.info(f"Server started on {self.host}:{self.port}")
        logging.info("Waiting for connections... (Ctrl+C to stop)\n")

        try:
            while self.running:
                try:
                    conn, address = self.server_socket.accept()
                    handler = ClientHandler(conn, address, self)
                    self.add_client(handler)
                    handler.start()
                except OSError:
                    break  # Socket closed
        except KeyboardInterrupt:
            logging.info("Shutdown requested.")
        finally:
            self.stop()

    def stop(self):
        """Gracefully shut down the server."""
        self.running = False
        logging.info("Shutting down server...")

        with self._lock:
            for client in list(self.clients):
                client.send("Server is shutting down.")
                client.disconnect()

        if self.server_socket:
            self.server_socket.close()

        logging.info("Server stopped.")

    def add_client(self, handler: ClientHandler):
        with self._lock:
            self.clients.append(handler)

    def remove_client(self, handler: ClientHandler):
        with self._lock:
            self.clients = [c for c in self.clients if c is not handler]

    def client_count(self) -> int:
        with self._lock:
            return len(self.clients)

    def broadcast(self, message: str, exclude: ClientHandler | None = None):
        """Send a message to all connected clients."""
        with self._lock:
            for client in self.clients:
                if client is not exclude:
                    client.send(message)


if __name__ == "__main__":
    server = TCPServer(host="127.0.0.1", port=9000)
    server.start()