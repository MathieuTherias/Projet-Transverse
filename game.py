import pygame
from player import Player
from angel import ANGEL
from BOSS import boss
from SOUND import SoungManager

#creer une seconde classe qui va representer le jeu
class Game :

    def __init__(self):
        #Def si le jeu à commencé ou non
        self.is_playing = False
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #definir groupe de monstre
        self.all_ANGEL = pygame.sprite.Group()
        self.all_BOSS = pygame.sprite.Group()
        self.font = pygame.font.Font("assets/Text.ttf", 20)
        #gerer le son
        self.sound_manager = SoungManager()
        self.score = 0
        self.pressed = {}


    def start (self) :
        self.is_playing = True
        self.spawn_BOSS()
        self.spawn_ANGEL()
        self.spawn_ANGEL()

    def game_over(self):
        #reboot le jeu
        self.all_ANGEL = pygame.sprite.Group()
        self.all_BOSS = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')
        self.sound_manager.play('game_over2')

    def update(self, screen):
        #afficher score sur ecran
        score_text = self.font.render(f"Score : {self.score}", 1, (0,0,0))
        screen.blit(score_text, (20, 20))

        # appliquer image
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du j
        self.player.update_health_bar(screen)

        # Recuperer projectile du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Recuperer déplacement monstre
        for angel in self.all_ANGEL:
            angel.forward()
            angel.update_health_bar(screen)

        for boss in self.all_BOSS:
            boss.forward()
            boss.update_health_bar(screen)


        # appliquer l'ensemble des images
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de ange
        self.all_ANGEL.draw(screen)

        #applique ensemble image ange
        self.all_BOSS.draw(screen)

        # verifier si le J souhaite aller D ou G
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_ANGEL(self):
        angel = ANGEL(self)
        self.all_ANGEL.add(angel)

    def spawn_BOSS(self):
        BOSS = boss(self)
        self.all_BOSS.add(BOSS)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
