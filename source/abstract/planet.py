from .celestial_object import CelestialObject


class Planet(CelestialObject):

    def __init__(self, name: str, description: str, img_path: str) -> None:
        super().__init__(name, description, img_path)
