"""
This module contains the Controller class.
This class is responsible for managing the game.
"""

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
        self.current_scene: Scene = None
        self.screen: pyg.Surface = None
        self.clock: pyg.time.Clock = None
        self.running: bool = True

    def set(self) -> None:
        """
        Set all necessary configurations for the controller.
        """
        pyg.init()
        pyg.display.set_caption(GameConfig.TITLE)
        self.screen = pyg.display.set_mode(DisplayConfig.SIZE)
        self.clock = pyg.time.Clock()
        self.screen.fill(Colors.BLACK)
        self.populate()

    def populate(self) -> None:
        """
        Populate the controller with the scenes.
        """
        self.add_scene(IntroScene())

    def add_scene(self, scene: Scene) -> None:
        """
        Add a scene to the controller.

        Args:
            scene (Scene): The scene to be added.
        """
        self.scenes[scene.name] = scene

    def start(self) -> None:
        """
        Start the controller.
        """
        if not self.screen:
            raise RuntimeError("The controller must be set before starting.")
        while self.running:
            self.clock.tick(GameConfig.FPS)
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.running = False
            pyg.display.flip()
        pyg.quit()
        exit()
