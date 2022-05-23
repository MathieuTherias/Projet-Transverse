import pygame
from Etoile import etoile

#creation de classe
class FallEvent :

    #dans chargement -> creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 22
        self.game = game

        #def de sprite pour les etoiles
        self.all_etoile = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def etoile_fall(self):
        self.all_etoile.add(etoile(self))

    def attempt_fall(self):
        if self.is_full_loaded():
            print("Pluie de projectile !")
            self.etoile_fall()
            self.reset_percent()


    def update_bar(self, surface):

        #ajout de pourcentage
        self.add_percent()

        self.attempt_fall()

        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 20,
            1000,
            10
        ])

        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 20,
            (1000 / 100) * self.percent,
            10 ])
