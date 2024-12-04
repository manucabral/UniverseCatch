"""A celestial object"""

from abc import ABC, abstractmethod


class CelestialObject(ABC):
    """
    A celestial object representation in the sky.
    """

    def __init__(self, name: str, description: str, img_path: str) -> None:
        self.name: str = name | "Unknown"
        self.description: str = description | "No description"
        self.img_path: str = img_path | "resources/unknown.png"

    def __str__(self) -> str:
        """The string representation of the object"""
        return f"<CelestialObject {self.name}> {self.description}"

    def __repr__(self) -> str:
        """The representation of the object"""
        return self.__str__()
