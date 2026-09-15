from abc import ABC, abstractclassmethod
import pygame

class Layer:
    @abstractclassmethod
    def update(self, dt : float) -> None:
        pass

    @abstractclassmethod
    def render(self, screen : pygame.Surface) -> None:
        pass

    @abstractclassmethod
    def process_event(self, event : pygame.event.Event) -> None:
        pass