"""
Multiplayer menu scene.
"""

import pygame as pyg
from ..scene import Scene
from ..constants import Colors, DisplayConfig
from ..components import Button


class MultiplayerMenuScene(Scene):
    """
    The multiplayer menu scene.
    """

    def __init__(self, controller):
        """
        Create a new multiplayer menu scene.
        """
        super().__init__("multiplayer_menu_scene", controller, debug=controller.debug)
        self.background: pyg.Surface = None
        self.buttons: list[Button] = []

    def calculate_btn_position(
        self, button_width: int, button_height: int, index: int, offset_y: int = 0
    ) -> tuple[int, int]:
        """
        Calculate the position of the button based on the index.

        Args:
            button_width (int): The width of the button.
            button_height (int): The height of the button.
            index (int): The index of the button.
            offset_y (int): The vertical offset for the initial position.

        Returns:
            tuple[int, int]: The position of the button.
        """
        btn_x = (DisplayConfig.WIDTH - button_width) // 2
        btn_y = offset_y + index * (button_height + 10)
        return btn_x, btn_y

    def add_button(self, name: str, text: str, action, index: int, offset_y: int = 0):
        """
        Add a button to the scene.

        Args:
            name (str): The name of the button.
            text (str): The text of the button.
            action (callable): The action to perform when the button is clicked.
            index (int): The index of the button.
            offset_y (int): The vertical offset for the initial position.
        """
        button_width, button_height = 200, 50
        position = self.calculate_btn_position(
            button_width, button_height, index, offset_y
        )
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
        self.log("Entering scene.")

        lang = self.controller.lang
        multi_settings = self.controller.localizations.get_key("multiplayer_menu", lang)
        glob = self.controller.localizations.get_key("global", lang)

        offset_y = 100
        state = self.controller.music.paused
        self.add_button(
            "create_room_btn",
            multi_settings["create"],
            lambda: self.controller.change_scene("create_room_scene"),
            0,
            offset_y,
        )
        self.add_button(
            "join_room_btn",
            multi_settings["join"],
            lambda: self.controller.change_scene("join_room_scene"),
            1,
            offset_y,
        )
        self.add_button(
            "back_btn",
            glob["back"],
            lambda: self.controller.change_scene("main_menu"),
            4,
            offset_y,
        )

    def on_exit(self):
        self.log("Exiting scene.")
        self.background = None
        self.buttons.clear()

    def handle_event(self, event: list[pyg.event.Event]) -> None:
        for button in self.buttons:
            button.handle_event(event)

    def update(self, screen: pyg.Surface, delta_time: float) -> None:
        screen.fill(Colors.BLACK)
        for button in self.buttons:
            button.draw(screen)
