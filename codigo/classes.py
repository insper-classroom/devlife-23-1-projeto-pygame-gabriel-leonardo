import pygame
from constantes import *
import os



class Jogo:
    def __init__(self):
        self.WIDTH = 1024
        self.HEIGHT =  720 
        self.nuvem1_vel = NUVEM_1_VEL
        self.nuvem4_vel = NUVEM_4_VEL
        self.nuv_dir = 0
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.botao = 0
        self.volume = True
        self.wasd = True    
        # self.grupos = {'all_sprites': pygame.sprite.Group()}
        # self.player = Player(self.grupos)
        self.t0 = -1
        self.deltat = (pygame.time.get_ticks() - self.t0) / 1000

    def roda(self):
        self.desenha()
        pygame.display.update()
    
    def update(self):
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # if self.wasd == True:
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_a:
        #             self.player_vel = -10

class Player(pygame.sprite.Sprite, Jogo):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.player_vel = 0

        self.parado = True
        self.andando = False
        self.pulando = False

        self.imgs = {'parado': PLAYER_PARADO,
                     'andando': PLAYER_ANDANDO}
        self.imgs['parado'].convert_alpha()
        self.imgs['andando'].convert_alpha()

        # self.grupos = grupos

        # self.grupos['all_sprites'].add(self)
        

        self.sprite_parado = []
        self.sprite_andando = []
        for i in range(6):
            img = self.imgs['parado'].subsurface((128 * i, 0), (128,128))
            self.sprite_parado.append(img)

        for i in range(8):
            img = self.imgs['andando'].subsurface((128 * i, 0), (128,128))
            self.sprite_andando.append(img)

        self.index_parado = 0
        self.image = self.sprite_parado[self.index_parado]

        self.image = PLAYER_PARADO.convert_alpha()
        self.rect = self.image.get_rect()

       # self.index_andando = 0
       # self.image = self.sprite_andando[self.index_andando]

    # def update(self):
    #     self.rect.x += self.player_vel * deltat
                    
        self.index_parado += 0.1
        if self.index_parado > 5:
            self.index_parado = 0
        self.image = self.sprite_parado[int(self.index_parado)]

        
    #    self.index_andando += 0.1
    #    if self.index_andando > 7:
    #        self.index_andando = 0
    #    self.image = self.sprite_andando[int(self.index_andando)]

        #Movimentação:
        self.rect.x = 100
        self.rect.y = 510
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.gravidade = 0
        self.last_updated = 0
        self.pulos = 0
        self.max_pulos = 1

    def movimenta_player(self):
        self.gravidade += 0.3
        self.rect.y += self.gravidade
        prox_posicao_x = self.rect.x + self.velocidade_x

        # Verifica borda:
        if prox_posicao_x < 0:
            prox_posicao_x = 0
            self.velocidade_x = 0
        elif prox_posicao_x > 1024:
            prox_posicao_x = 1024
            self.velocidade_x = 0
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

    def desenha(self):
        self.window.fill((255, 255, 255))
        self.window.blit(pygame.transform.scale(FUNDO_INICIO, (self.WIDTH, self.HEIGHT)), (0, 0))
        self.sprites.update()
        self.sprites.draw(self.window)

    def update(self):
        # self.grupos['all_sprites'].update(self.deltat)
        self.player.movimenta_player()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN:
                    return TelaGameOver()
                if event.key == pygame.K_d:
                    self.player.velocidade_x += 3 
                elif event.key == pygame.K_a:
                    self.player.velocidade_x -= 3 
                elif event.key == pygame.K_SPACE:
                    if self.player.pulos < self.player.max_pulos:
                        self.player.gravidade = -10
                        self.player.pulos += 1
                        self.player.pulando = True
                self.player.parado = False
                self.player.andando = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.velocidade_x -= 3 
                elif event.key == pygame.K_a:
                    self.player.velocidade_x += 3 
                self.player.parado = True
                self.player.andando = False
            

        return self 
    
class TelaOpcoes(Jogo):
    def desenha(self):
        self.window.blit(pygame.transform.scale(FUNDO, (self.WIDTH, self.HEIGHT)), (0, 0))
        self.window.blit(pygame.transform.scale(NUVEM_1, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem1_vel, 0))  
        self.window.blit(pygame.transform.scale(NUVEM_4, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem4_vel, 0))  
        self.window.blit(pygame.transform.scale_by(LUA, 2.5), (-80, 0))
        self.window.blit(FONTE_TITULO.render('OPÇÕES', True, BRANCO), (40, self.HEIGHT/2 + 20))


        if self.botao == 1:
            if self.volume == True:
                self.window.blit(FONTE_TEXTO_POPUP.render('Sons e música [LIGADOS]', True, BRANCO), (40, self.HEIGHT/2 + 77))
            else:
                self.window.blit(FONTE_TEXTO_POPUP.render('Sons e música [DESLIGADOS]', True, BRANCO), (40, self.HEIGHT/2 + 77))
        else:
            self.window.blit(FONTE_TEXTO.render('Sons e música', True, CINZA), (40, self.HEIGHT/2 + 80))
        
        if self.botao == 2:
            if self.wasd == True:
                self.window.blit(FONTE_TEXTO_POPUP.render('Controles [W A S D]', True, BRANCO), (40, self.HEIGHT/2 + 127))
            else:
                self.window.blit(FONTE_TEXTO_POPUP.render('Controles [S E T A S]', True, BRANCO), (40, self.HEIGHT/2 + 127))
        else:
            self.window.blit(FONTE_TEXTO.render('Controles', True, CINZA), (40, self.HEIGHT/2 + 130))

        if self.botao == 3:
            self.window.blit(FONTE_TEXTO_POPUP.render('Voltar', True, BRANCO), (40, self.HEIGHT/2 + 177))
        else:
            self.window.blit(FONTE_TEXTO.render('Voltar', True, CINZA), (40, self.HEIGHT/2 + 180))

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
                    if self.volume == False:
                        self.volume = True
                    elif self.volume == True:
                        self.volume = False
                if self.botao == 2:
                    if self.wasd == False:
                        self.wasd = True
                    elif self.wasd == True:
                        self.wasd = False
                if self.botao == 3:
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