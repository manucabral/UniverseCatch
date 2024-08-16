"""A strategic adaptation of Go Fish, featuring cards with planets, stars, black holes, and galaxies"""

from .controller import Controller
from .constants import GameConfig

__author__ = "Universe Catch, Inc."
__copyright__ = "Copyright 2024 Universe Catch"
__developers__ = ["manucabral", "larayavrs"]
__version__ = GameConfig.VERSION
__license__ = "GNU GPL v3.0"
__all__ = [
    "Controller",
]
