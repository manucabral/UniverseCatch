"""
This module is responsible for loading resources from the disk.
Resources are images, sounds, and other files that are used in the game.
"""

import os
import pygame as pyg
from .logger import get_logger
from .constants import ResourceConfig


class ResourceLoader:
    """
    This class is responsible for loading resources from the disk.
    """

    def __init__(self, resource_dir: str = "resources"):
        self.logger = get_logger(self.__class__.__name__)
        if not os.path.isdir(resource_dir):
            msg = f"Directory '{resource_dir}' not found."
            self.logger.error(msg)
            raise FileNotFoundError(msg)
        self.dir = resource_dir
        self.fonts = {}
        self.images = {}
        self.sounds = {}
        self.planets: dict = {}

    def load_all_fonts(self) -> None:
        pass

    def load_all_images(self) -> None:
        self.images["screen_loading"] = pyg.image.load(
            os.path.join(self.dir, "screen_loading.png")
        )
        self.images["logo"] = pyg.image.load(os.path.join(self.dir, "logo.png"))

        """
        Load all image planets
        """
        for item, item_path in ResourceConfig.PLANETS.items():
            try:
                path = os.path.join(ResourceConfig.PLANETS_DIR, item_path)
                self.planets[item] = pyg.image.load(path)
            except Exception as exc:
                self.logger.error(
                    f"Error loading planetId {item} from {path}, not found."
                )
                self.logger.error(exc, console=False)

    def load_all_sounds(self) -> None:
        pass
