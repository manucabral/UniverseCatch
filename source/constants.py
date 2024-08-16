class GlobalConfig:
    """
    Global configuration for the game.
    """

    DEBUG: bool = True
    TITLE: str = "UniverseCatch"
    VERSION: str = "0.1"
    FPS: int = 60


class DisplayConfig:
    """
    Configuration for the game display.
    """

    WIDTH: int = 800
    HEIGHT: int = 600
    FULLSCREEN: bool = False

    @property
    def SIZE(self) -> tuple:
        return self.WIDTH, self.HEIGHT


class ResourceConfig:
    """
    Configuration for the game resources.
    """

    RESOURCE_DIR: str = "resources"


class NetworkConfig:
    """
    Configuration for the game network.
    """

    HOST: str = "localhost"
    PORT: int = 12345
