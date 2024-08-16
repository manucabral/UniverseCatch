"""A celestial object"""

from abc import ABC, abstractmethod

class CelestialObject(ABC):
    """
    A celestial object representation in the sky.
    """
    def __init__(self, name: str, description: str, img_path: str) -> None:
        self.name = name
        self.description = description
        self.img_path = img_path
    
    @abstractmethod
    def effect(self, state: dict) -> None:
        """
        Define the special effect on this card when it is played

        Args:
            state (dict): The current state of the game

        Returns:
            None: This method does not return anything
        """
        pass

    def __str__(self) -> str:
        """The string representation of the object"""
        return f"<CelestialObject {self.name}> {self.description}"
    
    def __repr__(self) -> str:
        """The representation of the object"""
        return self.__str__()