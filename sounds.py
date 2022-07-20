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
            "doctor_strange": pygame.mixer.Sound(
                "assets/assets/sounds/.data/'Doctor Strange' Main Theme by Michael Giacchino 128 kbps.mp3/doctor_strange.mp3"
            ),
            "marvel": pygame.mixer.Sound(
                "assets/assets/sounds/.data/Marvel Opening Theme 128 kbps.mp3/Marvel Opening Theme 128 kbps.mp3"
            ),
        }

    def play(self, name):
        "playing sound during the game"
        self.sounds[name].play()
