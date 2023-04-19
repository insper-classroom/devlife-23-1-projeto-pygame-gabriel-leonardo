import pygame
pygame.init()

# Fontes 
font_arc ='assets/fonts\Akira Expanded Demo.otf'
font_titulo = pygame.font.Font(font_arc, 30)
font_texto = pygame.font.Font(font_arc, 20)
font_texto_popup = pygame.font.Font(font_arc, 25)
FONTE_TITULO = font_titulo
FONTE_TEXTO = font_texto
FONTE_TEXTO_POPUP = font_texto_popup

# Backgrounds
FUNDO = pygame.image.load('assets/backgrounds\Clouds 3/1.png')
LUA = pygame.image.load('assets/backgrounds\Clouds 3/2.png')
NUVEM_1 = pygame.image.load('assets/backgrounds\Clouds 3/3.png')
NUVEM_4 = pygame.image.load('assets/backgrounds\Clouds 3/4.png')

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (128, 128, 128)
VERMELHO = (255, 0, 0)
COR_FUNDO = (23, 22, 40)
