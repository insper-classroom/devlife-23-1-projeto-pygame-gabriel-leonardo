import pygame
from constantes import *

class Jogo:
    def __init__(self):
        # Inicialização do jogo:
        # Tamaho da tela
        self.WIDTH = 1024
        self.HEIGHT =  720
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # Velocidade das nuvens da tela inicial
        self.nuvem1_vel = NUVEM_1_VEL
        self.nuvem4_vel = NUVEM_4_VEL
        self.nuv_dir = 0
        # Variável que controla a tela do jogo
        self.scroll = 0
        # Variáveis de controle
        self.botao = 0
        # Variáveis das opções
        self.musica = True
        self.sons = True
        self.show_fps = False
        # Outros
        self.t0 = -1
        self.deltat = (pygame.time.get_ticks() - self.t0) / 1000

    # Update na tela(não precisa ficar chamando a funcao pygame.display.update):
    def roda(self):
        self.desenha()
        pygame.display.update()
