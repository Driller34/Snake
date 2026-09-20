import pygame

class Label:
    def __init__(self, font : pygame.Font, content : str, color : str, position : tuple[int, int]) -> None:
        self.font = font
        self.content = content
        self.color = color
        self.position = position

        self.text = self.font.render(self.content, True, self.color)

    def render(self, screen : pygame.Surface) -> None:
        screen.blit(self.text, self.text.get_rect(center=self.position))