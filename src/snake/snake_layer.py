import pygame
from src.layers.layer import Layer
from src.layers.layer_manager import LayerManager
from src.snake.snake_core import SnakeCore
from src.menu.game_over_layer import GameOverLayer

class SnakeLayer(Layer):
    def __init__(self, layer_manager : LayerManager, config : dict) -> None:
        self.layer_manager = layer_manager
        self.config = config
        
        self.snake = SnakeCore(config['game'])

    def process_event(self, event : pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.snake.set_drection_up()
            elif event.key == pygame.K_s:
                self.snake.set_drection_down()
            elif event.key == pygame.K_a:
                self.snake.set_drection_left()
            elif event.key == pygame.K_d:
                self.snake.set_drection_right()

    def update(self, dt : float):
        if self.snake.is_game_over:
            self.layer_manager.push_layer(GameOverLayer(self.layer_manager, self.config))

        self.snake.update(dt)

    def render(self, screen : pygame.Surface) -> None:
        self.snake.render(screen)