"""
This module contains the network configuration for the game.
"""


class NetworkConfig:
    """
    Configuration for the game network.
    """

    HOST: str = "localhost"
    PORT: int = 5642
    MAX_CONNECTIONS: int = 4
    BUFFER_SIZE: int = 1024
    TIMEOUT: int = 5
    RECV_SIZE: int = 1024
