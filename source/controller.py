"""
This module contains the Controller class.
This class is responsible for managing the game.
"""

import os
import pygame as pyg
from .scene import Scene
from .logger import get_logger
from .constants import DisplayConfig, Colors, GameConfig, ResourceConfig
from .resource_loader import ResourceLoader
from .localizations import Localizations
from .music import Music


class Controller:
    def __init__(self):
        """
        Initialize the controller.

        The controller is responsible for managing the game.
        After starting, the method `set` must be called to set the configurations.
        """
        self.logger = get_logger(self.__class__.__name__)
        self.lang: str = GameConfig.DEFAULT_LANGUAGE
        self.scenes: dict[str, Scene] = {}
        self.scene_id: str = GameConfig.INITIAL_SCENE_ID
        self.screen: pyg.Surface = None
        self.clock: pyg.time.Clock = None
        self.running: bool = True
        self.debug: bool = GameConfig.DEBUG
        self.resource_loader: ResourceLoader = ResourceLoader(
            resource_dir=ResourceConfig.RESOURCE_DIR
        )
        self.localizations: Localizations = Localizations(
            localizations_dir=ResourceConfig.LOCALIZATIONS_DIR
        )
        self.music: Music = Music(music_path=ResourceConfig.MUSIC_DIR)
        self.logger.info("Initialized.")

    @property
    def current_scene(self) -> Scene:
        """
        Get the current scene.

        Returns:
            Scene: The current scene.
        """
        try:
            return self.scenes[self.scene_id]
        except KeyError:
            raise KeyError(f"Scene {self.scene_id} not found.")

    def set(self) -> None:
        """
        Set all necessary configurations for the controller.
        """
        pyg.init()
        pyg.display.set_caption(GameConfig.TITLE)
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        self.screen = pyg.display.set_mode(DisplayConfig.SIZE)
        self.clock = pyg.time.Clock()
        self.screen.fill(Colors.BLACK)
        self.music.init_music()
        self.localizations.load_all_localizations()
        self.resource_loader.load_all_images()
        self.logger.info("Configurations set.")

    # TODO: maybe move to localizations.py
    def set_language(self, lang: str) -> None:
        """
        Set the language for the controller.

        Args:
            lang (str): The language to be set.
        """
        if lang not in GameConfig.LANGUAGES:
            msg = f"Language {lang} not found."
            self.logger.error(msg)
            return
        self.lang = lang
        self.logger.info(f"Language set to {lang}.")

    def populate(self, scenes: list[Scene] = []) -> None:
        """
        Populate the controller with the scenes.

        Args:
            scenes (list[Scene]): The scenes to be added to the controller.
        """
        if len(scenes) == 0:
            msg = "No scenes to populate."
            self.logger.error(msg)
            raise ValueError(msg)
        for scene in scenes:
            self.add_scene(scene)
        if self.debug:
            self.logger.debug("Scenes populated.")

    def add_scene(self, scene: Scene) -> None:
        """
        Add a scene to the controller.

        Args:
            scene (Scene): The scene to be added.
        """
        self.scenes[scene.name] = scene
        if self.debug:
            self.logger.debug(f"Scene added: {scene.name}")

    def change_scene(self, scene_id: str) -> None:
        """
        Change the current scene.

        Args:
            scene_id (str): The id of the scene to change to.
        """
        last_scene = self.scene_id
        self.current_scene.on_exit()
        self.scene_id = scene_id
        self.current_scene.on_enter()
        if self.debug:
            self.logger.debug(f"Scene changed: {last_scene} -> {scene_id}")

    def event_handler(self) -> None:
        """
        Handle the events of the game.
        """
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                self.running = False
            if self.debug:
                pass
            self.current_scene.handle_event(event)
            self.music.handle_event(event)

    def update(self, delta_time: float) -> None:
        """
        Update the game.

        Args:
            delta_time (float): The time since the last update.
        """
        self.current_scene.update(self.screen, delta_time)

    def start(self) -> None:
        """
        Start the controller.
        """
        if not self.screen:
            raise RuntimeError("The controller must be set before starting.")
        try:
            self.current_scene.on_enter()
            self.music.play_music()
            while self.running:
                time_delta = self.clock.tick(GameConfig.FPS) / 1000.0
                self.event_handler()
                self.update(time_delta)
                pyg.display.update()
        except Exception as exc:
            self.logger.error(f"An error occurred: {exc}")
            self.stop()
        finally:
            pyg.quit()
            exit()

    def stop(self) -> None:
        """
        Stop the controller.
        """
        self.running = False
        self.logger.info("Stopped by user.")
        pyg.quit()
        exit()
