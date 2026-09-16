import pygame
from src.layers.layer import Layer
from src.layers.layer_manager import LayerManager
from src.snake.snake_core import SnakeCore

class SnakeLayer(Layer):
    def __init__(self, layer_manager : LayerManager, config : dict) -> None:
        self.layer_manager = layer_manager
        
        self.snake = SnakeCore(config)

    def process_event(self, event : pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.snake.move_up()
            elif event.key == pygame.K_s:
                self.snake.move_down()
            elif event.key == pygame.K_a:
                self.snake.move_left()
            elif event.key == pygame.K_d:
                self.snake.move_right()

    def update(self, dt : float):
        if self.snake.game_over:
            return

        self.snake.update(dt)

    def render(self, screen : pygame.Surface) -> None:
        self.snake.render(screen)