import pygame as pyg
from .component import Component
from ..scene import Scene
from ..constants import Colors


class Dropdown(Component):
    """
    A dropdown component that allows selecting an item from a dictionary.
    """

    def __init__(
        self,
        scene: Scene,
        size: tuple[int, int],
        name: str,
        items: dict[str, str],
        position: tuple[int, int] = (0, 0),
        action: callable = None,
        selected_key: str = None,
        color: tuple[int, int, int] = Colors.BLUE,
        item_color: tuple[int, int, int] = Colors.BLACK,
        selected_color: tuple[int, int, int] = Colors.BLUE,
        font_color: tuple[int, int, int] = Colors.WHITE,
        font: pyg.font.Font = None,
        visible: bool = True,
        debug: bool = False,
    ):
        """
        Create a new dropdown component.

        Args:
            scene (Scene): The scene the component belongs to.
            size (tuple[int, int]): The size of the component.
            name (str): The name of the component.
            items (dict): The items to display in the dropdown.
            position (tuple[int, int]): The position of the component.
            color (tuple[int, int, int]): The color of the component.
            item_color (tuple[int, int, int]): The color of the items.
            selected_color (tuple[int, int, int]): The color of the selected item.
            font_color (tuple[int, int, int]): The color of the font.
            font (pyg.font.Font): The font to use for the text.
            visible (bool): Whether the component is visible or not.
            debug (bool): Whether to log debug messages or not.
            action (callable): Function to call when an item is selected.
        """
        super().__init__(scene, size, name, position, color, visible, debug)
        self.items: dict[str, str] = items
        self.item_color: tuple[int, int, int] = item_color
        self.action: callable = action
        self.selected_color: tuple[int, int, int] = selected_color
        self.font_color: tuple[int, int, int] = font_color
        self.font = font or pyg.font.Font(None, 24)
        self.selected_key = selected_key or next(iter(self.items.keys()))
        self.expanded = False

    def draw(self, screen: pyg.Surface) -> None:
        """
        Draw the dropdown on the screen.

        Args:
            screen (pyg.Surface): The surface to draw the component on.
        """
        if not self.visible:
            return
        pyg.draw.rect(screen, self.selected_color, self.rect, 2)
        pyg.draw.rect(screen, self.color, self.rect.inflate(-4, -4))
        text = self.font.render(self.items[self.selected_key], True, self.font_color)
        text_rect = text.get_rect(center=(self.rect.centerx, self.rect.centery))
        screen.blit(text, text_rect)

        if self.expanded:
            # Draw the dropdown items
            mouse_pos = pyg.mouse.get_pos()
            for i, (key, item) in enumerate(self.items.items()):
                item_rect = pyg.Rect(
                    self.rect.x,
                    self.rect.y + (i + 1) * self.rect.height,
                    self.rect.width,
                    self.rect.height,
                )
                # Check if mouse is over the item
                if item_rect.collidepoint(mouse_pos):
                    item_bg_color = self.selected_color
                    pyg.mouse.set_cursor(pyg.SYSTEM_CURSOR_HAND)
                else:
                    item_bg_color = (
                        self.item_color
                        if key != self.selected_key
                        else self.selected_color
                    )
                    pyg.mouse.set_cursor(pyg.SYSTEM_CURSOR_ARROW)

                pyg.draw.rect(screen, item_bg_color, item_rect)
                item_text = self.font.render(item, True, self.font_color)
                item_text_rect = item_text.get_rect(
                    center=(item_rect.centerx, item_rect.centery)
                )
                screen.blit(item_text, item_text_rect)

    def handle_event(self, event: pyg.event.Event) -> None:
        """
        Handle an event.

        Args:
            event (pyg.event.Event): The event to handle.
        """
        super().handle_event(event)
        if event.type == pyg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.toggle()
            elif self.expanded:
                clicked_inside = False
                for i, key in enumerate(self.items.keys()):
                    item_rect = pyg.Rect(
                        self.rect.x,
                        self.rect.y + (i + 1) * self.rect.height,
                        self.rect.width,
                        self.rect.height,
                    )
                    if item_rect.collidepoint(event.pos):
                        self.select_item(key)
                        self.toggle()
                        clicked_inside = True
                        break
                if not clicked_inside:
                    self.expanded = False

    def toggle(self) -> None:
        """
        Toggle the expanded state of the dropdown.
        """
        self.expanded = not self.expanded
        self.log(f"Toggled expanded state: {self.expanded}")

    def select_item(self, key: str) -> None:
        """
        Select an item from the dropdown.

        Args:
            key (str): The key of the item to select.
        """
        self.selected_key = key
        self.log(f"Selected item: {self.items[key]}")
        if self.action:
            self.action(key)
