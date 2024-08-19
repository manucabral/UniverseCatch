"""
This module contains the Controller class.
This class is responsible for managing the game.
"""

import os
import pygame as pyg
from .scene import Scene
from .constants import DisplayConfig, Colors, GameConfig
from .scenes import IntroScene


class Controller:
    def __init__(self):
        """
        Initialize the controller.

        The controller is responsible for managing the game.
        After starting, the method `set` must be called to set the configurations.
        """
        self.scenes: dict[str, Scene] = {}
        self.scene_id: str = GameConfig.INITIAL_SCENE_ID
        self.screen: pyg.Surface = None
        self.clock: pyg.time.Clock = None
        self.running: bool = True
        self.debug: bool = GameConfig.DEBUG

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

    def populate(self, scenes: list[Scene] = []) -> None:
        """
        Populate the controller with the scenes.

        Args:
            scenes (list[Scene]): The scenes to be added to the controller.
        """
        if len(scenes) == 0:
            raise ValueError("At least one scene must be provided.")
        for scene in scenes:
            self.add_scene(scene)

    def add_scene(self, scene: Scene) -> None:
        """
        Add a scene to the controller.

        Args:
            scene (Scene): The scene to be added.
        """
        self.scenes[scene.name] = scene
        if self.debug:
            print(f"Scene {scene.name} added.")

    def change_scene(self, scene_id: str) -> None:
        """
        Change the current scene.

        Args:
            scene_id (str): The id of the scene to change to.
        """
        self.current_scene.on_exit()
        self.scene_id = scene_id

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
            while self.running:
                time_delta = self.clock.tick(GameConfig.FPS) / 1000.0
                self.event_handler()
                self.update(time_delta)
                pyg.display.update()
        except Exception as exc:
            print(f"An error occurred: {exc}")
            raise exc
        finally:
            pyg.quit()
            exit()
