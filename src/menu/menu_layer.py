import pygame
from src.layers.layer import Layer
from src.layers.layer_manager import LayerManager
from src.snake.snake_layer import SnakeLayer
from src.gui.button import Button
from src.gui.label import Label

class MenuLayer(Layer):
    def __init__(self, layer_manager : LayerManager, config : dict) -> None:
        self.layer_manager = layer_manager
        self.config = config

        self.gui_config = self._get_gui_config()

        self.big_font = pygame.font.Font(None, config['font']['big-font'])
        self.mid_font = pygame.font.Font(None, config['font']['mid-font']) 

        self.label = Label(self.big_font, "MENU", "white", self.gui_config['label'])   
        self.new_game_button = Button(self.mid_font, "New Game", "white", 
                                      "green", self.gui_config['new_game'], self._new_game)
        self.exit_button = Button(self.mid_font, "Exit", "white", 
                                  "red", self.gui_config['exit'], self._exit_game)

    def _new_game(self) -> None:
        self.layer_manager.push_layer(SnakeLayer(self.layer_manager, self.config))
    
    def _exit_game(self) -> None:
        self.layer_manager.pop_layer()

    def _get_gui_config(self) -> dict:
        x = self.config['window']['width'] / 2
        y = self.config['window']['height'] / 2

        return {
            'label' : (x, y - 200),
            'new_game' : pygame.Rect(x - 150, y - 100, 300, 100),
            'exit' : pygame.Rect(x - 150, y + 20, 300, 100)
        }

    def process_event(self, event : pygame.event.Event) -> None:
        self.exit_button.process_event(event)
        self.new_game_button.process_event(event)

    def update(self, dt : float):
        pass

    def render(self, screen : pygame.Surface) -> None:
        self.label.render(screen)
        self.exit_button.render(screen)
        self.new_game_button.render(screen)