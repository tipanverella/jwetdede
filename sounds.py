"""
_extended_summary_
"""
import pygame


class SoundManager:
    "Sound manager class"

    def __init__(self) -> None:
        self.sounds = {
            "click": pygame.mixer.Sound(
<<<<<<< HEAD
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
=======
                "C:/Users/dedea/Dropbox/PC/Downloads/My works/my python games(try)/assets/assets/sounds/click.ogg"
            ),
            "game_over": pygame.mixer.Sound(
                "C:/Users/dedea/Dropbox/PC/Downloads/My works/my python games(try)/assets/assets/sounds/game_over.ogg"
            ),
            "meteorite": pygame.mixer.Sound(
                "C:/Users/dedea/Dropbox/PC/Downloads/My works/my python games(try)/assets/assets/sounds/meteorite.ogg"
            ),
            "tir": pygame.mixer.Sound(
                "C:/Users/dedea/Dropbox/PC/Downloads/My works/my python games(try)/assets/assets/sounds/tir.ogg"
            ),
            "doctor_strange": pygame.mixer.Sound(
                "C:/Users/dedea/Dropbox/PC/Downloads/My works/my python games(try)/assets/assets/sounds/.data/'Doctor Strange' Main Theme by Michael Giacchino 128 kbps.mp3/doctor_strange.mp3"
            ),
            "marvel": pygame.mixer.Sound(
                "C:/Users/dedea/Dropbox/PC/Downloads/My works/my python games(try)/assets/assets/sounds/.data/Marvel Opening Theme 128 kbps.mp3/Marvel Opening Theme 128 kbps.mp3"
>>>>>>> e8b06d02043617852b91b517f90d293595c53d37
            ),
        }

    def play(self, name):
        "playing sound during the game"
        self.sounds[name].play()
