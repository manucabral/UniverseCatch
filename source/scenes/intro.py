"""
Intro scene module.
"""

import pygame
from ..scene import Scene
from ..constants import Colors, GameConfig
from ..components import Button
from ..components import Text


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
        self.texts: list[Text] = []

    def on_enter(self):
        self.texts.append(
            Text(
                text=f"Welcome to {GameConfig.TITLE}",
                font=pygame.font.Font(None, 50),
                font_size=50,
                font_color=Colors.WHITE,
                position=(10, 50),
                scene=self,
                size=(400, 100),
                color=Colors.WHITE,
                name="title_text",
            )
        )
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
