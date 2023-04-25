import pygame
from constantes import *
import os



class Jogo:
    def __init__(self):
        # Inicialização do pygame:
        self.WIDTH = 1024
        self.HEIGHT =  720 
        self.nuvem1_vel = NUVEM_1_VEL
        self.nuvem4_vel = NUVEM_4_VEL
        self.nuv_dir = 0
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.botao = 0
        self.musica = True
        self.sons = True
        self.show_fps = False
        self.t0 = -1
        self.deltat = (pygame.time.get_ticks() - self.t0) / 1000
        self.scroll = 0

    def roda(self):
        # Update na tela(não precisa ficar chamando a funcao pygame.display.update):
        self.desenha()
        pygame.display.update()
    
    def update(self):
        # Define a taxa de atualizacao da tela:
        pygame.time.Clock().tick(60)

class Player(pygame.sprite.Sprite, Jogo):
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
        print(self.index_pulando)

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

class InimigoMeele(pygame.sprite.Sprite, Jogo):
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
 
class InimigoRanged(pygame.sprite.Sprite, Jogo):
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
                      
class TelaInicial(Jogo):
    def desenha(self):
        self.window.blit(pygame.transform.scale(FUNDO, (self.WIDTH, self.HEIGHT)), (0, 0))
        self.window.blit(pygame.transform.scale(NUVEM_1, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem1_vel, 0))  
        self.window.blit(pygame.transform.scale(NUVEM_4, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem4_vel, 0))
        self.window.blit(pygame.transform.scale_by(LUA, 2.5), (-80, 0))

        self.window.blit(FONTE_TITULO.render('SHADOW OF THE NINJA', True, BRANCO), (40, self.HEIGHT/2 + 20))
        
        if self.botao == 1:
            self.window.blit(FONTE_TEXTO_POPUP.render('Novo jogo', True, BRANCO), (40, self.HEIGHT/2 + 77))
        else:
            self.window.blit(FONTE_TEXTO.render('Novo jogo', True, CINZA), (40, self.HEIGHT/2 + 80))

        if self.botao == 2:
            self.window.blit(FONTE_TEXTO_POPUP.render('Opções', True, BRANCO), (40, self.HEIGHT/2 + 127))
        else:
            self.window.blit(FONTE_TEXTO.render('Opções', True, CINZA), (40, self.HEIGHT/2 + 130))

        if self.botao == 3:
            self.window.blit(FONTE_TEXTO_POPUP.render('Creditos', True, BRANCO), (40, self.HEIGHT/2 + 177))
        else:
            self.window.blit(FONTE_TEXTO.render('Créditos', True, CINZA), (40, self.HEIGHT/2 + 180))

        if self.botao == 4:
            self.window.blit(FONTE_TEXTO_POPUP.render('Sair', True, BRANCO), (40, self.HEIGHT/2 + 227))
        else:
            self.window.blit(FONTE_TEXTO.render('Sair', True, CINZA), (40, self.HEIGHT/2 + 230))

    def colisao_ponto_retangulo(self, ponto_x, ponto_y, rect_x, rect_y, rect_w, rect_h):
        if (
        rect_x <= ponto_x and 
        ponto_x <= rect_x + rect_w and 
        rect_y <= ponto_y and 
        ponto_y <= rect_y + rect_h
        ):
            return True
        else:
            return False
    
    def update(self):
        if self.nuv_dir == -1:
            self.nuvem1_vel -= 0.5
            self.nuvem4_vel += 0.5
        if self.nuv_dir == 1:
            self.nuvem1_vel += 0.5
            self.nuvem4_vel -= 0.5
        if self.nuvem1_vel == 50:
            self.nuv_dir = -1
        if self.nuvem1_vel == 0.5:
            self.nuv_dir = 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.botao == 1:
                    return TelaJogo()
                elif self.botao == 2:
                    return TelaOpcoes()
                elif self.botao == 3:
                    return TelaCreditos()
                elif self.botao == 4:
                    pygame.quit()
                    quit()
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 440, 145, 25):
                    self.botao = 1
                elif self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 490, 145, 25) == False:
                    self.botao = 0
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 490, 105, 25):
                    self.botao = 2
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 540, 115, 25):
                    self.botao = 3
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 590, 60, 25):
                    self.botao = 4
        return self 
    
