import pygame
from src.layers.layer import Layer
from src.layers.layer_manager import LayerManager

class GameOverLayer(Layer):
    def __init__(self, layer_manager : LayerManager, config : dict) -> None:
        self.layer_manager = layer_manager
        self.config = config

        x = self.config['window']['width'] / 2 - 150
        y = self.config['window']['height'] / 2 - 100

        self.menu_button = pygame.Rect(x, y, 300, 100)
        self.exit_button = pygame.Rect(x, y + 120, 300, 100)

        self.big_font = pygame.font.Font(None, 70)
        self.small_font = pygame.font.Font(None, 50)
        self.front_text = self.big_font.render("Game Over", True, "red")
        self.menu_button_text = self.small_font.render("Menu", True, "white")
        self.exit_button_text = self.small_font.render("Exit", True, "white")        

    def process_event(self, event : pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.menu_button.collidepoint(event.pos):
                self.layer_manager.pop_layer(2)
            elif self.exit_button.collidepoint(event.pos):
                self.layer_manager.pop_layer(3)

    def update(self, dt : float):
        pass

    def render(self, screen : pygame.Surface) -> None:
        pygame.draw.rect(screen, "gray", self.menu_button)
        pygame.draw.rect(screen, "gray", self.exit_button)

        screen.blit(self.front_text, self.front_text.get_rect(center=(self.config['window']['width'] / 2, self.config['window']['height'] / 2 - 200)))

        screen.blit(self.menu_button_text, self.menu_button_text.get_rect(center=self.menu_button.center))
        screen.blit(self.exit_button_text, self.exit_button_text.get_rect(center=self.exit_button.center))