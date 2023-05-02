import pygame
from constantes import *

class InimigoMeele(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Variáveis do Inimigo Meele
        # Ações
        self.meele_parado = True
        self.meele_correndo = False
        self.meele_ataque1 = False
        self.meele_ataque2 = False
        self.meele_ataque3 = False
        self.meele_morrendo = False
        self.meele_defendendo = False
        self.meele_dano = False
        self.colisao = False

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
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Correndo
        self.image = self.sprite_correndo[self.index_correndo]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Ataque 1
        self.image = self.sprite_ataque1[self.index_ataque1]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Ataque 2
        self.image = self.sprite_ataque2[self.index_ataque2]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Ataque 3
        self.image = self.sprite_ataque3[self.index_ataque3]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Morrendo
        self.image = self.sprite_morrendo[self.index_morrendo]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Defendendo
        self.image = self.sprite_defendendo[self.index_defendendo]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        # Dano
        self.image = self.sprite_dano[self.index_dano]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        
        # Posição inicial
        self.rect.x = 1030
        self.rect.y = 515
        # Máscara de colisão
        self.mask = pygame.mask.from_surface(self.image)

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
                    self.index_morrendo = 6
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
                        self.kill()
                        
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
 
# Classe do inimigo ranged
class InimigoRanged(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Variáveis do inimigo ranged
        # Ações	
        self.ranged_parado = True
        self.ranged_atirando = False
        self.ranged_morrendo = False
        self.ranged_ataque_fraco = False
        self.ranged_ataque_forte = False
        # Direção
        self.ranged_esquerda = True
        self.ranged_direita = False
        # Status 
        self.ranged_vida = 100

        
        self.sprite_ranged_parado = []
        self.sprite_ranged_atirando = []
        self.sprite_ranged_morrendo = []
        self.sprite_ranged_ataque_fraco = []
        self.sprite_ranged_ataque_forte = []

        for i in range(9):
            img = INIMIGO_RANGED_PARADO.subsurface((85 * i, 0), (85,104))
            self.sprite_ranged_parado.append(img)
        for i in range(14):
            img = INIMIGO_RANGED_ATIRANDO.subsurface((85 * i, 0), (85,104))
            self.sprite_ranged_atirando.append(img)
        for i in range(4):
            img = INIMIGO_RANGED_MORRENDO.subsurface((85 * i, 0), (85,104))
            self.sprite_ranged_morrendo.append(img)
        for i in range(5):
            img = INIMIGO_RANGED_ATAQUE_FRACO.subsurface((85 * i, 0), (85,104))
            self.sprite_ranged_ataque_fraco.append(img)
        for i in range(5):
            img = INIMIGO_RANGED_ATAQUE_FORTE.subsurface((85 * i, 0), (85,104))
            self.sprite_ranged_ataque_forte.append(img)

        self.index_ranged_parado = 0
        self.index_ranged_atirando = 0
        self.index_ranged_morrendo = 0
        self.index_ranged_ataque_fraco = 0
        self.index_ranged_ataque_forte = 0

        self.image = self.sprite_ranged_parado[self.index_ranged_parado]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.image = self.sprite_ranged_atirando[self.index_ranged_atirando]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.image = self.sprite_ranged_morrendo[self.index_ranged_morrendo]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.image = self.sprite_ranged_ataque_fraco[self.index_ranged_ataque_fraco]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.image = self.sprite_ranged_ataque_forte[self.index_ranged_ataque_forte]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        if self.ranged_direita:
            if self.ranged_parado:
                self.index_ranged_parado += 0.08
                if self.index_ranged_parado > 9:
                    self.index_ranged_parado = 0
                self.image = self.sprite_ranged_parado[int(self.index_ranged_parado)]
            if self.ranged_atirando:
                self.index_ranged_atirando += 0.08
                if self.index_ranged_atirando > 14:
                    self.index_ranged_atirando = 0
                self.image = self.sprite_ranged_atirando[int(self.index_ranged_atirando)]
            if self.ranged_morrendo:
                self.index_ranged_morrendo += 0.08
                if self.index_ranged_morrendo > 4:
                    self.index_ranged_morrendo = 0
                self.image = self.sprite_ranged_morrendo[int(self.index_ranged_morrendo)]
            if self.ranged_ataque_fraco:
                self.index_ranged_ataque_fraco += 0.08
                if self.index_ranged_ataque_fraco > 5:
                    self.index_ranged_ataque_fraco = 0
                self.image = self.sprite_ranged_ataque_fraco[int(self.index_ranged_ataque_fraco)]
            if self.ranged_ataque_forte:
                self.index_ranged_ataque_forte += 0.08
                if self.index_ranged_ataque_forte > 5:
                    self.index_ranged_ataque_forte = 0
                self.image = self.sprite_ranged_ataque_forte[int(self.index_ranged_ataque_forte)]
        elif self.ranged_esquerda:
            if self.ranged_parado:
                self.index_ranged_parado += 0.08
                if self.index_ranged_parado > 9:
                    self.index_ranged_parado = 0
                imagem = self.sprite_ranged_parado[int(self.index_ranged_parado)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.ranged_atirando:
                self.index_ranged_atirando += 0.08
                if self.index_ranged_atirando > 14:
                    self.index_ranged_atirando = 0
                imagem = self.sprite_ranged_atirando[int(self.index_ranged_atirando)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.ranged_morrendo:
                self.index_ranged_morrendo += 0.08
                if self.index_ranged_morrendo > 4:
                    self.index_ranged_morrendo = 0
                imagem = self.sprite_ranged_morrendo[int(self.index_ranged_morrendo)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.ranged_ataque_fraco:
                self.index_ranged_ataque_fraco += 0.08
                if self.index_ranged_ataque_fraco > 5:
                    self.index_ranged_ataque_fraco = 0
                imagem = self.sprite_ranged_ataque_fraco[int(self.index_ranged_ataque_fraco)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.ranged_ataque_forte:
                self.index_ranged_ataque_forte += 0.08
                if self.index_ranged_ataque_forte > 5:
                    self.index_ranged_ataque_forte = 0
                imagem = self.sprite_ranged_ataque_forte[int(self.index_ranged_ataque_forte)]
                self.image = pygame.transform.flip(imagem, True, False)