import pygame
from constantes import *

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/Plataforma.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rects = []
        self.rects.append(self.rect)