"""
Music Settings scene menu.
"""

import pygame as pyg
from ..scene import Scene
from ..constants import Colors, DisplayConfig
from ..components import Button


class MusicSettingsScene(Scene):
    """
    The settings scene.
    """

    def __init__(self, controller):
        """
        Create a new music settings scene.
        """
        super().__init__("music_settings_scene", controller, debug=controller.debug)
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

    def toggle_music(self, target: Button):
        """
        Toggle the music on and off.

        Args:
            state (bool): The current state of the music.
            target (Button): The button that was clicked.
        """
        self.controller.music.toggle_pause()
        state = self.controller.music.paused
        target.textContent = self.controller.localizations.get_key(
            "music_settings", self.controller.lang
        )["off" if state else "on"]

    def on_enter(self):
        self.log("Entering scene.")

        lang = self.controller.lang
        music_settings = self.controller.localizations.get_key("music_settings", lang)
        glob = self.controller.localizations.get_key("global", lang)

        # adding buttons with an offset of 100 pixels from the top
        offset_y = 100
        state = self.controller.music.paused
        self.add_button(
            "state_btn",
            music_settings["off"] if state else music_settings["on"],
            lambda: self.toggle_music(self.buttons[0]),
            0,
            offset_y,
        )
        self.add_button(
            "volume_up_btn",
            music_settings["up"],
            lambda: self.controller.music.set_volume(
                min(1.0, self.controller.music.get_volume + 0.1)
            ),
            1,
            offset_y,
        )
        self.add_button(
            "volume_down_btn",
            music_settings["down"],
            lambda: self.controller.music.set_volume(
                max(0.0, self.controller.music.get_volume - 0.1)
            ),
            2,
            offset_y,
        )
        self.add_button(
            "back_btn",
            glob["back"],
            lambda: self.controller.change_scene("settings_scene"),
            3,
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
