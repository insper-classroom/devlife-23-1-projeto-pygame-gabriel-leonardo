import pygame
import webbrowser
from constantes import *
from classes.jogo import Jogo

class TelaCreditos(Jogo):
    def desenha(self):
        self.window.blit(pygame.transform.scale(FUNDO, (self.WIDTH, self.HEIGHT)), (0, 0))
        self.window.blit(pygame.transform.scale(NUVEM_1, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem1_vel, 0))  
        self.window.blit(pygame.transform.scale(NUVEM_4, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem4_vel, 0))  
        self.window.blit(pygame.transform.scale_by(LUA, 2.5), (-80, 0))
        self.window.blit(FONTE_TITULO.render('Créditos', True, BRANCO), (40, self.HEIGHT/2 + 20))
        if self.botao == 1:
            self.window.blit(FONTE_TEXTO_POPUP.render('Gabriel Rodrigues e Leonardo Freitas', True, BRANCO), (40, self.HEIGHT/2 + 77))
        else:
            self.window.blit(FONTE_TEXTO.render("Dev's", True, CINZA), (40, self.HEIGHT/2 + 80))
        if self.botao == 2:
            self.window.blit(FONTE_TEXTO_POPUP.render('Site do jogo', True, BRANCO), (40, self.HEIGHT/2 + 127))
        else:
            self.window.blit(FONTE_TEXTO.render('Site do jogo', True, CINZA), (40, self.HEIGHT/2 + 130))
        if self.botao == 3:
            self.window.blit(FONTE_TEXTO_POPUP.render('Doc de Referências', True, BRANCO), (40, self.HEIGHT/2 + 177))
        else:
            self.window.blit(FONTE_TEXTO.render('Doc de Referências', True, CINZA), (40, self.HEIGHT/2 + 180))
        if self.botao == 4:
            self.window.blit(FONTE_TEXTO_POPUP.render('Voltar', True, BRANCO), (40, self.HEIGHT/2 + 227))
        else:
            self.window.blit(FONTE_TEXTO.render('Voltar', True, CINZA), (40, self.HEIGHT/2 + 230))

    def colisao_ponto_retangulo(self, ponto_x, ponto_y, rect_x, rect_y, rect_w, rect_h):
        if (ponto_x >= rect_x and ponto_x <= rect_x + rect_w and
            ponto_y >= rect_y and ponto_y <= rect_y + rect_h):
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
                #if self.botao == 1:

                if self.botao == 2:
                    webbrowser.open_new_tab('https://insper-classroom.github.io/devlife-23-1-projeto-pygame-gabriel-leonardo/')


                if self.botao == 3:
                    webbrowser.open_new_tab('https://docs.google.com/document/d/1WqG90zjR1cBxKDNmpo1__kWCyiw1g8MiH1vKCQGhRsQ/edit?usp=sharingv')

                if self.botao == 4:
                    from classes.tela_inicial import TelaInicial
                    return TelaInicial()

            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 440, 70, 25):
                    self.botao = 1
                elif self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 440, 100, 25) == False:
                    self.botao = 0
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 490, 170, 26):
                    self.botao = 2
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 540, 275, 25):
                    self.botao = 3
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, 42, 590, 85, 25):
                    self.botao = 4
        return self