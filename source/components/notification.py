"""
This module contains the Notification class, which is used to display notifications.
"""

import pygame as pyg
from source.logger import get_logger
from source.constants.colors import Colors


class Notification:
    """
    A class used to display simple notifications.
    """

    def __init__(self, uniqueId: int, message: str, duration: int = 2000):
        """
        Initialize the notification.

        Args:
            uniqueId (int): A unique identifier for the notification
            message (str): The message to display.
            duration (int, optional): The duration to display the notification in milliseconds. Defaults to 2000.
        """
        self.logger = get_logger(f"Notification-{uniqueId}")
        self.message: str = message
        self.duration: int = duration
        self.font: pyg.font.Font = None
        self.text: pyg.Surface = None
        self.rect: pyg.Rect = None
        self.start_time: int = 0
        self.visible: bool = False

    def init(self):
        """
        Initialize the notification.
        """
        self.font = pyg.font.Font(None, 36)
        self.logger.info("Initialized.")

    def update(self, screen: pyg.Surface):
        """
        Update the notification.
        """
        if self.visible:
            current_time = pyg.time.get_ticks()
            if current_time - self.start_time > self.duration:
                self.visible = False
            else:
                screen.blit(self.text, self.rect)

    def show(self):
        """
        Show the notification.
        """
        self.text = self.font.render(self.message, True, Colors.WHITE)
        self.rect = self.text.get_rect()
        self.rect.center = (pyg.display.get_surface().get_width() // 2, 50)
        self.start_time = pyg.time.get_ticks()
        self.visible = True
        self.logger.info("Notification shown.")
