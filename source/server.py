"""
This module contains the server class for the application.
"""

import socket
import threading
from .logger import get_logger, UCLogger
from .constants import NetworkConfig


class Server:
    """
    Server class for the application.
    """

    def __init__(
        self,
        host: str = NetworkConfig.HOST,
        port: int = NetworkConfig.PORT,
        max_connections: int = NetworkConfig.MAX_CONNECTIONS,
        debug: bool = False,
    ):
        """
        Initialize the server.
        """
        self.logger: UCLogger = get_logger(self.__class__.__name__)
        self.host: str = host
        self.port: int = port
        self.max_connections: int = max_connections
        self.socket: socket.socket = None
        self.clients: dict[str, socket.socket] = {}
        self.logger.info("Initialized instance.")

    def init(self):
        """
        Initialize the connection.
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.host, self.port))
            self.socket.listen(self.max_connections)
            self.logger.debug("Connection initialized.")
            if self.debug:
                self.logger.info(f"Started at {self.host}:{self.port}")
        except Exception as exc:
            self.logger.error(f"Error starting server: {exc}")
