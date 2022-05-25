import pygame


class SoungManager:
    def __init__(self):
        self.sound = {
            'click': pygame.mixer.Sound("assets/sounds/MOI.ogg"),
            'game_over': pygame.mixer.Sound("assets/sounds/Chevre qui cri.ogg"),
            'game_over2' : pygame.mixer.Sound("assets/sounds/Je vous demande de vous arreter.ogg"),
            'tir': pygame.mixer.Sound("assets/sounds/perlimpinpin.ogg"),
        }

    def play(self, name):
        self.sound[name].play()
