import pygame
import json
from src.game import Game

pygame.init()
pygame.font.init()

def main():
    with open('src/config.json', 'r') as file:
        config = json.load(file)

    game = Game(config)
    game.run()