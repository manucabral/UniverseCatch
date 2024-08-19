"""
This module contains the Scene class which is used to represent a scene in the game.
Eg. The intro, main menu, the game itself, etc.
"""

from abc import ABC, abstractmethod
import pygame as pyg


class Scene(ABC):
    """
    A scene is a collection of entities that are rendered together.
    """

    def __init__(self, name: str, controller):
        """
        Create a new scene with the given name.

        Args:
            name (str): The name of the scene.
        """
        self.controller = controller
        self.name = name
        self.done = False

    @abstractmethod
    def on_enter(self):
        """
        Called when the scene is entered.
        """

    @abstractmethod
    def on_exit(self):
        """
        Called when the scene is exited.
        """

    @abstractmethod
    def update(self, screen: pyg.Surface, delta_time: float):
        """
        Update the scene.


        Args:
            screen (pyg.Surface): The screen to render the scene on.
            delta_time (float): The time since the last update
        """

    @abstractmethod
    def render(self):
        """
        Render the scene.
        """

    @abstractmethod
    def handle_event(self, event: pyg.event.Event):
        """
        Handle an event.

        Args:
            event (pyg.event.Event): The event to handle.
        """
