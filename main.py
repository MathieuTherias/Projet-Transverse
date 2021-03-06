import pygame
import math
from game import Game
pygame.init()

#def d'une clock
clock = pygame.time.Clock()
FPS = 40


pygame.display.set_caption("A.O.G")
screen = pygame.display.set_mode((1080,720))

#importation de l'arriere plan
background = pygame.image.load('assets/Decore.jpg')
background = pygame.transform.scale(background, (1080, 720))


#charger la baniere
banner = pygame.image.load('assets/ASCENSION T.png')
banner = pygame.transform.scale(banner, (700, 700))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4.888)
banner_rect.y = math.ceil(screen.get_height()/15)

#importer ou charger un bouton pour lancer la partie
play_button = pygame.image.load('assets/JOUER T.png')
play_button = pygame.transform.scale(play_button, (1000, 1100))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/15)
play_button_rect.y = math.ceil(screen.get_height() / 25)

#charger le jeu
game = Game()

running = True

while running :

    #appliquer la fenetre du jeu
    screen.blit(background, (0, 0))

    #verifier si notre jeu à commencé ou non
    if game.is_playing:
        #déclencher les instructions de la partie
        game.update(screen)
    #verifier si le jeu n'a pas commencé
    else:
        #ajout d'écran de bvn
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    #met à jour l'écran
    pygame.display.flip()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True

            #detection de la touche espace
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN :
            #verification de la souris avec le play_button
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancer
                game.start()
                #son
                game.sound_manager.play('click')
    clock.tick(FPS)
