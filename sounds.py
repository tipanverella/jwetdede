"""
_extended_summary_
"""
import pygame


class SoundManager:
    "Sound manager class"

    def __init__(self) -> None:
        self.sounds = {
            "click": pygame.mixer.Sound(
                "assets/assets/sounds/click.ogg"
            ),
            "game_over": pygame.mixer.Sound(
                "assets/assets/sounds/game_over.ogg"
            ),
            "meteorite": pygame.mixer.Sound(
                "assets/assets/sounds/meteorite.ogg"
            ),
            "tir": pygame.mixer.Sound(
                "assets/assets/sounds/tir.ogg"
            ),           
        }

    def play(self, name):
        "playing sound during the game"
        self.sounds[name].play()
