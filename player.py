import pygame
from projectile import Projectile

#Creation de Classe qui va représenter le Joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 7
        self.velocity = 3.5
        self.image = pygame.image.load('assets/hero.png')
        #self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300
        self.all_projectiles = pygame.sprite.Group()

    def move_right(self):
        # si le joueur n'est pas en collision avec les monstres
        if not self.game.check_collision(self, self.game.all_ANGEL) or self.game.check_collision(self, self.game.all_BOSS):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def launch_projectile(self):
        #creation d'une nouvelle instance de le class projectile
        self.all_projectiles.add(Projectile(self))
        self.game.sound_manager.play('tir')

    def update_health_bar(self, surface):
        #dessiner la bar de vie
        pygame.draw.rect(surface, (255, 0, 0), [self.rect.x + 50, self.rect.y + 5 , self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 5, self.health, 5])

    def damage (self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur n'a plus de pv
            self.game.game_over()
