import pygame
from src.layers.layer import Layer
from src.layers.layer_manager import LayerManager
from src.snake.snake_layer import SnakeLayer

class MenuLayer(Layer):
    def __init__(self, layer_manager : LayerManager, config : dict) -> None:
        self.layer_manager = layer_manager
        self.config = config

        x = self.config['window']['width'] / 2 - 150
        y = self.config['window']['height'] / 2 - 100

        self.new_game_button = pygame.Rect(x, y, 300, 100)
        self.exit_button = pygame.Rect(x, y + 120, 300, 100)

    def process_event(self, event : pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.new_game_button.collidepoint(event.pos):
                self.layer_manager.push_layer(SnakeLayer(self.layer_manager, self.config['game']))
            elif self.exit_button.collidepoint(event.pos):
                self.layer_manager.pop_layer()

    def update(self, dt : float):
        pass

    def render(self, screen : pygame.Surface) -> None:
        pygame.draw.rect(screen, "green", self.new_game_button)
        pygame.draw.rect(screen, "red", self.exit_button)