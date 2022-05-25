import pygame
import random

class boss(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 350
        self.max_health = 350
        self.attack = 6
        self.image = pygame.image.load('assets/BOSS T.png')
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 200
        self.velocity = 0.01

    def update_health_bar(self, surface):
        #dessiner la bar de vie
        pygame.draw.rect(surface, (255, 0, 0), [self.rect.x + 15, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 15, self.rect.y - 20, self.health, 5])

    def forward (self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en collision avec J
        else :
            self.game.player.damage(self.attack)

    def damage(self, amount):
        #infliger les degats
        self.health -= amount
        #verifier si son nouveau nombre de pv <= 0
        if self.health <= 0 :
            #reaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(0, 2)
            # ajout du score
            self.game.score += 50
