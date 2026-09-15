import pygame
from src.layers.layer_manager import LayerManager
from src.snake.snake_layer import SnakeLayer

class Game:
    def __init__(self, config : dict) -> None:
        self.screen = pygame.display.set_mode((config['window']['width'], config['window']['height']))
        self.clock = pygame.time.Clock()
        self.fps = config['window']['fps']
        self.running = True
        self.layer_manager = LayerManager()
        self.layer_manager.push_layer(SnakeLayer(self.layer_manager, config['game']))

    def run(self) -> None:
        dt = 0

        while self.running:

            self.eventHandler()
            self.update(dt)
            self.render()

            pygame.display.flip()

            dt = self.clock.tick(self.fps) / 1000

        pygame.quit()

    def update(self, dt : float) -> None:
        self.layer_manager.update(dt)

    def eventHandler(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.layer_manager.process_event(event)

    def render(self) -> None:
        self.layer_manager.render(self.screen)