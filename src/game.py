import pygame
from src.layers.layer_manager import LayerManager
from src.snake_layer import SnakeLayer

class Game:
    def __init__(self, width : int, height : int, fps : int = 60) -> None:
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.layer_manager = LayerManager()
        self.layer_manager.push_layer(SnakeLayer())

    def run(self) -> None:
        dt = 0

        while self.running:

            self.eventHandler()
            self.update(dt)
            self.render()

            pygame.display.flip()

            dt = self.clock.tick(self.fps) / 1000

        pygame.quit()

    def update(self, dt) -> None:
        self.layer_manager.update(dt)

    def eventHandler(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.layer_manager.process_event(event)

    def render(self) -> None:
        self.layer_manager.render()