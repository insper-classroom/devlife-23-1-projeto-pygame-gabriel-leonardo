import pygame
from constantes import *

class Plataforma1_1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/Plataforma1.1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Plataforma1_2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/Plataforma1.2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Plataforma2_1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/Plataforma2.1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class FlechaEsq(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../assets/inimigo_ranged/FlechaESQ.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.x -= 5
        self.mask = pygame.mask.from_surface(self.image)
        
class FlechaDir(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../assets/inimigo_ranged/Flecha.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.x += 5
        self.mask = pygame.mask.from_surface(self.image)
        