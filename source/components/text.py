import pygame as pyg
from .component import Component

class Text(Component):
    """
    A text component.
    """

    def __init__(
        self,
        text: str,
        font: pyg.font.Font,
        font_size: int,
        font_color: tuple[int, int, int],
        *args,
        **kwargs,
    ):
        """
        Create a new text component.

        Args:
            text (str): The text to display.
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

    def draw(self, screen: pyg.Surface) -> None:
        """
        Draw the text on the screen.
        """
        super().draw(screen)
        screen.blit(self.font_object, self.font_rect)

    def set_text(self, text: str) -> None:
        """
        Set the text of the component.

        Args:
            text (str): The new text to display.
        """
        self.text = text
        self.font_object = self.font.render(self.text, True, self.font_color)
        self.font_rect = self.font_object.get_rect(center=self.rect.center)