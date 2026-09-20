import pygame

class Button:
    def __init__(self, font : pygame.Font, content : str, color : str,
                bg_color : str, rect : pygame.Rect, callback) -> None:
        self.font = font
        self.content = content
        self.color = color
        self.bg_color = bg_color
        self.rect = rect
        self.callback = callback

        self.text = self.text = self.font.render(self.content, True, self.color)

    def process_event(self, event : pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

    def render(self, screen : pygame.Surface) -> None:
        pygame.draw.rect(screen, self.bg_color, self.rect)
        screen.blit(self.text, self.text.get_rect(center=self.rect.center))
