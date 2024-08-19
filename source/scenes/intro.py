"""
Intro scene module.
"""

from ..scene import Scene
from ..constants import Colors
from ..components import Button


class IntroScene(Scene):
    """
    The intro scene.

    This scene is shown when the game starts.
    """

    def __init__(self, controller):
        """
        Create a new intro scene.
        """
        super().__init__("intro", controller)
        self.buttons: list[Button] = []

    def on_enter(self):
        self.buttons.append(
            Button(
                100,
                100,
                200,
                50,
                "Test",
                30,
                Colors.BLUE,
                Colors.LIGHT_BLUE,
                lambda: self.controller.change_scene("game"),
            )
        )

    def on_exit(self):
        self.buttons.clear()

    def update(self, screen, delta_time):
        screen.fill(Colors.BLACK)
        for button in self.buttons:
            button.draw(screen)

    def render(self):
        pass

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)
