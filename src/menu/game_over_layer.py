import pygame
from src.layers.layer import Layer
from src.layers.layer_manager import LayerManager
from src.gui.button import Button
from src.gui.label import Label

class GameOverLayer(Layer):
    def __init__(self, layer_manager : LayerManager, config : dict) -> None:
        self.layer_manager = layer_manager
        self.config = config

        self.gui_config = self._get_gui_config()

        self.big_font = pygame.font.Font(None, config['font']['big-font'])
        self.mid_font = pygame.font.Font(None, config['font']['mid-font']) 

        self.label = Label(self.big_font, "Game Over", "white", self.gui_config['label'])   

        self.menu_button = Button(self.mid_font, "Menu", "white", 
                                      "gray", self.gui_config['menu'], self._menu)

        self.exit_button = Button(self.mid_font, "Exit", "white", 
                                  "gray", self.gui_config['exit'], self._exit)   

    def _get_gui_config(self) -> dict:
        x = self.config['window']['width'] / 2
        y = self.config['window']['height'] / 2

        return {
            'label' : (x, y - 200),
            'menu' : pygame.Rect(x - 150, y - 100, 300, 100),
            'exit' : pygame.Rect(x - 150, y + 20, 300, 100)
        }   

    def _menu(self) -> None:
        self.layer_manager.pop_layer(2)

    def _exit(self) -> None:
        self.layer_manager.pop_layer(3)

    def process_event(self, event : pygame.event.Event) -> None:
        self.menu_button.process_event(event)
        self.exit_button.process_event(event)

    def update(self, dt : float):
        pass

    def render(self, screen : pygame.Surface) -> None:
        self.label.render(screen)
        self.menu_button.render(screen)
        self.exit_button.render(screen)