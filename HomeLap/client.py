"""
TCP Client - Python OOP Implementation
Connects to the TCP server, sends messages, and receives responses.
"""

import socket
import threading
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [CLIENT] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S"
)


class TCPClient:
    """
    OOP TCP Client that connects to a TCPServer,
    sends messages, and listens for responses in a background thread.
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 9000):
        self.host = host
        self.port = port
        self.socket: socket.socket | None = None
        self.connected = False
        self._listener_thread: threading.Thread | None = None

    # ------------------------------------------------------------------ #
    # Connection management                                                #
    # ------------------------------------------------------------------ #

    def connect(self) -> bool:
        """Establish a connection to the server."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.connected = True
            logging.info(f"Connected to server at {self.host}:{self.port}")
            self._start_listener()
            return True
        except ConnectionRefusedError:
            logging.error(f"Connection refused. Is the server running on {self.host}:{self.port}?")
            return False
        except Exception as e:
            logging.error(f"Connection error: {e}")
            return False

    def disconnect(self):
        """Close the connection cleanly."""
        self.connected = False
        if self.socket:
            try:
                self.socket.close()
            except Exception:
                pass
        logging.info("Disconnected from server.")

    # ------------------------------------------------------------------ #
    # Sending & receiving                                                  #
    # ------------------------------------------------------------------ #

    def send(self, message: str) -> bool:
        """Send a message string to the server."""
        if not self.connected or not self.socket:
            logging.warning("Not connected. Call connect() first.")
            return False
        try:
            self.socket.sendall((message + "\n").encode("utf-8"))
            logging.info(f"Sent: {message!r}")
            return True
        except (BrokenPipeError, OSError) as e:
            logging.error(f"Send failed: {e}")
            self.connected = False
            return False

    def _start_listener(self):
        """Start a background thread to receive server messages."""
        self._listener_thread = threading.Thread(
            target=self._listen, daemon=True, name="ClientListener"
        )
        self._listener_thread.start()

    def _listen(self):
        """Continuously read data from the server socket."""
        buffer = ""
        while self.connected:
            try:
                chunk = self.socket.recv(1024)
                if not chunk:
                    logging.warning("Server closed the connection.")
                    self.connected = False
                    break

                buffer += chunk.decode("utf-8")
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    self.on_message(line.strip())

            except OSError:
                break  # Socket was closed locally

    # ------------------------------------------------------------------ #
    # Callback                                                             #
    # ------------------------------------------------------------------ #

    def on_message(self, message: str):
        """
        Called whenever a complete message arrives from the server.
        Override this in a subclass for custom handling.
        """
        logging.info(f"Received: {message!r}")

    # ------------------------------------------------------------------ #
    # Interactive mode                                                     #
    # ------------------------------------------------------------------ #

    def interactive(self):
        """
        Run an interactive REPL so the user can type messages.
        Built-in commands:
          ping      → server responds PONG
          time      → server returns current time
          clients   → number of active clients
          quit      → graceful disconnect
        """
        print("\n" + "=" * 50)
        print("  TCP Client — Interactive Mode")
        print("  Commands: ping | time | clients | quit")
        print("=" * 50 + "\n")

        try:
            while self.connected:
                try:
                    user_input = input(">> ").strip()
                except EOFError:
                    break

                if not user_input:
                    continue

                self.send(user_input)

                if user_input.lower() == "quit":
                    import time; time.sleep(0.2)  # wait for BYE response
                    break
        finally:
            self.disconnect()


class LoggingClient(TCPClient):

    def __init__(self, host: str = "127.0.0.1", port: int = 9000,
                 logfile: str = "client_log.txt"):
        super().__init__(host, port)
        self.logfile = logfile

    def on_message(self, message: str):
        super().on_message(message)
        with open(self.logfile, "a") as f:
            f.write(message + "\n")

if __name__ == "__main__":
    client = TCPClient(host="127.0.0.1", port=9000)

    if client.connect():
        client.interactive()