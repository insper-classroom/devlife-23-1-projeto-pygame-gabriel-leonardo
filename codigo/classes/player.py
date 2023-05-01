import pygame
from constantes import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Variáveis do player
        # Status
        self.vivo = True
        self.max_vida = 5
        self.vida = 5
        self.stamina = 10
        self.max_atq_forte = 0
        self.max_atq_fraco = 0
        self.max_ataques = 1
        self.pulos = 0
        self.max_pulos = 1
        self.cima_plataforma = False
        # Ações
        self.parado = True
        self.andando = False
        self.defendendo = False
        self.pulando = False
        self.correndo = False
        self.ataque_forte = False
        self.ataque_fraco = False
        # Direção
        self.esquerda = False
        self.direita = True
        # Velociades
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.gravidade = 0
        # Outros
        self.last_updated = 0

        # Animação das Sprites
        # Definindo as listas de sprites
        self.sprite_parado = []
        self.sprite_andando = []
        self.sprite_correndo = []
        self.sprite_ataque_forte = []
        self.sprite_ataque_fraco = []
        self.sprite_pulando = []
        self.sprite_defendendo = []

        # Cada sprite em sua respectiva lista
        for i in range(6):
            img = PLAYER_PARADO.subsurface((85 * i, 0), (85,104))
            self.sprite_parado.append(img)
        for i in range(9):
            img = PLAYER_ANDANDO.subsurface((85 * i, 0), (85,104))
            self.sprite_andando.append(img)
        for i in range(8):
            img = PLAYER_CORRENDO.subsurface((85 * i, 0), (85,104))
            self.sprite_correndo.append(img)
        for i in range(8):
            img = PLAYER_ATAQUE_FORTE.subsurface((85 * i, 0), (85,104))
            self.sprite_ataque_forte.append(img)
        for i in range(4):
            img = PLAYER_ATAQUE_FRACO.subsurface((85 * i, 0), (85,104))
            self.sprite_ataque_fraco.append(img)
        for i in range(2,7): 
            img = PLAYER_PULANDO.subsurface((85 * i, 0), (85,104))
            self.sprite_pulando.append(img)
        for i in range(2):
            img = PLAYER_DEFENDENDO.subsurface((85 * i, 0), (85,104))
            self.sprite_defendendo.append(img)
        
        # Index das sprites
        self.index_parado = 0
        self.index_andando = 0
        self.index_correndo = 0
        self.index_ataque_forte = 0
        self.index_ataque_fraco = 0
        self.index_pulando = 0
        self.index_defendendo = 0

        # Parado:
        self.image = self.sprite_parado[self.index_parado]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Andando:
        self.image = self.sprite_andando[self.index_andando]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Correndo:
        self.image = self.sprite_correndo[self.index_correndo]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Ataque forte:
        self.image = self.sprite_ataque_forte[self.index_ataque_forte]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Ataque fraco:
        self.image = self.sprite_ataque_fraco[self.index_ataque_fraco]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Pulando:
        self.image = self.sprite_pulando[self.index_pulando]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Defendendo:
        self.image = self.sprite_defendendo[self.index_defendendo]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Posição inicial
        self.rect.x = 512
        self.rect.y = 535
        # Máscara de colisão:
        self.mask = pygame.mask.from_surface(self.image)

    
    # Função que atualiza a animação do player:
    def update(self):
        # Para a direita:
        if self.direita:
            # Parado
            if self.parado:
                self.index_parado += 0.05
                if self.index_parado > 6:
                    self.index_parado = 0
                self.image = self.sprite_parado[int(self.index_parado)]

            # Andando
            if self.andando:
                self.index_andando += 0.06
                if self.index_andando > 9:
                    self.index_andando = 0
                self.image = self.sprite_andando[int(self.index_andando)]

            # Correndo
            if self.correndo:
                self.index_correndo += 0.1
                if self.index_correndo > 8:
                    self.index_correndo = 0
                self.image = self.sprite_correndo[int(self.index_correndo)]

            # Ataque forte
            if self.ataque_forte:
                self.index_ataque_forte += 0.09
                if self.index_ataque_forte > 8:
                    self.index_ataque_forte = 0
                    self.max_atq_forte = 0
                    self.ataque_forte = False
                    self.parado = True
                self.image = self.sprite_ataque_forte[int(self.index_ataque_forte)]

            # Ataque fraco
            if self.ataque_fraco:
                self.index_ataque_fraco += 0.08
                if self.index_ataque_fraco > 4:
                    self.index_ataque_fraco = 0
                    self.max_atq_fraco = 0
                    self.ataque_fraco = False
                    self.parado = True
                self.image = self.sprite_ataque_fraco[int(self.index_ataque_fraco)]

            # Pulando
            if self.pulando:
                self.index_pulando += 0.07
                if self.index_pulando > len(self.sprite_pulando):
                    self.index_pulando = 0
                self.image = self.sprite_pulando[int(self.index_pulando)]

            # Defendendo
            if self.defendendo:
                self.index_defendendo += 0.05
                if self.index_defendendo > 1:
                    self.index_defendendo = 0
                    self.defendendo = False
                    self.parado = True
                self.image = self.sprite_defendendo[int(self.index_defendendo)]
        
        # Para a esquerda:
        elif self.esquerda:
            # Parado
            if self.parado:
                self.index_parado += 0.05
                if self.index_parado > 6:
                    self.index_parado = 0
                imagem = self.sprite_parado[int(self.index_parado)]
                self.image = pygame.transform.flip(imagem, True, False)

            # Andando
            if self.andando:
                self.index_andando += 0.06
                if self.index_andando > 9:
                    self.index_andando = 0
                imagem = self.sprite_andando[int(self.index_andando)]
                self.image = pygame.transform.flip(imagem, True, False)

            # Correndo
            if self.correndo:
                self.index_correndo += 0.1
                if self.index_correndo > 8:
                    self.index_correndo = 0
                imagem = self.sprite_correndo[int(self.index_correndo)]
                self.image = pygame.transform.flip(imagem, True, False)

            # Ataque forte
            if self.ataque_forte:
                self.index_ataque_forte += 0.09
                if self.index_ataque_forte > 8:
                    self.index_ataque_forte = 0
                    self.ataque_forte = False
                    self.parado = True
                imagem = self.sprite_ataque_forte[int(self.index_ataque_forte)]
                self.image = pygame.transform.flip(imagem, True, False)

            # Ataque fraco
            if self.ataque_fraco:
                self.index_ataque_fraco += 0.08
                if self.index_ataque_fraco > 4:
                    self.index_ataque_fraco = 0
                    self.ataque_fraco = False
                    self.parado = True
                imagem = self.sprite_ataque_fraco[int(self.index_ataque_fraco)]
                self.image = pygame.transform.flip(imagem, True, False)

            # Pulando
            if self.pulando:
                self.index_pulando += 0.07
                if self.index_pulando > len(self.sprite_pulando):
                    self.index_pulando = 0
                imagem = self.sprite_pulando[int(self.index_pulando)]
                self.image = pygame.transform.flip(imagem, True, False)

            # Defendendo
            if self.defendendo:
                self.index_defendendo += 0.05
                if self.index_defendendo > 1:
                    self.index_defendendo = 0
                    self.defendendo = False
                    self.parado = True
                imagem = self.sprite_defendendo[int(self.index_defendendo)]
                self.image = pygame.transform.flip(imagem, True, False)

    # Função que verifica a movimentaçãoo do player
    def movimenta_player(self):
        self.gravidade += 0.3
        self.rect.y += self.gravidade
        prox_posicao_x = self.rect.x + self.velocidade_x

        # Verifica as bordas
        if prox_posicao_x < 0:
            prox_posicao_x = 0
            if self.rect.y < 535:
                self.rect.y = self.rect.y
            else:
                self.rect.y = 535
                self.index_pulando = 0

        elif self.rect.y > 535 and self.cima_plataforma == False:
            self.rect.y = 535
            self.pulos = 0
            self.pulando = False
            self.parado = True
            self.index_pulando = 0

        # Atualiza
        self.rect.x = prox_posicao_x
        self.velocidade_x = self.velocidade_x