class TelaJogo(Jogo):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        self.background = []
        for i in range(1, 13):
            img = pygame.image.load(f'../assets/backgrounds/TelaJogo/Backgorund_Floresta/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (self.WIDTH, self.HEIGHT))
            self.background.append(img)
        
    def desenha(self):
        self.window.fill((255, 255, 255))
        for x in range(12):
            for i in self.background:
                self.window.blit(i, (x * self.WIDTH - self.scroll, 0))
        self.sprites.draw(self.window)
        self.sprites.update()

    def update(self):
        self.player.movimenta_player()
        key = pygame.key.get_pressed()

        # Movimentação do player (e ataque):
        if self.player.ataque_forte == False and self.player.ataque_fraco == False:
            if key[pygame.K_a]:
                if self.scroll == 0:
                    self.player.rect.x -= 1
                elif self.player.rect.x <= 511 or self.scroll != 1000 and self.scroll != 0:
                    self.scroll -= 1
                elif self.scroll == 1000:
                    self.player.rect.x -= 1
                self.player.andando = True
                self.player.esquerda = True
                self.player.direita = False
            if key[pygame.K_d]:
                if self.scroll == 1000:
                    self.player.rect.x += 1
                elif self.player.rect.x >= 511 or self.scroll != 1000 and self.scroll != 0:
                    self.scroll += 1
                elif self.scroll == 0:
                    self.player.rect.x += 1
                self.player.andando = True
                self.player.direita = True
                self.player.esquerda = False
            if key[pygame.K_LSHIFT] and key[pygame.K_a]:
                if self.scroll == 0:
                    self.player.rect.x -= 1
                elif self.player.rect.x <= 511 or self.scroll != 1000 and self.scroll != 0:
                    self.scroll -= 2
                elif self.scroll == 1000:
                    self.player.rect.x -= 1
                self.player.andando = False
                self.player.correndo = True
            if key[pygame.K_LSHIFT] and key[pygame.K_d]: 
                if self.scroll == 1000:
                    self.player.rect.x += 1
                elif self.player.rect.x >= 511 or self.scroll != 1000 and self.scroll != 0:
                    self.scroll += 2
                elif self.scroll == 0:
                    self.player.rect.x += 1
                self.player.andando = False
                self.player.correndo = True
            if key[pygame.K_SPACE]:
                if self.player.pulos < self.player.max_pulos:
                    self.player.gravidade = -10
                    self.player.pulos += 1
                    self.player.pulando = True
                    self.player.andando = False
                    self.player.correndo = False
                    self.player.parado = False
        if self.player.correndo == False and self.player.pulando == False:
            if key[pygame.K_q]:
                self.player.ataque_forte = True
                if self.player.parado == True:
                    self.player.parado = False
            if key[pygame.K_e]:
                self.player.ataque_fraco = True
                if self.player.parado == True:
                    self.player.parado = False
        if self.scroll < 0:
            self.scroll = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return TelaGameOver()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.player.andando = False
                    self.player.parado = True
                    self.player.correndo = False
                if event.key == pygame.K_LSHIFT:
                    self.player.correndo = False
        return self 
    
class TelaOpcoes(Jogo):
    def desenha(self):
        self.window.blit(pygame.transform.scale(FUNDO, (self.WIDTH, self.HEIGHT)), (0, 0))
        self.window.blit(pygame.transform.scale(NUVEM_1, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem1_vel, 0))  
        self.window.blit(pygame.transform.scale(NUVEM_4, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem4_vel, 0))  
        self.window.blit(pygame.transform.scale_by(LUA, 2.5), (-80, 0))
        self.window.blit(FONTE_TITULO.render('OPÇÕES', True, BRANCO), (40, self.HEIGHT/2 + 20))


        if self.botao == 1:
            if self.musica == True:
                self.window.blit(FONTE_TEXTO_POPUP.render('Música [LIGADA]', True, BRANCO), (40, self.HEIGHT/2 + 77))
            else:
                self.window.blit(FONTE_TEXTO_POPUP.render('Música [DESLIGADA]', True, BRANCO), (40, self.HEIGHT/2 + 77))
        else:
            self.window.blit(FONTE_TEXTO.render('Música', True, CINZA), (40, self.HEIGHT/2 + 80))
        
        if self.botao == 2:
            if self.sons == True:
                self.window.blit(FONTE_TEXTO_POPUP.render('Efeitos Sonoros [LIGADOS]', True, BRANCO), (40, self.HEIGHT/2 + 127))
            else:
                self.window.blit(FONTE_TEXTO_POPUP.render('Efeitos Sonoros [DESLIGADOS]', True, BRANCO), (40, self.HEIGHT/2 + 127))
        else:
            self.window.blit(FONTE_TEXTO.render('Efeitos Sonoros', True, CINZA), (40, self.HEIGHT/2 + 130))

        if self.botao == 3:
            if self.show_fps == True:
                self.window.blit(FONTE_TEXTO_POPUP.render('FPS [LIGADO]', True, BRANCO), (40, self.HEIGHT/2 + 177))
            else:
                self.window.blit(FONTE_TEXTO_POPUP.render('FPS [DESLIGADO]', True, BRANCO), (40, self.HEIGHT/2 + 177))
        else:
            self.window.blit(FONTE_TEXTO.render('FPS', True, CINZA), (40, self.HEIGHT/2 + 180))
        
        if self.botao == 4:
            self.window.blit(FONTE_TEXTO_POPUP.render('Voltar', True, BRANCO), (40, self.HEIGHT/2 + 227))
        else:
            self.window.blit(FONTE_TEXTO.render('Voltar', True, CINZA), (40, self.HEIGHT/2 + 230))


    def colisao_ponto_retangulo(self, ponto_x, ponto_y, rect_x, rect_y, rect_w, rect_h):
        if (
            ponto_x >= rect_x and ponto_x <= rect_x + rect_w and
            ponto_y >= rect_y and ponto_y <= rect_y + rect_h
        ):
            return True
        else:
            return False

    def update(self):
        if self.nuv_dir == -1:
            self.nuvem1_vel -= 0.5
            self.nuvem4_vel += 0.5
        if self.nuv_dir == 1:
            self.nuvem1_vel += 0.5
            self.nuvem4_vel -= 0.5
        if self.nuvem1_vel == 50:
            self.nuv_dir = -1
        if self.nuvem1_vel == 0.5:
            self.nuv_dir = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.botao == 1:
                    if self.musica == False:
                        self.musica = True
                    elif self.musica == True:
                        self.musica = False
                if self.botao == 2:
                    if self.sons == False:
                        self.sons = True
                    elif self.sons == True:
                        self.sons = False
                if self.botao == 3:
                    if self.show_fps == False:
                        self.show_fps = True
                    elif self.show_fps == True:
                        self.show_fps = False
                if self.botao == 4:
                    return TelaInicial()

            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 440, 200, 25):
                    self.botao = 1
                elif self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 440, 100, 25) == False:
                    self.botao = 0
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 490, 132, 25):
                    self.botao = 2
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 540, 85, 25):
                    self.botao = 3
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 590, 60, 25):
                    self.botao = 4
        return self
    
class TelaCreditos(Jogo):
    def desenha(self):
        self.window.fill((0, 255, 0))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return TelaGameOver()
        return self
    
class TelaGameOver(Jogo):
    def desenha(self):
        self.window.fill((255, 0, 0))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return TelaInicial()
        return self