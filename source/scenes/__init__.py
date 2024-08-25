"""
This file is used to make the scenes folder a package.
"""

from .intro import IntroScene
from .main_menu import MainMenuScene
from .settings_menu import SettingsMenuScene
from .music_settings import MusicSettingsScene

__all__ = ["IntroScene", "MainMenuScene", "SettingsMenuScene", "MusicSettingsScene"]
