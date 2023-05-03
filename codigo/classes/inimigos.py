import pygame
from constantes import *

class InimigoMeele(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.min = min
        self.max = max
        # Variáveis do Inimigo Meele
        # Ações
        self.meele_combate = False
        self.meele_parado = False
        self.meele_correndo = True
        self.meele_ataque1 = False
        self.meele_ataque2 = False
        self.meele_ataque3 = False
        self.meele_morrendo = False
        self.meele_defendendo = False
        self.meele_dano = False
        self.colisao = False
        self.dano = 0

        # Direção
        self.meele_esquerda = True
        self.meele_direita = False
        # Status
        self.vida = 5
        # Velocidade
        self.velocidade_x = 0
        # Outros
        self.last_update = 0

        # Animação das Sprites
        # Definindo as listas de sprites
        self.sprite_parado = []
        self.sprite_correndo = []
        self.sprite_ataque1 = []
        self.sprite_ataque2 = []
        self.sprite_ataque3 = []
        self.sprite_morrendo = []
        self.sprite_defendendo = []
        self.sprite_dano = []

        # Cada sprite em sua respectiva lista
        for i in range(5):
            img = INIMIGO_MEELE_PARADO.subsurface((128 * i, 0), (128,128))
            self.sprite_parado.append(img)
        for i in range(8):
            img = INIMIGO_MEELE_CORRENDO.subsurface((128 * i, 0), (128,128))
            self.sprite_correndo.append(img)
        for i in range(4):
            img = INIMIGO_MEELE_ATAQUE_1.subsurface((128 * i, 0), (128,128))
            self.sprite_ataque1.append(img)
        for i in range(5):
            img = INIMIGO_MEELE_ATAQUE_2.subsurface((128 * i, 0), (128,128))
            self.sprite_ataque2.append(img)
        for i in range(4):
            img = INIMIGO_MEELE_ATAQUE_3.subsurface((128 * i, 0), (128,128))
            self.sprite_ataque3.append(img)
        for i in range(6):
            img = INIMIGO_MEELE_MORRENDO.subsurface((128 * i, 0), (128,128))
            self.sprite_morrendo.append(img)
        for i in range(2):
            img = INIMIGO_MEELE_DEFENDENDO.subsurface((128 * i, 0), (128,128))
            self.sprite_defendendo.append(img)
        for i in range(2):
            img = INIMIGO_MEELE_DANO.subsurface((128 * i, 0), (128,128))
            self.sprite_dano.append(img)

        # Index das sprites
        self.index_parado = 0
        self.index_correndo = 0
        self.index_ataque1 = 0
        self.index_ataque2 = 0
        self.index_ataque3 = 0
        self.index_morrendo = 0
        self.index_defendendo = 0
        self.index_dano = 0

        # Parado
        self.image = self.sprite_parado[self.index_parado]

        # Correndo
        self.image = self.sprite_correndo[self.index_correndo]

        # Ataque 1
        self.image = self.sprite_ataque1[self.index_ataque1]

        # Ataque 2
        self.image = self.sprite_ataque2[self.index_ataque2]

        # Ataque 3
        self.image = self.sprite_ataque3[self.index_ataque3]

        # Morrendo
        self.image = self.sprite_morrendo[self.index_morrendo]

        # Defendendo
        self.image = self.sprite_defendendo[self.index_defendendo]

        # Dano
        self.image = self.sprite_dano[self.index_dano]

        # Pega as imagens
        self.image = self.image.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        # Posiciona o inimigo
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # Função para atualizar a animação
    def update(self):
        # Para a direita
        if self.meele_direita:
            # Parado
            if self.meele_parado:
                self.index_parado += 0.08
                if self.index_parado > 5:
                    self.index_parado = 0
                self.image = self.sprite_parado[int(self.index_parado)]
            # Correndo
            if self.meele_correndo:
                self.index_correndo += 0.08
                if self.index_correndo > 8:
                    self.index_correndo = 0
                self.image = self.sprite_correndo[int(self.index_correndo)]
            # Ataque 1
            if self.meele_ataque1:
                self.index_ataque1 += 0.08
                if self.index_ataque1 > 4:
                    self.index_ataque1 = 0
                    if self.colisao == True:
                        self.meele_ataque2 = True
                        self.meele_ataque1 = False
                self.image = self.sprite_ataque1[int(self.index_ataque1)]
            # Ataque 2
            elif self.meele_ataque2:
                self.index_ataque2 += 0.08
                if self.index_ataque2 > 5:
                    self.index_ataque2 = 0
                    self.meele_ataque3 = True
                    self.meele_ataque2 = False
                self.image = self.sprite_ataque2[int(self.index_ataque2)]
            # Ataque 3
            elif self.meele_ataque3:
                self.index_ataque3 += 0.08
                if self.index_ataque3 > 4:
                    self.index_ataque3 = 0
                self.image = self.sprite_ataque3[int(self.index_ataque3)]
            # Morrendo
            if self.meele_morrendo:
                self.index_morrendo += 0.05
                if self.index_morrendo > 6:
                    self.index_morrendo = 0
                    self.meele_morrendo = False
                self.image = self.sprite_morrendo[int(self.index_morrendo)]
            # Defendendo
            if self.meele_defendendo:
                self.index_defendendo += 0.08
                if self.index_defendendo > 2:
                    self.index_defendendo = 0
                self.image = self.sprite_defendendo[int(self.index_defendendo)]
            # Dano
            if self.meele_dano:
                self.index_dano += 0.08
                if self.index_dano > 1:
                    self.index_dano = 0
                self.image = self.sprite_dano[int(self.index_dano)]

        # Para a esquerda
        elif self.meele_esquerda:
            # Parado
            if self.meele_parado:
                self.index_parado += 0.08
                if self.index_parado > 5:
                    self.index_parado = 0
                imagem = self.sprite_parado[int(self.index_parado)]
                self.image = pygame.transform.flip(imagem, True, False)
            # Correndo
            if self.meele_correndo:
                self.index_correndo += 0.08
                if self.index_correndo > 8:
                    self.index_correndo = 0
                imagem = self.sprite_correndo[int(self.index_correndo)]
                self.image = pygame.transform.flip(imagem, True, False)
            # Ataque 1
            if self.meele_ataque1:
                self.index_ataque1 += 0.08
                if self.index_ataque1 > 4:
                    self.index_ataque1 = 0
                    if self.colisao == True:
                        self.meele_ataque3 = True
                        self.meele_ataque1 = False
                imagem = self.sprite_ataque1[int(self.index_ataque1)]
                self.image = pygame.transform.flip(imagem, True, False)
            # Ataque 2
            elif self.meele_ataque2:
                self.index_ataque2 += 0.08
                if self.index_ataque2 > 5:
                    self.index_ataque2 = 0
                    self.meele_ataque2 = False
                imagem = self.sprite_ataque2[int(self.index_ataque2)]
                self.image = pygame.transform.flip(imagem, True, False)
            # Ataque 3
            elif self.meele_ataque3:
                self.index_ataque3 += 0.08
                if self.index_ataque3 > 4:
                    self.index_ataque3 = 0
                    self.meele_ataque2 = True
                    self.meele_ataque3 = False
                imagem = self.sprite_ataque3[int(self.index_ataque3)]
                self.image = pygame.transform.flip(imagem, True, False)
            # Morrendo
            if self.meele_morrendo:
                self.index_morrendo += 0.08
                if self.index_morrendo > 6:
                    self.index_morrendo = 0
                    self.meele_morrendo = False
                    if self.meele_morrendo == False:
                        self.rect.y += 500
                imagem = self.sprite_morrendo[int(self.index_morrendo)]
                self.image = pygame.transform.flip(imagem, True, False)
            # Defendendo
            if self.meele_defendendo:
                self.index_defendendo += 0.08
                if self.index_defendendo > 2:
                    self.index_defendendo = 0
                imagem = self.sprite_defendendo[int(self.index_defendendo)]
                self.image = pygame.transform.flip(imagem, True, False)
            # Dano
            if self.meele_dano:
                self.index_dano += 0.08
                if self.index_dano > 1:
                    self.index_dano = 0
                imagem = self.sprite_dano[int(self.index_dano)]
                self.image = pygame.transform.flip(imagem, True, False)
        self.mask = pygame.mask.from_surface(self.image)