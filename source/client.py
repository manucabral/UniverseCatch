"""
Client module is responsible for managing the client side of the game.
"""

import os
import pygame as pyg
import socket as skt
from .logger import get_logger
from .constants import GameConfig, NetworkConfig


class Client:
    """
    Client class for the game.
    """

    def __init__(self, host: str, port: int = NetworkConfig.PORT):
        """
        Initialize the client.
        """
        self.logger = get_logger(self.__class__.__name__)
        self.host: str = host
        self.port: int = port
        self.socket: skt.socket = None
        self.running: bool = True
        self.logger.info("Initialized.")
