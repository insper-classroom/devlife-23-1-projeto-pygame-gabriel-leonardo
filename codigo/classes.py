import pygame
from constantes import *

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
        
    def roda(self):
        self.desenha()
        pygame.display.update()
    
    def update(self):
        pass

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
    def desenha(self):
        self.window.fill((255, 255, 255))
        self.window.blit(pygame.transform.scale(FUNDO_INICIO, (self.WIDTH, self.HEIGHT)), (0, 0))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return TelaGameOver()
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