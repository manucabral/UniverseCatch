"""
This module contains the Button class.
"""

import pygame as pyg


class Button:
    """
    A button is an interactive element that can be clicked.
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        font_size: int,
        color: tuple[int, int, int],
        hover_color: tuple[int, int, int],
        action: callable,
    ):
        self.rect = pyg.Rect(x, y, width, height)
        self.text = text
        self.font = pyg.font.Font(None, font_size)
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.hovered = False

    def draw(self, screen: pyg.Surface):
        """
        Draw the button on the screen.

        Args:
            screen (pyg.Surface): The screen to draw the button on.
        """
        color = self.hover_color if self.hovered else self.color
        pyg.draw.rect(screen, color, self.rect)
        text = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def handle_event(self, event: pyg.event.Event):
        """
        Handle an event.

        Args:
            event (pyg.event.Event): The event to handle.
        """
        if event.type == pyg.MOUSEMOTION:
            pyg.mouse.set_system_cursor(
                pyg.SYSTEM_CURSOR_HAND if self.hovered else pyg.SYSTEM_CURSOR_ARROW
            )
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pyg.MOUSEBUTTONDOWN and self.hovered:
            self.action()
