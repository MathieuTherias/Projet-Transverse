import pygame

#definir la class du projectile du joueur
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 10
        self.player = player
        self.image = pygame.image.load('assets/lance T.png')
        self.image = pygame.transform.scale(self.image, (100 , 100))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 150
        self.rect.y = player.rect.y + 10
        self.origin_image = self.image
        self.angle = 0

    def move(self):
        self.rect.x += self.velocity
        #self.rotate()

        #verifie si projectile supprimer
        if self.rect.x > 1080:
            self.remove()

        #verifie si projectile entre en contact avec ange et boss
        for ANGEL in self.player.game.check_collision(self, self.player.game.all_ANGEL) :
            self.remove()
            ANGEL.damage(self.player.attack)

        for BOSS in self.player.game.check_collision(self, self.player.game.all_BOSS) :
            self.remove()
            BOSS.damage(self.player.attack)

    def remove(self):
        self.player.all_projectiles.remove(self)
