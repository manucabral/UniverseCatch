"""
Image component
"""

import pygame as pyg
from .component import Component


class Image(Component):
    """
    An image component.
    """

    def __init__(self, image: pyg.Surface, *args, **kwargs):
        """
        Create a new image.

        Args:
            image (pyg.Surface): The image to display.

        Inherited Args:
            See Component class.
        """
        super().__init__(*args, **kwargs)
        self.image: pyg.Surface = image
        self.rescale(self.size)
        self.logger.debug("Initialized.")

    def rescale(self, size: tuple[int, int]) -> None:
        """
        Rescale the image to the given size.

        Args:
            size (tuple[int, int]): The new size of the image.
        """
        self.image = pyg.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, screen: pyg.Surface) -> None:
        """
        Draw the image on the screen.
        """
        super().draw(screen)
        screen.blit(self.image, self.rect)
