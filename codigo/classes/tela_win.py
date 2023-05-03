import pygame
import webbrowser
from classes.jogo import Jogo
from classes.tela_inicial import TelaInicial
from constantes import *

class TelaWin(Jogo):
    def desenha(self):
        self.window.blit(pygame.transform.scale(FUNDO, (self.WIDTH, self.HEIGHT)), (0, 0))
        self.window.blit(pygame.transform.scale(NUVEM_1, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem1_vel, 0))  
        self.window.blit(pygame.transform.scale(NUVEM_4, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem4_vel, 0))  
        self.window.blit(pygame.transform.scale_by(LUA, 2.5), (-80, 0))
        self.window.blit(FONTE_TITULO.render('Vitória!', True, BRANCO), (self.WIDTH/2 - len('vitoria!') * 10, self.HEIGHT/2 + 20))
        if self.botao == 1:
            self.window.blit(FONTE_TEXTO_POPUP.render('Novo Jogo', True, BRANCO), (self.WIDTH/2 - len('novo jogo') * 10, self.HEIGHT/2 + 77))
        else:
            self.window.blit(FONTE_TEXTO.render("Novo Jogo", True, CINZA), (self.WIDTH/2 - len('novo jogo') * 9, self.HEIGHT/2 + 80))
        if self.botao == 2:
            self.window.blit(FONTE_TEXTO_POPUP.render('Tela Inicial', True, BRANCO), (self.WIDTH/2 - len('tela inicial') * 8, self.HEIGHT/2 + 127))
        else:
            self.window.blit(FONTE_TEXTO.render('Tela Inicial', True, CINZA), (self.WIDTH/2 - len('tela inicial') * 7, self.HEIGHT/2 + 130))
        if self.botao == 3:
            self.window.blit(FONTE_TEXTO_POPUP.render('Site', True, BRANCO), (self.WIDTH/2 - len('site') * 9, self.HEIGHT/2 + 177))
        else:
            self.window.blit(FONTE_TEXTO.render('Site', True, CINZA), (self.WIDTH/2 - len('site') * 8, self.HEIGHT/2 + 180))
        if self.botao == 4:
            self.window.blit(FONTE_TEXTO_POPUP.render('Sair', True, BRANCO), (self.WIDTH/2 - len('sair') * 9, self.HEIGHT/2 + 227))
        else:
            self.window.blit(FONTE_TEXTO.render('Sair', True, CINZA), (self.WIDTH/2 - len('sair') * 8, self.HEIGHT/2 + 230))

    def colisao_ponto_retangulo(self, ponto_x, ponto_y, rect_x, rect_y, rect_w, rect_h):
        if ponto_x >= rect_x and ponto_x <= rect_x + rect_w and ponto_y >= rect_y and ponto_y <= rect_y + rect_h:
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
                    from classes.tela_jogo import TelaJogo
                    return TelaJogo()
                if self.botao == 2:
                    return TelaInicial()
                if self.botao == 3:
                    webbrowser.open_new_tab('https://insper-classroom.github.io/devlife-23-1-projeto-pygame-gabriel-leonardo/')
                if self.botao == 4:
                    pygame.quit()
                    quit()

            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, self.WIDTH/2 - len('novo jogo') * 10, self.HEIGHT/2 + 80, 145, 25):
                    self.botao = 1
                elif self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 440, 100, 25) == False:
                    self.botao = 0
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, self.WIDTH/2 - len('tela inicial') * 7, self.HEIGHT/2 + 130, 170, 26):
                    self.botao = 2
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, self.WIDTH/2 - len('site') * 9, self.HEIGHT/2 + 180, 60, 25):
                    self.botao = 3
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, self.WIDTH/2 - len('sair') * 9, self.HEIGHT/2 + 230, 60, 25):
                    self.botao = 4
        return self