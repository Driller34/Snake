import pygame
from src.layers.layer import Layer

class LayerManager:
    def __init__(self) -> None:
        self.layers = []
    
    def push_layer(self, layer : Layer) -> None:
        if not isinstance(state, State):
            raise TypeError("State must inherit from State")

        self.layers.append(layer)

    def pop_layer(self) -> Layer:
        return self.layers.pop()

    def top(self) -> Layer:
        if not self.layers:
            raise RuntimeError("Layers stack is empty")

        return self.layers[-1]

    def update(self) -> None:
        self.top().update()

    def render(self) -> None:
        self.top().render()

    def process_event(self, event : pygame.event.Event) -> None:
        self.top().process_event(event)