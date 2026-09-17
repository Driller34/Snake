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
        self.direction = (1, 0)

        self._game_over = False

        self.move_timer = 0.0
        self.timeout = config["timeout"]

        self.map = [[Cell.EMPTY for i in range(0, self.width)] for i in range(0, self.height)]

        self._set_apple()

    def _is_valid_position(self, position : tuple[int, int]) -> bool:
        return (position[0] >= 0 
            and position[0] < self.width 
            and position[1] >= 0 
            and position[1] < self.height 
            and position not in self.snake_positions[0:-2])

    def _new_position(self) -> tuple:
        x, y = self.snake_positions[0]
        dx, dy = self.direction

        return (x + dx, y + dy)

    def _set_apple(self) -> None:
        n = self.width * self.height

        r = random.randint(0, n - 1)

        for i in range(n):
            x = r % self.width
            y = r // self.width

            if (x, y) not in self.snake_positions:
                self.map[y][x] = Cell.APPLE
                return

            r = (r + 1) % n

        self._game_over = True

    def _set_direction(self, direction : tuple[int, int]) -> None:
        dx, dy = direction

        if self.direction != (-dx, -dy):
            self.direction = (dx, dy)

    def _move_snake(self):
        x, y = self._new_position()

        if not self._is_valid_position((x, y)):
            self._game_over = True
            return

        self.snake_positions.insert(0, (x, y))

        if self.map[y][x] == Cell.EMPTY:
            self.snake_positions.pop()
        else:
            self.map[y][x] = Cell.EMPTY
            self._set_apple()

    @property
    def is_game_over(self) -> bool:
        return self._game_over

    def update(self, dt : float) -> None:
        self.move_timer += dt

        if self.move_timer < self.timeout:
            return

        self.move_timer -= self.timeout

        self._move_snake()

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

    def set_drection_up(self) -> None:
        self._set_direction((0, -1))

    def set_drection_down(self) -> None:
        self._set_direction((0, 1))

    def set_drection_right(self) -> None:
        self._set_direction((1, 0))

    def set_drection_left(self) -> None:
        self._set_direction((-1, 0))