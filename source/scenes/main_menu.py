"""
Main menu scene.
"""

import pygame as pyg
from ..scene import Scene
from ..constants import Colors, DisplayConfig
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
        super().__init__("main_menu", controller, debug=controller.debug)
        self.background: pyg.Surface = None
        self.buttons: list[Button] = []

    def calculate_btn_position(
        self, button_width: int, button_height: int, index: int
    ) -> tuple[int, int]:
        """
        Calculate the position of the button based on the index.

        Args:
            button_width (int): The width of the button.
            button_height (int): The height of the button.
            index (int): The index of the button.

        Returns:
            tuple[int, int]: The position of the button.
        """
        btn_x = (DisplayConfig.WIDTH - button_width) // 2
        btn_y = (DisplayConfig.HEIGHT - button_height) // 2 + index * (
            button_height + 10
        )
        return btn_x, btn_y

    def add_button(self, name: str, text: str, action, index: int):
        """
        Add a button to the scene.

        Args:
            name (str): The name of the button.
            text (str): The text of the button.
            action (callable): The action to perform when the button is clicked.
            index (int): The index of the button.
        """
        button_width, button_height = 200, 50
        position = self.calculate_btn_position(button_width, button_height, index)
        button = Button(
            scene=self,
            name=name,
            text=text,
            font=pyg.font.Font(None, 24),
            font_size=24,
            font_color=Colors.WHITE,
            action=action,
            position=position,
            size=(button_width, button_height),
            color=Colors.BLUE,
            debug=self.debug,
        )
        self.buttons.append(button)

    def on_enter(self):
        """
        Called when the scene is entered.
        """
        self.log("Entering scene.")
        lang = self.controller.lang
        menu = self.controller.localizations.get_key("menu", lang)

        # adding buttons
        self.add_button(
            "play_btn",
            menu["play"],
            lambda: self.controller.change_scene("play_scene"),
            0,
        )
        self.add_button(
            "settings_btn",
            menu["settings"],
            lambda: self.controller.change_scene("settings_scene"),
            1,
        )
        self.add_button("exit_btn", menu["exit"], lambda: self.controller.quit(), 2)

    def on_exit(self):
        self.log("Exiting scene.")
        self.buttons.clear()

    def update(self, screen: pyg.Surface, delta_time: float) -> None:
        screen.fill(Colors.BLACK)
        for button in self.buttons:
            button.draw(screen)

    def render(self): ...

    def handle_event(self, event: pyg.event.Event) -> None:
        for button in self.buttons:
            button.handle_event(event)
