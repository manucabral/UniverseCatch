"""
Intro scene module.
"""

from ..scene import Scene


class IntroScene(Scene):
    """
    The intro scene.

    This scene is shown when the game starts.
    """

    def __init__(self):
        """
        Create a new intro scene.
        """
        super().__init__("intro")

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def handle_event(self, event):
        pass
