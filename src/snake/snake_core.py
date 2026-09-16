import pygame
from enum import Enum
import random

class Cell(Enum):
    EMPTY = 0
    APPLE = 1

class SnakeCore:
    def __init__(self, config : dict) -> None:
        self.width = config["width"]
        self.height = config["height"]

        self.cell_width = config["cell-width"]
        self.cell_height = config["cell-height"]
        self.gap = config["gap"]

        self.empty_color = config["empty-color"]
        self.snake_color = config["snake-color"]
        self.apple_color = config["apple-color"]

        self.snake_positions = [(0, 0)]
        self.velocity = (1, 0)

        self.game_over = False

        self.move_timer = 0.0

        self.map = [[Cell.EMPTY for i in range(0, self.width)] for i in range(0, self.height)]

        self.set_apple()

    def set_apple(self) -> None:
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)

        self.map[y][x] = Cell.APPLE

    def game_over(self) -> bool:
        return self.game_over

    def update(self, dt : float) -> None:
        self.move_timer += dt

        if self.move_timer < 0.5:
            return

        self.move_timer -= 0.5

        x, y = self.snake_positions[0]
        vx, vy = self.velocity
        new_x = x + vx
        new_y = y + vy

        if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height:
            self.game_over = True
            return

        self.snake_positions.insert(0, (new_x, new_y))

        if self.map[new_y][new_x] == Cell.EMPTY:
            self.snake_positions.pop()
        else:
            self.map[new_y][new_x] = Cell.EMPTY
            self.set_apple()

    def render(self, screen : pygame.Surface) -> None:
        for i in range(0, self.height):
            for j in range(0, self.width):
                color = self.empty_color

                if self.map[i][j] == Cell.APPLE:
                    color = self.apple_color

                if (j, i) in self.snake_positions:
                    color = self.snake_color

                pygame.draw.rect(screen, color, (j * (self.cell_width + self.gap), 
                    i * (self.cell_height + self.gap), 
                    self.cell_width, 
                    self.cell_height))

    def move_up(self) -> None:
        self.velocity = (0, -1)

    def move_down(self) -> None:
        self.velocity = (0, 1)

    def move_right(self) -> None:
        self.velocity = (1, 0)

    def move_left(self) -> None:
        self.velocity = (-1, 0)