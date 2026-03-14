"""
TCP Client - Full Two-Way OOP Implementation
Continuously listens for messages FROM the server (not just replies).
"""

import socket
import threading
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [CLIENT] %(message)s",
    datefmt="%H:%M:%S"
)


class TCPClient:
    """
    OOP TCP Client with full two-way communication.

    - Connects to a TCPServer.
    - Background listener thread receives ANY message from the server
      at any time (not just responses to what the client sent).
    - on_message() callback fires for every incoming server message —
      override it in a subclass for custom handling.
    - interactive() gives a live console REPL.
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 9000):
        self.host    = host
        self.port    = port
        self._sock   = None
        self.connected = False
        self._recv_thread = None
        self._send_lock   = threading.Lock()

    # ------------------------------------------------------------------ #
    # Connection                                                           #
    # ------------------------------------------------------------------ #
    def connect(self) -> bool:
        """Open the connection and start the background listener."""
        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.connect((self.host, self.port))
            self.connected = True
            logging.info(f"Connected to server at {self.host}:{self.port}")

            # Start background thread to receive server messages
            self._recv_thread = threading.Thread(
                target=self._listen_loop, daemon=True, name="RecvThread"
            )
            self._recv_thread.start()
            return True

        except ConnectionRefusedError:
            logging.error(f"Connection refused — is the server running on {self.host}:{self.port}?")
            return False
        except Exception as e:
            logging.error(f"Connection error: {e}")
            return False

    def disconnect(self):
        """Close the connection gracefully."""
        self.connected = False
        if self._sock:
            try:
                self._sock.close()
            except Exception:
                pass
        logging.info("Disconnected from server.")

    # ------------------------------------------------------------------ #
    # Sending  (CLIENT -> SERVER)                                          #
    # ------------------------------------------------------------------ #
    def send(self, message: str) -> bool:
        """Send a message to the server."""
        if not self.connected:
            logging.warning("Not connected.")
            return False
        with self._send_lock:
            try:
                self._sock.sendall((message + "\n").encode("utf-8"))
                return True
            except (BrokenPipeError, OSError) as e:
                logging.error(f"Send failed: {e}")
                self.connected = False
                return False

    # ------------------------------------------------------------------ #
    # Receiving  (SERVER -> CLIENT)  — background thread                  #
    # ------------------------------------------------------------------ #
    def _listen_loop(self):
        """
        Runs in a background daemon thread.
        Receives ALL messages from the server — both replies and
        server-initiated pushes — and calls on_message() for each.
        """
        buffer = ""
        while self.connected:
            try:
                chunk = self._sock.recv(1024)
                if not chunk:
                    logging.warning("Server closed the connection.")
                    self.connected = False
                    break
                buffer += chunk.decode("utf-8")
                # Split on newlines so multi-line messages work correctly
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    line = line.strip()
                    if line:
                        self.on_message(line)   # <-- YOUR HOOK
            except OSError:
                break   # Socket closed from our side

    # ------------------------------------------------------------------ #
    # Callback — override in subclass for custom handling                 #
    # ------------------------------------------------------------------ #
    def on_message(self, message: str):
        """
        Called every time ANY message arrives from the server.
        Override this in a subclass to handle messages your own way.
        """
        print(f"\n  [SERVER -> YOU]: {message}")

    # ------------------------------------------------------------------ #
    # Interactive REPL                                                     #
    # ------------------------------------------------------------------ #
    def interactive(self):
        """
        Live console. Type messages and press Enter to send.
        The background thread prints server replies/pushes automatically.

        Built-in commands understood by the server:
          ping          -> PONG
          time          -> server timestamp
          clients       -> count of active clients
          broadcast MSG -> push MSG to all other clients
          help          -> list commands
          quit          -> disconnect
        """
        print("\n" + "=" * 54)
        print("  Two-Way TCP Client  |  server: "
              f"{self.host}:{self.port}")
        print("  Commands: ping | time | clients |")
        print("            broadcast <msg> | help | quit")
        print("=" * 54)
        print("  (Server messages appear automatically)\n")

        try:
            while self.connected:
                try:
                    user_input = input("YOU >> ").strip()
                except EOFError:
                    break

                if not user_input:
                    continue

                self.send(user_input)

                if user_input.lower() == "quit":
                    time.sleep(0.25)   # wait for BYE reply
                    break
        finally:
            self.disconnect()


# ---------------------------------------------------------------------- #
# Subclass example: auto-reconnect client                                 #
# ---------------------------------------------------------------------- #
class AutoReconnectClient(TCPClient):
    """Automatically tries to reconnect if the server drops the connection."""

    def __init__(self, host: str = "127.0.0.1", port: int = 9000,
                 retry_interval: float = 3.0):
        super().__init__(host, port)
        self.retry_interval = retry_interval

    def connect_with_retry(self, max_attempts: int = 5) -> bool:
        for attempt in range(1, max_attempts + 1):
            logging.info(f"Connection attempt {attempt}/{max_attempts}...")
            if self.connect():
                return True
            if attempt < max_attempts:
                logging.info(f"Retrying in {self.retry_interval}s...")
                time.sleep(self.retry_interval)
        logging.error("Could not connect after maximum attempts.")
        return False

    def on_message(self, message: str):
        super().on_message(message)
        # Auto-reconnect if server says it's shutting down
        if "shutting down" in message.lower():
            logging.info(f"Server shutdown detected. Reconnecting in {self.retry_interval}s...")
            self.connected = False
            time.sleep(self.retry_interval)
            self.connect_with_retry()


# ---------------------------------------------------------------------- #
# Entry point                                                              #
# ---------------------------------------------------------------------- #
if __name__ == "__main__":
    client = TCPClient(host="127.0.0.1", port=9000)

    if client.connect():
        client.interactive()