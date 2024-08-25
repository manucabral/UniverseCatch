"""
Intro scene module.
"""

import pygame as pyg
from ..scene import Scene


class IntroScene(Scene):
    """
    The intro scene.

    This scene is shown when the game starts.
    """

    def __init__(self, controller):
        """
        Create a new intro scene.
        """
        super().__init__("intro", controller, debug=controller.debug)
        self.background: pyg.Surface = None
        self.zoom_factor: float = 1.0
        self.zoom_speed: float = 0.3
        self.time_elapsed: float = 0.0
        self.max_time: float = 3.0
        self.background_size: tuple[int, int] = (1000, 600)

    def on_enter(self):
        self.log("Entering scene.")
        self.background = self.controller.resource_loader.images["screen_loading"]
        self.background = pyg.transform.scale(self.background, self.background_size)

    def on_exit(self):
        self.log("Exiting scene.")
        self.background = None
        self.zoom_factor = 1.0
        self.time_elapsed = 0.0

    def update(self, screen: pyg.Surface, delta_time: float) -> None:
        self.time_elapsed += delta_time
        self.zoom_factor += self.zoom_speed * delta_time

        new_width = int(self.background.get_width() * self.zoom_factor)
        new_height = int(self.background.get_height() * self.zoom_factor)
        zoomed_background = pyg.transform.scale(
            self.background, (new_width, new_height)
        )
        x = (screen.get_width() - new_width) // 2
        y = (screen.get_height() - new_height) // 2
        screen.blit(zoomed_background, (x, y))

        if self.time_elapsed > self.max_time:
            self.controller.change_scene("main_menu")

    def handle_event(self, event: pyg.event.Event) -> None: ...
