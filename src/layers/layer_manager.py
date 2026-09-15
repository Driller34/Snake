import pygame
from src.layers.layer import Layer

class LayerManager:
    def __init__(self) -> None:
        self.layers = []
    
    def push_layer(self, layer : Layer) -> None:
        if not isinstance(layer, Layer):
            raise TypeError("State must inherit from State")

        self.layers.append(layer)

    def pop_layer(self, n: int = 1) -> Layer:
        if not self.layers:
            raise RuntimeError("Layers stack is empty")

        n = min(n, len(self.layers))

        for _ in range(n):
            layer = self.layers.pop()

        return layer

    def top(self) -> Layer:
        if not self.layers:
            raise RuntimeError("Layers stack is empty")

        return self.layers[-1]

    def __len__(self):
        return len(self.layers)

    def update(self, dt : float) -> None:
        self.top().update(dt)

    def render(self, screen : pygame.Surface) -> None:
        self.top().render(screen)

    def process_event(self, event : pygame.event.Event) -> None:
        self.top().process_event(event)