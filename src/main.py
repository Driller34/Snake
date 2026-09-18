import pygame
import json
from pathlib import Path
from src.game import Game

pygame.init()
pygame.font.init()

def main():
    base_dir = Path(__file__).resolve().parent.parent
    config_path = base_dir / "src" / "config.json"

    with open(config_path, 'r') as file:
        config = json.load(file)

    game = Game(config)
    game.run()

if __name__ == "__main__":
    main()