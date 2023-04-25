import pygame
from constantes import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Variáveis de estado:
        self.parado = True
        self.andando = False
        self.pulando = False
        self.correndo = False
        self.esquerda = False
        self.direita = True
        self.ataque_forte = False
        self.ataque_fraco = False

        ## INICIALIZAÇÃO DE IMAGENS (ANIMAÇÃO):

        # Adicionando as imagens em listas (uma lista para cada tipo de animação. Ex.: parado, andando, pulando, etc.):
        self.sprite_parado = []
        self.sprite_andando = []
        self.sprite_correndo = []
        self.sprite_ataque_forte = []
        self.sprite_ataque_fraco = []
        self.sprite_pulando = []

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
        
        # Indexes:
        self.index_parado = 0
        self.index_andando = 0
        self.index_correndo = 0
        self.index_ataque_forte = 0
        self.index_ataque_fraco = 0
        self.index_pulando = 0

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

        # Movimentação:
        self.rect.x = 512
        self.rect.y = 535
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.gravidade = 0
        self.last_updated = 0
        self.pulos = 0
        self.max_pulos = 1
    
    def update(self):
        # Função que atualiza a animação do player:
        # Para a direita:
        if self.direita:
            if self.parado:
                self.index_parado += 0.05
                if self.index_parado > 6:
                    self.index_parado = 0
                self.image = self.sprite_parado[int(self.index_parado)]
            if self.andando:
                self.index_andando += 0.06
                if self.index_andando > 9:
                    self.index_andando = 0
                self.image = self.sprite_andando[int(self.index_andando)]
            if self.correndo:
                self.index_correndo += 0.1
                if self.index_correndo > 8:
                    self.index_correndo = 0
                self.image = self.sprite_correndo[int(self.index_correndo)]
            if self.ataque_forte:
                self.index_ataque_forte += 0.09
                if self.index_ataque_forte > 8:
                    self.index_ataque_forte = 0
                    self.ataque_forte = False
                    self.parado = True
                self.image = self.sprite_ataque_forte[int(self.index_ataque_forte)]
            if self.ataque_fraco:
                self.index_ataque_fraco += 0.07
                if self.index_ataque_fraco > 4:
                    self.index_ataque_fraco = 0
                    self.ataque_fraco = False
                    self.parado = True
                self.image = self.sprite_ataque_fraco[int(self.index_ataque_fraco)]
            if self.pulando:
                self.index_pulando += 0.07
                self.image = self.sprite_pulando[int(self.index_pulando)]
        
        # Para a esquerda:
        elif self.esquerda:
            if self.parado:
                self.index_parado += 0.05
                if self.index_parado > 6:
                    self.index_parado = 0
                imagem = self.sprite_parado[int(self.index_parado)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.andando:
                self.index_andando += 0.06
                if self.index_andando > 9:
                    self.index_andando = 0
                imagem = self.sprite_andando[int(self.index_andando)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.correndo:
                self.index_correndo += 0.1
                if self.index_correndo > 8:
                    self.index_correndo = 0
                imagem = self.sprite_correndo[int(self.index_correndo)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.ataque_forte:
                self.index_ataque_forte += 0.09
                if self.index_ataque_forte > 5:
                    self.index_ataque_forte = 0
                    self.ataque_forte = False
                    self.parado = True
                imagem = self.sprite_ataque_forte[int(self.index_ataque_forte)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.ataque_fraco:
                self.index_ataque_fraco += 0.08
                if self.index_ataque_fraco > 4:
                    self.index_ataque_fraco = 0
                    self.ataque_fraco = False
                    self.parado = True
                imagem = self.sprite_ataque_fraco[int(self.index_ataque_fraco)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.pulando:
                self.index_pulando += 0.07
                imagem = self.sprite_pulando[int(self.index_pulando)]
                self.image = pygame.transform.flip(imagem, True, False)

    def movimenta_player(self):
        self.gravidade += 0.3
        self.rect.y += self.gravidade
        prox_posicao_x = self.rect.x + self.velocidade_x

        # Verifica borda:
        if prox_posicao_x < 0:
            prox_posicao_x = 0
            if self.rect.y < 535:
                self.rect.y = self.rect.y
            else:
                self.rect.y = 535
        elif prox_posicao_x > 896:
            prox_posicao_x = 896
            if self.rect.y < 535:
                self.rect.y = self.rect.y
            else:
                self.rect.y = 535
        elif self.rect.y > 535:
            self.rect.y = 535
            self.pulos = 0
            self.pulando = False
            self.parado = True
            self.index_pulando = 0
        
        # Atualiza
        self.rect.x = prox_posicao_x
        self.velocidade_x = self.velocidade_x      

class InimigoMeele(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.meele_parado = False
        self.meele_correndo = False
        self.meele_ataque1 = False
        self.meele_ataque2 = False
        self.meele_ataque3 = False
        self.meele_morrendo = False
        self.meele_defendendo = False
        self.meele_esquerda = True
        self.meele_direita = False

        self.sprite_meele_parado = []
        self.sprite_meele_correndo = []
        self.sprite_meele_ataque1 = []
        self.sprite_meele_ataque2 = []
        self.sprite_meele_ataque3 = []
        self.sprite_meele_morrendo = []
        self.sprite_meele_defendendo = []
        
        for i in range(5):
            img = INIMIGO_MEELE_PARADO.subsurface((85 * i, 0), (85,104))
            self.sprite_parado.append(img)
        for i in range(8):
            img = INIMIGO_MEELE_CORRENDO.subsurface((85 * i, 0), (85,104))
            self.sprite_correndo.append(img)
        for i in range(4):
            img = INIMIGO_MEELE_ATAQUE_1.subsurface((85 * i, 0), (85,104))
            self.sprite_ataque1.append(img)
        for i in range(5):
            img = INIMIGO_MEELE_ATAQUE_2.subsurface((85 * i, 0), (85,104))
            self.sprite_ataque2.append(img)
        for i in range(4):
            img = INIMIGO_MEELE_ATAQUE_3.subsurface((85 * i, 0), (85,104))
            self.sprite_ataque3.append(img)
        for i in range(6):
            img = INIMIGO_MEELE_MORRENDO.subsurface((85 * i, 0), (85,104))
            self.sprite_morrendo.append(img)
        for i in range(2):
            img = INIMIGO_MEELE_DEFENDENDO.subsurface((85 * i, 0), (85,104))
            self.sprite_defendendo.append(img)

        self.index_meele_parado = 0
        self.index_meele_correndo = 0
        self.index_meele_ataque1 = 0
        self.index_meele_ataque2 = 0
        self.index_meele_ataque3 = 0
        self.index_meele_morrendo = 0
        self.index_meele_defendendo = 0

        self.image = self.sprite_meele_parado[self.index_meele_parado]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.image = self.sprite_meele_correndo[self.index_meele_correndo]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.image = self.sprite_meele_ataque1[self.index_meele_ataque1]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.image = self.sprite_meele_ataque2[self.index_meele_ataque2]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.image = self.sprite_meele_ataque3[self.index_meele_ataque3]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.image = self.sprite_meele_morrendo[self.index_meele_morrendo]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.image = self.sprite_meele_defendendo[self.index_meele_defendendo]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        if self.meele_direita:
            if self.meele_parado:
                self.index_meele_parado += 0.08
                if self.index_meele_parado > 5:
                    self.index_meele_parado = 0
                self.image = self.sprite_meele_parado[int(self.index_meele_parado)]
            if self.meele_correndo:
                self.index_meele_correndo += 0.08
                if self.index_meele_correndo > 8:
                    self.index_meele_correndo = 0
                self.image = self.sprite_meele_correndo[int(self.index_meele_correndo)]
            if self.meele_ataque1:
                self.index_meele_ataque1 += 0.08
                if self.index_meele_ataque1 > 4:
                    self.index_meele_ataque1 = 0
                self.image = self.sprite_meele_ataque1[int(self.index_meele_ataque1)]
            if self.meele_ataque2:
                self.index_meele_ataque2 += 0.08
                if self.index_meele_ataque2 > 5:
                    self.index_meele_ataque2 = 0
                self.image = self.sprite_meele_ataque2[int(self.index_meele_ataque2)]
            if self.meele_ataque3:
                self.index_meele_ataque3 += 0.08
                if self.index_meele_ataque3 > 4:
                    self.index_meele_ataque3 = 0
                self.image = self.sprite_meele_ataque3[int(self.index_meele_ataque3)]
            if self.meele_morrendo:
                self.index_meele_morrendo += 0.08
                if self.index_meele_morrendo > 6:
                    self.index_meele_morrendo = 0
                self.image = self.sprite_meele_morrendo[int(self.index_meele_morrendo)]
            if self.meele_defendendo:
                self.index_meele_defendendo += 0.08
                if self.index_meele_defendendo > 2:
                    self.index_meele_defendendo = 0
                self.image = self.sprite_meele_defendendo[int(self.index_meele_defendendo)]
        elif self.meele_esquerda:
            if self.meele_parado:
                self.index_meele_parado += 0.08
                if self.index_meele_parado > 5:
                    self.index_meele_parado = 0
                imagem = self.sprite_meele_parado[int(self.index_meele_parado)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.meele_correndo:
                self.index_meele_correndo += 0.08
                if self.index_meele_correndo > 8:
                    self.index_meele_correndo = 0
                imagem = self.sprite_meele_correndo[int(self.index_meele_correndo)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.meele_ataque1:
                self.index_meele_ataque1 += 0.08
                if self.index_meele_ataque1 > 4:
                    self.index_meele_ataque1 = 0
                imagem = self.sprite_meele_ataque1[int(self.index_meele_ataque1)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.meele_ataque2:
                self.index_meele_ataque2 += 0.08
                if self.index_meele_ataque2 > 5:
                    self.index_meele_ataque2 = 0
                imagem = self.sprite_meele_ataque2[int(self.index_meele_ataque2)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.meele_ataque3:
                self.index_meele_ataque3 += 0.08
                if self.index_meele_ataque3 > 4:
                    self.index_meele_ataque3 = 0
                imagem = self.sprite_meele_ataque3[int(self.index_meele_ataque3)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.meele_morrendo:
                self.index_meele_morrendo += 0.08
                if self.index_meele_morrendo > 6:
                    self.index_meele_morrendo = 0
                imagem = self.sprite_meele_morrendo[int(self.index_meele_morrendo)]
                self.image = pygame.transform.flip(imagem, True, False)
            if self.meele_defendendo:
                self.index_meele_defendendo += 0.08
                if self.index_meele_defendendo > 2:
                    self.index_meele_defendendo = 0
                imagem = self.sprite_meele_defendendo[int(self.index_meele_defendendo)]
                self.image = pygame.transform.flip(imagem, True, False)
            
    # def movimenta_meele(self):
 
class InimigoRanged(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ranged_parado = True
        self.ranged_atirando = False
        self.ranged_morrendo = False
        self.ranged_ataque_fraco = False
        self.ranged_ataque_forte = False
        self.ranged_esquerda = True
        self.ranged_direita = False
        
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
    
    # def movimenta_ranged(self):