"""
Language settings scene.
"""

import pygame as pyg
from ..scene import Scene
from ..constants import Colors, DisplayConfig, GameConfig
from ..components import Button, Dropdown


class LanguageSettingsScene(Scene):
    """
    The language settings scene.
    """

    def __init__(self, controller):
        """
        Create a new language settings scene.
        """
        super().__init__("language_settings_scene", controller, debug=controller.debug)
        self.background: pyg.Surface = None
        self.buttons: list[Button] = []
        self.elements = []

    def calculate_element_position(
        self, element_width: int, element_height: int, index: int, offset_y: int = 0
    ) -> tuple[int, int]:
        """
        Calculate the position of the element based on the index.

        Args:
            element_width (int): The width of the element.
            element_height (int): The height of the element.
            index (int): The index of the element.
            offset_y (int): The vertical offset for the initial position.

        Returns:
            tuple[int, int]: The position of the element.
        """
        element_x = (DisplayConfig.WIDTH - element_width) // 2
        element_y = offset_y + index * (element_height + 10)
        return element_x, element_y

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
        position = self.calculate_element_position(
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

    def add_element(self, element, index: int, offset_y: int = 0):
        """
        Add an element to the scene.

        Args:
            element: The element to add.
            index (int): The index of the element.
            offset_y (int): The vertical offset for the initial position.
        """
        element_width, element_height = element.size
        position = self.calculate_element_position(
            element_width, element_height, index, offset_y
        )
        element.rect.topleft = position
        self.elements.append(element)

    def change_language(self, language: str):
        """
        Change the language of the game.

        Args:
            language (str): The new language.
        """
        self.controller.set_language(language)
        self.controller.change_scene(self.name)

    def on_enter(self):
        self.log("Entering scene.")

        lang = self.controller.lang
        lang_settings = self.controller.localizations.get_key("music_settings", lang)
        glob = self.controller.localizations.get_key("global", lang)

        offset_y = 100

        # adding elements
        self.add_element(
            Dropdown(
                scene=self,
                size=(200, 50),
                name="language_dropdown",
                items=GameConfig.LANGUAGES,
                action=self.change_language,
                selected_key=self.controller.lang,
                position=(0, 0),
                font=pyg.font.Font(None, 24),
                color=Colors.BLUE,
                item_color=Colors.BLACK,
                selected_color=Colors.BLUE,
                debug=self.debug,
            ),
            0,
            offset_y,
        )

        self.add_button(
            "back_btn",
            glob["back"],
            lambda: self.controller.change_scene("settings_scene"),
            4,
        )

    def on_exit(self):
        self.log("Exiting scene.")
        self.background = None
        self.buttons.clear()
        self.elements.clear()

    def handle_event(self, event: list[pyg.event.Event]) -> None:
        for button in self.buttons:
            button.handle_event(event)
        for element in self.elements:
            element.handle_event(event)

    def update(self, screen: pyg.Surface, delta_time: float) -> None:
        screen.fill(Colors.BLACK)
        for button in self.buttons:
            button.draw(screen)
        for element in self.elements:
            element.draw(screen)
