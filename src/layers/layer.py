from abc import ABC, abstractclassmethod
import pygame

class Layer:
    @abstractclassmethod
    def update(self, dt):
        pass

    @abstractclassmethod
    def render(self):
        pass

    @abstractclassmethod
    def process_event(self, event : pygame.event.Event):
        pass