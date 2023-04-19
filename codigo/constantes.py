import pygame
pygame.init()

# Fontes 
font_arc ='assets/fonts\JosefinSans-BoldItalic.ttf'
font_titulo = pygame.font.Font(font_arc, 40)
font_texto = pygame.font.Font(font_arc, 30)
font_texto_popup = pygame.font.Font(font_arc, 35)
FONTE_TITULO = font_titulo
FONTE_TEXTO = font_texto
FONTE_TEXTO_POPUP = font_texto_popup

# Backgrounds
FUNDO = pygame.image.load('assets/backgrounds\StartScreen/1.png')
LUA = pygame.image.load('assets/backgrounds\StartScreen/2.png')
NUVEM_1 = pygame.image.load('assets/backgrounds\StartScreen/3.png')
NUVEM_1_VEL = 0.5
NUVEM_4 = pygame.image.load('assets/backgrounds\StartScreen/4.png')
NUVEM_4_VEL = - 0.5

FUNDO_INICIO = pygame.image.load('assets/backgrounds\TelaJogo\Background DE FATO.png')

#
# Sprites
# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (128, 128, 128)
VERMELHO = (255, 0, 0)
COR_FUNDO = (23, 22, 40)
