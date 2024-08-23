"""
Constants for the game resources.
"""


class ResourceConfig:
    """
    Configuration for the game resources.
    """

    RESOURCE_DIR: str = "resources"
    LOCALIZATIONS_DIR: str = RESOURCE_DIR + "/localizations"
    PLANETS_DIR: str = RESOURCE_DIR + "/planets"

    PLANETS: dict = {
        0: "mercury.png",
        1: "venus.png",
        2: "earth.png",
        3: "mars.png",
        4: "jupiter.png",
        5: "saturn.png",
        6: "uranus.png",
        7: "neptune.png",
        8: "pluto.png",
        9: "bellerophonn.png",
    }
