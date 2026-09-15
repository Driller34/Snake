import pygame
from src.layers.layer import Layer
from src.layers.layer_manager import LayerManager
import random

class SnakeLayer(Layer):
    def __init__(self, layer_manager : LayerManager):
        self.layer_manager = layer_manager
        
        self.width = 10
        self.height = 10

        self.cell_width = 50
        self.cell_height = 50
        self.gap = 10

        self.snake_positions = [(3, 0), (2, 0), (1, 0), (0, 0)]
        self.velocity = (1, 0)

        self.move_timer = 0.0
        
        self.map = [[0 for i in range(0, self.width)] for i in range(0, self.height)]

        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)

        self.map[y][x] = 1

    def process_event(self, event : pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.velocity = (0, -1)
            if event.key == pygame.K_s:
                self.velocity = (0, 1)
            if event.key == pygame.K_a:
                self.velocity = (-1, 0)
            if event.key == pygame.K_d:
                self.velocity = (1, 0)

    def update(self, dt : float):
        self.move_timer += dt

        if self.move_timer < 0.5:
            return

        self.move_timer -= 0.5

        x, y = self.snake_positions[0]
        vx, vy = self.velocity

        self.snake_positions.insert(0, (x + vx, y + vy))

        if self.map[x + vx][y + vy] == 0:
            self.snake_positions.pop()
        else:
            self.map[x + vx][y + vy] = 0
            self.map[random.randint(0, self.height - 1)][random.randint(0, self.width - 1)] = 1

    def render(self, screen : pygame.Surface) -> None:
        for i in range(0, self.height):
            for j in range(0, self.width):
                color = "green"

                if self.map[j][i] == 1:
                    color = "red"

                if (j, i) in self.snake_positions:
                    color = "black"

                pygame.draw.rect(screen, color, (j * (self.cell_width + self.gap), 
                    i * (self.cell_height + self.gap), 
                    self.cell_width, 
                    self.cell_height))