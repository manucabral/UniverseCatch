"""
This module contains the Button class.
"""

import pygame as pyg
from .component import Component


class Button(Component):
    """
    A button component.
    """

    def __init__(
        self,
        text: str,
        font: pyg.font.Font,
        font_size: int,
        font_color: tuple[int, int, int],
        action: callable,
        *args,
        **kwargs,
    ):
        """
        Create a new button.

        Args:
            text (str): The text to display on the button.
            font (pyg.font.Font): The font to use for the text.
            font_size (int): The size of the font.
            font_color (tuple[int, int, int]): The color of the font.

        Inherited Args:
            See Component class.
        """
        super().__init__(*args, **kwargs)
        self.text: str = text
        self.font: pyg.font.Font = font
        self.font_size: int = font_size
        self.font_color: tuple[int, int, int] = font_color
        self.font_object: pyg.Surface = self.font.render(
            self.text, True, self.font_color
        )
        self.font_rect: pyg.Rect = self.font_object.get_rect(center=self.rect.center)
        self.action = action or (lambda: None)
        self.previous_hover_state: bool = False
        self.logger.debug("Initialized.")

    @property
    def textContent(self) -> str:
        return self.text

    @textContent.setter
    def textContent(self, value: str) -> None:
        self.text = value
        self.font_object = self.font.render(self.text, True, self.font_color)
        self.font_rect = self.font_object.get_rect(center=self.rect.center)

    def draw(self, screen: pyg.Surface) -> None:
        """
        Draw the button on the screen.
        """
        super().draw(screen)
        if self.is_hovered:
            pyg.draw.rect(screen, self.color, self.rect)
            if not self.previous_hover_state:
                pyg.mouse.set_cursor(pyg.SYSTEM_CURSOR_HAND)
        else:
            pyg.draw.rect(screen, self.color, self.rect, 2)
            if self.previous_hover_state:
                pyg.mouse.set_cursor(pyg.SYSTEM_CURSOR_ARROW)

        screen.blit(self.font_object, self.font_rect)
        self.previous_hover_state = self.is_hovered

    def handle_event(self, event: pyg.event.Event) -> None:
        super().handle_event(event)
        if event.type == pyg.MOUSEBUTTONDOWN:
            if self.is_hovered:
                self.log("Clicked")
                self.action()
