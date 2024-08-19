"""
Intro scene module.
"""

import pygame
from ..scene import Scene
from ..constants import Colors
from ..components import Button


class IntroScene(Scene):
    """
    The intro scene.

    This scene is shown when the game starts.
    """

    def __init__(self, controller):
        """
        Create a new intro scene.
        """
        super().__init__("intro", controller)
        self.buttons: list[Button] = []

    def on_enter(self):
        self.buttons.append(
            Button(
                action=lambda: self.controller.change_scene("game"),
                text="Start",
                font=pygame.font.Font(None, 50),
                font_size=50,
                font_color=Colors.WHITE,
                color=Colors.BLUE,
                size=(200, 100),
                position=(300, 300),
                name="start_button",
                scene=self,
            )
        )

    def on_exit(self):
        self.buttons.clear()

    def update(self, screen, delta_time):
        screen.fill(Colors.BLACK)
        for button in self.buttons:
            button.draw(screen)

    def render(self):
        pass

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)
