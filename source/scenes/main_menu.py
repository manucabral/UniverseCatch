"""
Main menu scene.
"""

import pygame as pyg
from ..scene import Scene
from ..constants import Colors
from ..components import Button


class MainMenuScene(Scene):
    """
    The main menu scene.

    This scene is shown when the game starts.
    """

    def __init__(self, controller):
        """
        Create a new intro scene.
        """
        super().__init__("main_menu", controller)
        self.background: pyg.Surface = None
        self.buttons: list[Button] = []

    def on_enter(self):
        """
        Called when the scene is entered.
        """
        lang = self.controller.lang
        menu = self.controller.localizations.get_key("menu", lang)
        self.buttons.append(
            Button(
                scene=self,
                name="play_btn",
                text=menu["play"],
                font=pyg.font.Font(None, 24),
                font_size=24,
                font_color=Colors.WHITE,
                action=lambda: self.controller.change_scene("intro"),
                position=(100, 100),
                size=(100, 50),
                color=Colors.BLUE,
            )
        )

    def on_exit(self): ...

    def update(self, screen: pyg.Surface, delta_time: float) -> None:
        screen.fill(Colors.BLACK)
        for button in self.buttons:
            button.draw(screen)

    def render(self): ...

    def handle_event(self, event: pyg.event.Event) -> None: ...
