import pygame
from player import Player
from monster import Monster
from Event import FallEvent

#creer une seconde classe qui va representer le jeu
class Game :

    def __init__(self):
        #Def si le jeu à commencé ou non
        self.is_playing = True
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #generer l'event
        self.event = FallEvent(self)
        #definir groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}


    def start (self) :
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        #reboot le jeu
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = True

    def update(self, screen):
        # appliquer image
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du j
        self.player.update_health_bar(screen)

        #actualise la barre event du jeu
        self.event.update_bar(screen)

        # Recuperer projectile du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Recuperer déplacement monstre
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # recup etoiles
        for Etoile in self.event.all_etoile:
            Etoile.fall()

        # appliquer l'ensemble des images
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de monstre
        self.all_monsters.draw(screen)

        # appliquer ensemble images d'etoile
        self.event.all_etoile.draw(screen)

        # verifier si le J souhaite aller D ou G
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
