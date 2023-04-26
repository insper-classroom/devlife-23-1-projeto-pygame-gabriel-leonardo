import pygame
pygame.init()

# Fonte
font_arc ='../assets/fonts/JosefinSans-BoldItalic.ttf'
font_titulo = pygame.font.Font(font_arc, 40)
font_texto = pygame.font.Font(font_arc, 30)
font_texto_popup = pygame.font.Font(font_arc, 35)
# Variáveis
FONTE_TITULO = font_titulo
FONTE_TEXTO = font_texto
FONTE_TEXTO_POPUP = font_texto_popup

# Backgrounds
# Tela inicial e Tela Opções
FUNDO = pygame.image.load('../assets/backgrounds/StartScreen/1.png')
LUA = pygame.image.load('../assets/backgrounds/StartScreen/2.png')
NUVEM_1 = pygame.image.load('../assets/backgrounds/StartScreen/3.png')
NUVEM_1_VEL = 0.5
NUVEM_4 = pygame.image.load('../assets/backgrounds/StartScreen/4.png')
NUVEM_4_VEL = - 0.5

TESTE = pygame.image.load('../assets/backgrounds/TelaJogo/Backgorund_Floresta/map.png')

#TelaJogo


# Sprites
# Player
PLAYER_PARADO = pygame.image.load('../assets/player/parado/Parado.png')
PLAYER_ANDANDO = pygame.image.load('../assets/player/andando/Andando.png')
PLAYER_CORRENDO = pygame.image.load('../assets/player/correndo/Correndo.png')
PLAYER_PULANDO = pygame.image.load('../assets/player/pulando/Pulando.png')
PLAYER_ATAQUE_FRACO = pygame.image.load('../assets/player/ataque_fraco/Ataque_fraco.png')
PLAYER_ATAQUE_FORTE = pygame.image.load('../assets/player/ataque_forte/Ataque_forte.png')
PLAYER_DEFENDENDO = pygame.image.load('../assets/player/defendendo/Defesa.png')
PLAYER_MORRENDO = pygame.image.load('../assets/player/morrendo/Morrendo.png')

# Inimigo meele
INIMIGO_MEELE_PARADO = pygame.image.load('../assets/Inimigo_meele/Parado.png')
INIMIGO_MEELE_CORRENDO = pygame.image.load('../assets/Inimigo_meele/Correndo.png')
INIMIGO_MEELE_ATAQUE_1 = pygame.image.load('../assets/Inimigo_meele/Ataque_1.png')
INIMIGO_MEELE_ATAQUE_2 = pygame.image.load('../assets/Inimigo_meele/Ataque_2.png')
INIMIGO_MEELE_ATAQUE_3 = pygame.image.load('../assets/Inimigo_meele/Ataque_3.png')
INIMIGO_MEELE_MORRENDO = pygame.image.load('../assets/Inimigo_meele/Morrendo.png')
INIMIGO_MEELE_DEFENDENDO = pygame.image.load('../assets/Inimigo_meele/Defendendo.png')

# Inimigo ranged
INIMIGO_RANGED_PARADO = pygame.image.load('../assets/inimigo_ranged/Parado.png')
INIMIGO_RANGED_ATIRANDO = pygame.image.load('../assets/inimigo_ranged/Atirando.png')
INIMIGO_RANGED_MORRENDO = pygame.image.load('../assets/inimigo_ranged/Morrendo.png')
INIMIGO_RANGED_ATAQUE_FRACO = pygame.image.load('../assets/inimigo_ranged/Ataque_fraco.png')
INIMIGO_RANGED_ATAQUE_FORTE = pygame.image.load('../assets/inimigo_ranged/Ataque_forte.png')
INIMIGO_RANGED_FLECHA = pygame.image.load('../assets/inimigo_ranged/Flecha.png')






# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (128, 128, 128)
VERMELHO = (255, 0, 0)
COR_FUNDO = (23, 22, 40)
