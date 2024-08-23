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
        self.text = text
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.font_object = self.font.render(self.text, True, self.font_color)
        self.font_rect = self.font_object.get_rect(center=self.rect.center)
        self.action = action or (lambda: None)
        self.logger.debug("Initialized.")

    def draw(self, screen: pyg.Surface) -> None:
        """
        Draw the button on the screen.
        """
        super().draw(screen)
        if self.is_hovered:
            pyg.draw.rect(screen, self.color, self.rect)
            pyg.mouse.set_cursor(pyg.SYSTEM_CURSOR_HAND)
        else:
            pyg.mouse.set_cursor(pyg.SYSTEM_CURSOR_ARROW)
            pyg.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.font_object, self.font_rect)

    def handle_event(self, event: pyg.event.Event) -> None:
        super().handle_event(event)
        if event.type == pyg.MOUSEBUTTONDOWN:
            if self.is_hovered:
                self.log("Clicked")
                self.action()
