"""
This module contains the music class, responsible for playing music in the game.
"""

import os
import pygame as pg
from .logger import get_logger
from .constants.resource import ResourceConfig


class Music:
    """
    This class is responsible for playing music in the game.
    """

    def __init__(self, music_path: str, debug: bool = False):
        """
        Initialize the music class.
        """
        self.logger = get_logger(self.__class__.__name__)
        self.path: str = music_path
        self.debug: bool = debug
        self.music: pg.mixer.music = None
        self.data: dict = {}
        self.current_track: int = 0
        self.playlist: list[dict] = []

    def init_music(self) -> None:
        """
        Initialize the music.
        """
        pg.mixer.init()
        pg.mixer.music.set_endevent(pg.USEREVENT + 1)
        self.music = pg.mixer.music

        for music_item in ResourceConfig.MUSICS:
            self.load_music(music_item)

        self.logger.info("Initialized.")

    def load_music(self, music_name: str) -> None:
        """
        Load the music file.
        """
        if music_name not in ResourceConfig.MUSICS:
            self.logger.error(f"Music {music_name} not found.")
            return
        music_file = os.path.join(self.path, ResourceConfig.MUSICS[music_name])
        music_file = os.path.normpath(music_file)
        self.playlist.append({"name": music_name, "file": music_file})
        self.logger.info(f"{music_name} loaded ({music_file}).")

    def play_current_track(self) -> None:
        """
        Play the current track.
        """
        track = self.playlist[self.current_track]
        music_file = track["file"]
        self.logger.info(f"Playing {track['name']} ({music_file}).")
        self.music.load(music_file)
        self.music.play()

    def play_music(self) -> None:
        """
        Play current music.
        """
        if not self.playlist:
            self.logger.error("Playlist is empty.")
            return
        self.current_track = 0
        self.play_current_track()

    def stop_music(self) -> None:
        """
        Stop the music.
        """
        self.music.stop()

    def set_volume(self, volume: float) -> None:
        """
        Set the volume of the music.
        """
        self.music.set_volume(volume)

    def handle_event(self, event: pg.event.Event) -> None:
        """
        Handle events related to music playback.
        """
        if event.type == pg.USEREVENT + 1:
            self.current_track = (self.current_track + 1) % len(self.playlist)
            if self.debug:
                self.logger.debug(
                    f"Next track: {self.playlist[self.current_track]['name']}"
                )
            self.play_current_track()
