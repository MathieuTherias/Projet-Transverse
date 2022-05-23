import pygame
from math import cos, tan, sin, pi

#definir la class du projectile du joueur
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50 , 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 100
        self.origin_image = self.image
        self.angle = 0

    def compteur(self):
        for i in [0, 0.2 , 0.4, 0.6, 0.8] :
            sin(i)

    def move(self):
        self.rect.x += self.velocity
        self.angle += 3
        #self.rect.y += pygame.transform.rotozoom(self.rect, self.angle, 1)
        self.rotate()

        #verifie si projectile supprimer
        if self.rect.x > 1080:
            self.remove()

        #verifie si projectile entre en contact avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)