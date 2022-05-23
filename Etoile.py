import pygame
import random

class etoile(pygame.sprite.Sprite):

    def __init__(self, Event):
        super().__init__()
        #def image
        self.image = pygame.image.load('assets/boule-de-feu.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800 )
        self.rect.y = - random.randint(0, 800)
        self.Event = Event

    def remove(self):
        self.Event.all_etoile.remove(self)

    def fall(self):
        self.rect.y += self.velocity

        #ne tombe pas sur le sol
        if self.rect.y >= 500 :
            #retire la boule de feu
            self.remove()

        #verif si l'étoile touche le j
        if self.Event.game.check_collision(
                self, self.Event.game.all_players
        ) :
            print ("joueur touché")
            #suppression de l'étoile
            self.remove()
            #subir 20 degats
            self.Event.game.player.damage(20)
