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

        ## INICIALIZAÇÃO DE IMAGENS (ANIMAÇÃO):

        # Adicionando as imagens em listas (uma lista para cada tipo de animação. Ex.: parado, andando, pulando, etc.):
        self.sprite_parado = []
        self.sprite_andando = []
        self.sprite_correndo = []
        for i in range(6):
            img = PLAYER_PARADO.subsurface((128 * i, 0), (128,128))
            self.sprite_parado.append(img)
        for i in range(8):
            img = PLAYER_ANDANDO.subsurface((128 * i, 0), (128,128))
            self.sprite_andando.append(img)
        for i in range(7):
            img = PLAYER_CORRENDO.subsurface((128 * i, 0), (128,128))
            self.sprite_correndo.append(img)
        
        # Indexes:
        self.index_parado = 0
        self.index_andando = 0
        self.index_correndo = 0

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

        # Movimentação:
        self.rect.x = 512
        self.rect.y = 510
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.gravidade = 0
        self.last_updated = 0
        self.pulos = 0
        self.max_pulos = 1
    
    def update(self):
        # Função que atualiza a animação do player:
        if self.parado:
            self.index_parado += 0.1
            if self.index_parado > 5:
                self.index_parado = 0
            self.image = self.sprite_parado[int(self.index_parado)]
        if self.andando:
            self.index_andando += 0.1
            if self.index_andando > 7:
                self.index_andando = 0
            self.image = self.sprite_andando[int(self.index_andando)]
        if self.correndo:
            self.index_correndo += 0.1
            if self.index_correndo > 6:
                self.index_correndo = 0
            self.image = self.sprite_correndo[int(self.index_correndo)]

    def movimenta_player(self):
        self.gravidade += 0.3
        self.rect.y += self.gravidade
        prox_posicao_x = self.rect.x + self.velocidade_x

        # Verifica borda:
        if prox_posicao_x < 0:
            prox_posicao_x = 0
            if self.rect.y < 510:
                self.rect.y = self.rect.y
            else:
                self.rect.y = 510
        elif prox_posicao_x > 896:
            prox_posicao_x = 896
            if self.rect.y < 510:
                self.rect.y = self.rect.y
            else:
                self.rect.y = 510
        elif self.rect.y > 510:
            self.rect.y = 510
            self.pulos = 0
            self.pulando = False
        
        # Atualiza
        self.rect.x = prox_posicao_x
        self.velocidade_x = self.velocidade_x       

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
            img = pygame.image.load(f'../assets/backgrounds\TelaJogo\Backgorund_Floresta\{i}.png').convert_alpha()
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

        # Movimentação do player:
        if key[pygame.K_a]:
            if self.scroll == 0:
                self.player.rect.x -= 1
            elif self.player.rect.x <= 511 or self.scroll != 1000 and self.scroll != 0:
                self.scroll -= 2
            elif self.scroll == 1000:
                self.player.rect.x -= 1
            self.player.andando = True
        if key[pygame.K_d]:
            if self.scroll == 1000:
                self.player.rect.x += 1
            elif self.player.rect.x >= 511 or self.scroll != 1000 and self.scroll != 0:
                self.scroll += 2
            elif self.scroll == 0:
                self.player.rect.x += 1
            self.player.andando = True
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
                self.player.andando = False
                self.player.parado = False
                self.player.correndo = False
                self.player.pulando = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.player.andando = False
                    self.player.parado = True
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