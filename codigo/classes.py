import pygame
from constantes import *

class Jogo:
    def __init__(self):
        self.WIDTH = 1024
        self.HEIGHT =  720 
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.botao = 0
        
    def roda(self):
        self.desenha()
        pygame.display.update()
    
    def update(self):
        pass

class TelaInicial(Jogo):
    def desenha(self):
        for image in [FUNDO, LUA, NUVEM_1, NUVEM_4]:
            self.window.blit(pygame.transform.scale(image, (self.WIDTH, self.HEIGHT)), (0, 0))  
        self.window.blit(FONTE_TITULO.render('Shadow of the Ninja', True, BRANCO), (40, self.HEIGHT/2 + 20))

        if self.botao == 1:
            self.window.blit(FONTE_TEXTO_POPUP.render('novo jogo', True, BRANCO), (40, self.HEIGHT/2 + 77))
        else:
            pygame.draw.rect(self.window, (COR_FUNDO), pygame.Rect((40, 440), (160, 20)))
            self.window.blit(FONTE_TEXTO.render('novo jogo', True, CINZA), (40, self.HEIGHT/2 + 80))

        if self.botao == 2:
            self.window.blit(FONTE_TEXTO_POPUP.render('opcoes', True, BRANCO), (40, self.HEIGHT/2 + 127))
        else:
            pygame.draw.rect(self.window, (COR_FUNDO), pygame.Rect((40, 490), (110, 20)))
            self.window.blit(FONTE_TEXTO.render('opcoes', True, CINZA), (40, self.HEIGHT/2 + 130))

        if self.botao == 3:
            self.window.blit(FONTE_TEXTO_POPUP.render('creditos', True, BRANCO), (40, self.HEIGHT/2 + 177))
        else:
            pygame.draw.rect(self.window, (COR_FUNDO), pygame.Rect((40, 540), (140, 20)))
            self.window.blit(FONTE_TEXTO.render('creditos', True, CINZA), (40, self.HEIGHT/2 + 180))

        if self.botao == 4:
            self.window.blit(FONTE_TEXTO_POPUP.render('sair', True, BRANCO), (40, self.HEIGHT/2 + 227))
        else:
            pygame.draw.rect(self.window, (COR_FUNDO), pygame.Rect((40, 590), (65, 20)))
            self.window.blit(FONTE_TEXTO.render('sair', True, CINZA), (40, self.HEIGHT/2 + 230))

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
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 40, 440, 160, 20):
                    self.botao = 1
                elif self.colisao_ponto_retangulo(mouse_x, mouse_y, 40, 490, 110, 20) == False:
                    self.botao = 0
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 40, 490, 110, 20):
                    self.botao = 2
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 40, 540, 140, 20):
                    self.botao = 3
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 40, 590, 65, 20):
                    self.botao = 4
        return self 
    
class TelaJogo(Jogo):
    def desenha(self):
        self.window.fill((255, 255, 255))

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
        self.window.fill((255, 255, 0))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return TelaGameOver()
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