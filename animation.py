"""
    _summary_

    _extended_summary_
"""
import pygame


class AnimateSprite(pygame.sprite.Sprite):
    "definir une classe qui va s'occuper des animations"

    # initialisser la classe
    def __init__(self, sprite_name, size=(200, 200)):
        "initialiser la classe"
        super().__init__()
        self.image = pygame.image.load(
            f"assets/assets/{sprite_name}.png"
        )
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # definir une methode pour demarer l'animation
    def start_animation(self):
        "method to start animation of the objects"
        self.animation = True

    # definir une methode pour animer le sprite
    def animate(self, loop=False):
        "animation method"

        # verifier si l'animation est active
        if loop or self.animation:
            self.current_image += 1
            # verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au depart
                self.current_image = 0
                # desactiver l'animation

                # verifier si l'animation n'est pas en mode loop
                if loop is False:
                    self.animation = False

            # modifier l'image precedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    "function to load all the images of a sprite"
    # charger les images de ce sprie dans le dossier correspondant
    images = []
    # recuperer le chemin du dossier pour se sprite
    path = f"assets/assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque image du dossier
    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    return images


# definir un dictionnaire qui va contenir les images chargee de chaque classe

animations = {
    "mummy": load_animation_images("mummy"),
    "player": load_animation_images("player"),
    "alien": load_animation_images("alien"),
}
