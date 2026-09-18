from abc import ABC, abstractmethod
import pygame

class Layer:
    @abstractmethod
    def update(self, dt : float) -> None:
        pass

    @abstractmethod
    def render(self, screen : pygame.Surface) -> None:
        pass

    @abstractmethod
    def process_event(self, event : pygame.event.Event) -> None:
        pass