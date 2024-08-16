"""
This module is responsible for loading resources from the disk.
Resources are images, sounds, and other files that are used in the game.
"""

import os


class ResourceLoader:
    """
    This class is responsible for loading resources from the disk.
    """

    def __init__(self, resource_dir: str = "resources"):
        if not os.path.isdir(resource_dir):
            raise FileNotFoundError(f"Resource directory '{resource_dir}' not found.")
        self.resource_dir = resource_dir
        self.fonts = {}
        self.images = {}
        self.sounds = {}

    def load_all_fonts(self) -> None:
        pass

    def load_all_images(self) -> None:
        pass

    def load_all_sounds(self) -> None:
        pass
