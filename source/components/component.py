"""
This module contains the base class for all components in the game.
"""

import pygame as pyg

from ..scene import Scene
from ..logger import get_logger


class Component:
    """
    A component is a part of a scene that can be drawn on the screen.
    """

    def __init__(
        self,
        scene: Scene,
        size: tuple[int, int],
        position: tuple[int, int],
        color: tuple[int, int, int],
        name: str,
        visible: bool = True,
        debug: bool = False,
    ):
        """
        Create a new component.

        Args:
            scene (Scene): The scene the component belongs to.
            size (tuple[int, int]): The size of the component.
            position (tuple[int, int]): The position of the component.
            color (tuple[int, int, int]): The color of the component.
            name (str): The name of the component.
            visible (bool): Whether the component is visible or not.
            debug (bool): Whether to log debug messages or not.
        """
        self.scene = scene
        self.size = size
        self.position = position
        self.color = color
        self.name = name
        self.visible = visible
        self.rect = pyg.Rect(self.position, self.size)
        self.logger = get_logger(self.name or self.__class__.__name__)
        self.debug = debug
        self.is_hovered = False
        self.was_hovered = False

    def draw(self, screen: pyg.Surface) -> None:
        """
        Draw the component on the screen.

        Args:
            screen (pyg.Surface): The surface to draw the component on.
        """
        if not self.visible:
            return

    def collidepoint(self, point: tuple[int, int]) -> bool:
        """
        Check if a point is inside the component.

        Args:
            point (tuple[int, int]): The point to check.

        Returns:
            bool: True if the point is inside the component, False otherwise.
        """
        return self.rect.collidepoint(point)

    def _check_hover(self, position: tuple[int, int]) -> None:
        """
        Check if the mouse is hovering over the component.

        Args:
            position (tuple[int, int]): The position of the mouse.
        """
        self.is_hovered = self.rect.collidepoint(position)
        if self.is_hovered != self.was_hovered:
            if self.is_hovered:
                self.log("Hovering over the component.")
            elif not self.is_hovered:
                self.log("No longer hovering over the component.")
            self.was_hovered = self.is_hovered

    def handle_event(self, event: pyg.event.Event) -> None:
        """
        Handle an event.

        Args:
            event (pyg.event.Event): The event to handle.
        """
        if event.type == pyg.MOUSEMOTION:
            self._check_hover(position=event.pos)

    def log(self, message: str) -> None:
        """
        Log a debug message if debugging is enabled.

        Args:
            message (str): The message to log.
        """
        if self.debug:
            self.logger.debug(message)
