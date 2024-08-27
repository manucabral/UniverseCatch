"""
This is the main file of the project. It is used to run the controller.
"""

import source
import source.scenes

if __name__ == "__main__":
    controller = source.Controller()
    controller.set()
    controller.populate(
        [
            source.scenes.IntroScene(controller),
            source.scenes.MainMenuScene(controller),
            source.scenes.SettingsMenuScene(controller),
            source.scenes.MusicSettingsScene(controller),
            source.scenes.MultiplayerMenuScene(controller),
        ]
    )
    controller.start()
