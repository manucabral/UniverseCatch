from abstract.celestial_object import CelestialObject

class Planet(CelestialObject):
    """
    This is the Planet class, represents a Planet card in the game.
    """
    def __init__(self, name: str, description: str, img_path: str) -> None:
        """Constructor for the Planet class"""
        super().__init__(name, description, img_path)
    
    def effect(self, state: dict) -> None:
        """
        Planets have no special effect when played.
        """
        return super().effect(state)