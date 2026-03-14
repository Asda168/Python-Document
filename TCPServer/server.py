"""
TCP Server - Full Two-Way OOP Implementation
Server can push messages back to any/all clients at any time.
"""

import socket
import threading
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [SERVER] %(message)s",
    datefmt="%H:%M:%S"
)


class ClientHandler(threading.Thread):
    """Handles one connected client — reads from it AND sends back."""

    def __init__(self, conn: socket.socket, address: tuple, server: "TCPServer"):
        super().__init__(daemon=True)
        self.conn    = conn
        self.address = address
        self.server  = server
        self.running = False
        self._send_lock = threading.Lock()

    # ------------------------------------------------------------------ #
    # Main loop                                                            #
    # ------------------------------------------------------------------ #
    def run(self):
        self.running = True
        logging.info(f"++ Client connected  : {self.address}")
        self.send(f"Welcome! You are connected from {self.address}. Type 'help' for commands.")

        buffer = ""
        try:
            while self.running:
                chunk = self.conn.recv(1024)
                if not chunk:
                    break
                buffer += chunk.decode("utf-8")
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    msg = line.strip()
                    if msg:
                        logging.info(f"   FROM {self.address}: {msg!r}")
                        response = self._handle(msg)
                        self.send(response)
                        if msg.lower() == "quit":
                            self.running = False
                            break
        except (ConnectionResetError, BrokenPipeError):
            logging.warning(f"-- Client dropped    : {self.address}")
        except Exception as e:
            logging.error(f"   Error ({self.address}): {e}")
        finally:
            self._cleanup()

    # ------------------------------------------------------------------ #
    # Command dispatcher                                                   #
    # ------------------------------------------------------------------ #
    def _handle(self, msg: str) -> str:
        cmd = msg.lower()
        if cmd == "ping":
            return "PONG"
        elif cmd == "time":
            return f"SERVER TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        elif cmd == "clients":
            return f"Active clients: {self.server.client_count()}"
        elif cmd == "help":
            return (
                "Commands available:\n"
                "  ping          -> server replies PONG\n"
                "  time          -> server current time\n"
                "  clients       -> number of active clients\n"
                "  broadcast MSG -> push MSG to every other client\n"
                "  quit          -> disconnect"
            )
        elif cmd.startswith("broadcast "):
            text = msg[len("broadcast "):]
            self.server.broadcast(f"[BROADCAST from {self.address}]: {text}", exclude=self)
            return f"Broadcast sent to {self.server.client_count() - 1} other client(s)."
        elif cmd == "quit":
            return "BYE - goodbye!"
        else:
            return f"ECHO: {msg}"

    # ------------------------------------------------------------------ #
    # Public send (thread-safe) — SERVER -> CLIENT                        #
    # ------------------------------------------------------------------ #
    def send(self, message: str):
        """Push any message back to this specific client at any time."""
        with self._send_lock:
            try:
                self.conn.sendall((message + "\n").encode("utf-8"))
                logging.info(f"   TO   {self.address}: {message!r}")
            except Exception as e:
                logging.error(f"   Send failed ({self.address}): {e}")
                self.running = False

    # ------------------------------------------------------------------ #
    # Cleanup                                                              #
    # ------------------------------------------------------------------ #
    def _cleanup(self):
        self.running = False
        try:
            self.conn.close()
        except Exception:
            pass
        self.server.remove_client(self)
        logging.info(f"-- Client removed    : {self.address}")


class TCPServer:
    """
    OOP TCP Server.
    - Accepts multiple clients (one thread each).
    - Sends responses back to each client automatically.
    - Server operator can type in console to broadcast to ALL clients.
    - Supports broadcast() and send_to() for targeted messaging.
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 9000):
        self.host    = host
        self.port    = port
        self._sock   = None
        self._clients: list[ClientHandler] = []
        self._lock   = threading.Lock()
        self.running = False

    # ------------------------------------------------------------------ #
    # Lifecycle                                                            #
    # ------------------------------------------------------------------ #
    def start(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind((self.host, self.port))
        self._sock.listen(10)
        self.running = True

        logging.info(f"Server listening on {self.host}:{self.port}")
        logging.info("Type a message + Enter to PUSH it to ALL connected clients.")
        logging.info("Type 'stop' or press Ctrl+C to shut down.\n")

        # Accept loop runs in background thread
        accept_thread = threading.Thread(target=self._accept_loop, daemon=True)
        accept_thread.start()

        # Main thread = server console for pushing messages to clients
        self._console_loop()

    def _accept_loop(self):
        while self.running:
            try:
                conn, addr = self._sock.accept()
                handler = ClientHandler(conn, addr, self)
                self.add_client(handler)
                handler.start()
            except OSError:
                break

    def _console_loop(self):
        """Server operator types here to push messages to ALL clients."""
        try:
            while self.running:
                text = input()
                if text.strip().lower() in ("stop", "exit"):
                    break
                if text.strip():
                    self.broadcast(f"[SERVER]: {text.strip()}")
        except (KeyboardInterrupt, EOFError):
            pass
        finally:
            self.stop()

    def stop(self):
        self.running = False
        logging.info("Shutting down server...")
        with self._lock:
            for c in list(self._clients):
                c.send("Server is shutting down. Goodbye!")
                c._cleanup()
        if self._sock:
            self._sock.close()
        logging.info("Server stopped.")

    # ------------------------------------------------------------------ #
    # Client registry                                                      #
    # ------------------------------------------------------------------ #
    def add_client(self, h: ClientHandler):
        with self._lock:
            self._clients.append(h)

    def remove_client(self, h: ClientHandler):
        with self._lock:
            self._clients = [c for c in self._clients if c is not h]

    def client_count(self) -> int:
        with self._lock:
            return len(self._clients)

    # ------------------------------------------------------------------ #
    # Server -> Client messaging                                           #
    # ------------------------------------------------------------------ #
    def broadcast(self, message: str, exclude: ClientHandler | None = None):
        """Push a message to every connected client (optionally exclude one)."""
        with self._lock:
            targets = [c for c in self._clients if c is not exclude]
        for c in targets:
            c.send(message)

    def send_to(self, address: tuple, message: str) -> bool:
        """Push a message to one specific client by their (host, port) address."""
        with self._lock:
            for c in self._clients:
                if c.address == address:
                    c.send(message)
                    return True
        logging.warning(f"send_to: no client found at {address}")
        return False


if __name__ == "__main__":
    server = TCPServer(host="127.0.0.1", port=9000)
    server.start()