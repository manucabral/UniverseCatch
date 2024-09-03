"""
Constants for the game resources.
"""


class ResourceConfig:
    """
    Configuration for the game resources.
    """

    CONFIG_FILE: str = "config.json"
    RESOURCE_DIR: str = "resources"
    LOCALIZATIONS_DIR: str = RESOURCE_DIR + "/localizations"
    PLANETS_DIR: str = RESOURCE_DIR + "/planets"
    SOUNDS_DIR: str = RESOURCE_DIR + "/sounds"
    MUSIC_DIR: str = RESOURCE_DIR + "/music"

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

    MUSICS: dict = {
        "Calm Cosmos": "calm_cosmos.mp3",
        "Deep Space": "deep_space.mp3",
    }
