import pygame
pygame.init()

# Fonte
font_arc ='assets/fonts\JosefinSans-BoldItalic.ttf'
font_titulo = pygame.font.Font(font_arc, 40)
font_texto = pygame.font.Font(font_arc, 30)
font_texto_popup = pygame.font.Font(font_arc, 35)
# Variáveis
FONTE_TITULO = font_titulo
FONTE_TEXTO = font_texto
FONTE_TEXTO_POPUP = font_texto_popup

# Backgrounds
# Tela inicial e Tela Opções
FUNDO = pygame.image.load('assets/backgrounds\StartScreen/1.png')
LUA = pygame.image.load('assets/backgrounds\StartScreen/2.png')
NUVEM_1 = pygame.image.load('assets/backgrounds\StartScreen/3.png')
NUVEM_1_VEL = 0.5
NUVEM_4 = pygame.image.load('assets/backgrounds\StartScreen/4.png')
NUVEM_4_VEL = - 0.5

#TelaJogo
CHAO = pygame.image.load('assets/backgrounds\TelaJogo\CHAO TESTE.png')
FUNDO_INICIO = pygame.image.load('assets/backgrounds\TelaJogo\Background DE FATO.png')


# Sprites
# Player
PLAYER_ANDANDO = pygame.image.load('assets\player/andando\Walk.png')
PLAYER_ATAQUE_FORTE = pygame.image.load('assets\player/atacando 1\Attack_2.png')
PLAYER_ATAQUE_FRACO = pygame.image.load('assets\player/atacando 2\Attack_3.png')
PLAYER_CORRENDO = pygame.image.load('assets\player\correndo\Run.png')
PLAYER_DEFENDENDO = pygame.image.load('assets\player\defendendo\Protection.png')
PLAYER_MORRENDO = pygame.image.load('assets\player\morrendo\Dead.png')
PLAYER_PARADO = pygame.image.load('assets\player\parado\Idle.png')
PLAYER_PULANDO = pygame.image.load('assets\player\pulando\Jump.png')





# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (128, 128, 128)
VERMELHO = (255, 0, 0)
COR_FUNDO = (23, 22, 40)
