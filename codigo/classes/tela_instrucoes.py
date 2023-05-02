import pygame
from constantes import *
from classes.jogo import Jogo

class TelaInstrucoes(Jogo):
    def desenha(self):
        self.window.blit(pygame.transform.scale(FUNDO, (self.WIDTH, self.HEIGHT)), (0, 0))
        self.window.blit(pygame.transform.scale(NUVEM_1, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem1_vel, 0))
        self.window.blit(pygame.transform.scale(NUVEM_4, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem4_vel, 0))
        self.window.blit(pygame.transform.scale_by(LUA, 2.5), (-80, 0))

        self.window.blit(FONTE_TEXTO_POPUP.render("História", True, (255, 255, 255)), (self.WIDTH//4 - len('história') * 9, 30))
        self.window.blit(FONTE_TEXTO.render("   O jogador controla um ninja", True, (CINZA)), (30, 80))
        self.window.blit(FONTE_TEXTO.render("que precisa atravessar a mortal", True, (CINZA)), (30, 110))
        self.window.blit(FONTE_TEXTO.render("Floresta Negra para recuperar o", True, (CINZA)), (30, 140))
        self.window.blit(FONTE_TEXTO.render("artefato milenar da sua família", True, (CINZA)), (30, 170))
        self.window.blit(FONTE_TEXTO.render("que foi roubado pelo clã inimigo.", True, (CINZA)), (30, 200))
        self.window.blit(FONTE_TEXTO.render("   Para isso, ele deve enfrentar", True, (CINZA)), (30, 230))
        self.window.blit(FONTE_TEXTO.render("os vários inimigos que surgem em", True, (CINZA)), (30, 260))
        self.window.blit(FONTE_TEXTO.render("seu caminho, além  de  conseguir", True, (CINZA)), (30, 290))
        self.window.blit(FONTE_TEXTO.render("superar a famosa floresta.", True, (CINZA)), (30, 320))
        self.window.blit(FONTE_TEXTO_POPUP.render("Pressione [ENTER] para jogar", True, (255, 255, 255)), (self.WIDTH//2 - len('Pressione [ENTER] para jogar') * 9, 650))

        self.window.blit(FONTE_TEXTO_POPUP.render("Controles", True, (255, 255, 255)), (self.WIDTH//4 - len('controles') * 9, 380))
        if self.botao == 1:
            self.window.blit(FONTE_TEXTO_POPUP.render("Movimentação", True, (BRANCO)), (self.WIDTH//4 - len('movimentação') * 10 , 430))
            self.window.blit(FONTE_TEXTO.render("[A] - Andar para esquerda", True, (CINZA)), (self.WIDTH//2, 30))
            self.window.blit(FONTE_TEXTO.render("[A]", True, (BRANCO)), (self.WIDTH//2, 30))
            self.window.blit(FONTE_TEXTO.render("[CTRL] + [A] - Correr para esquerda", True, (CINZA)), (self.WIDTH//2, 70))
            self.window.blit(FONTE_TEXTO.render("[CTRL] + [A]", True, (BRANCO)), (self.WIDTH//2, 70))
            self.window.blit(FONTE_TEXTO.render("[D] - Andar para direita", True, (CINZA)), (self.WIDTH//2, 110))
            self.window.blit(FONTE_TEXTO.render("[D]", True, (BRANCO)), (self.WIDTH//2, 110))
            self.window.blit(FONTE_TEXTO.render("[CTRL] + [D] - Correr para direita", True, (CINZA)), (self.WIDTH//2, 150))
            self.window.blit(FONTE_TEXTO.render("[CTRL] + [D]", True, (BRANCO)), (self.WIDTH//2, 150))
            self.window.blit(FONTE_TEXTO.render("[ESPAÇO] - Pular", True, (CINZA)), (self.WIDTH//2, 190))
            self.window.blit(FONTE_TEXTO.render("[ESPAÇO]", True, (BRANCO)), (self.WIDTH//2, 190))
        else:
            self.window.blit(FONTE_TEXTO.render("Movimentação", True, (CINZA)), (self.WIDTH//4 - len('movimentação') * 9, 430))

        if self.botao == 2:
            self.window.blit(FONTE_TEXTO_POPUP.render("Combate", True, (BRANCO)), (self.WIDTH//4 - len('combateE') * 10, 480))
            self.window.blit(FONTE_TEXTO.render("[Q] - Ataque fraco", True, (CINZA)), (self.WIDTH//2, 30))
            self.window.blit(FONTE_TEXTO.render("[Q]", True, (BRANCO)), (self.WIDTH//2, 30))

            self.window.blit(FONTE_TEXTO.render("[E] - Ataque forte", True, (CINZA)), (self.WIDTH//2, 70))
            self.window.blit(FONTE_TEXTO.render("[E]", True, (BRANCO)), (self.WIDTH//2, 70))
            self.window.blit(FONTE_TEXTO.render("[C] - Defesa", True, (CINZA)), (self.WIDTH//2, 110))
            self.window.blit(FONTE_TEXTO.render("[C]", True, (BRANCO)), (self.WIDTH//2, 110))
        else:
            self.window.blit(FONTE_TEXTO.render("Combate", True, (CINZA)), (self.WIDTH//4 - len('comabteE') * 9, 480))
        
        if self.botao == 3:
            self.window.blit(FONTE_TEXTO_POPUP.render("Interações", True, (BRANCO)), (self.WIDTH//4 - len('interacoes') * 9, 530))
            self.window.blit(FONTE_TEXTO.render("[ESTAMINA] - Ao atacar ou pular, o ", True, (CINZA)), (self.WIDTH//2, 30))
            self.window.blit(FONTE_TEXTO.render("[ESTAMINA]", True, (BRANCO)), (self.WIDTH//2, 30))
            self.window.blit(FONTE_TEXTO.render("jogador começa a ficar cansado, e", True, (CINZA)), (self.WIDTH//2, 70))
            self.window.blit(FONTE_TEXTO.render("precisa esperar um tempo para que", True, (CINZA)), (self.WIDTH//2, 110))
            self.window.blit(FONTE_TEXTO.render("sua estamina volte à 100%.", True, (CINZA)), (self.WIDTH//2, 150))
            self.window.blit(FONTE_TEXTO.render("A situação atual da estamina pode", True, (CINZA)), (self.WIDTH//2, 190))
            self.window.blit(FONTE_TEXTO.render("ser reparada com base no nível de ", True, (CINZA)), (self.WIDTH//2, 230))
            self.window.blit(FONTE_TEXTO.render("esmaecimento da tela.", True, (CINZA)), (self.WIDTH//2, 270))
            self.window.blit(FONTE_TEXTO.render("[VIDA] - A análise do nível atual", True, (CINZA)), (self.WIDTH//2, 310))
            self.window.blit(FONTE_TEXTO.render("[VIDA]", True, (BRANCO)), (self.WIDTH//2, 310))
            self.window.blit(FONTE_TEXTO.render("de vida do jogador é feita com a", True, (CINZA)), (self.WIDTH//2, 350))
            self.window.blit(FONTE_TEXTO.render("mesma lógica da estamina, onde ", True, (CINZA)), (self.WIDTH//2, 390))
            self.window.blit(FONTE_TEXTO.render("quanto mais vermelha a tela, mais", True, (CINZA)), (self.WIDTH//2, 430))
            self.window.blit(FONTE_TEXTO.render("próximo da morte o jogador está.", True, (CINZA)), (self.WIDTH//2, 470))
        else:
            self.window.blit(FONTE_TEXTO.render("Interações", True, (CINZA)), (self.WIDTH//4 - len('interacoes') * 8, 530))

            



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
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.colisao_ponto_retangulo(mouse_x, mouse_y, self.WIDTH//4 - len('movimentacao') * 9, 430, 210, 25):
                    self.botao = 1
                elif self.colisao_ponto_retangulo(mouse_x, mouse_y, self.WIDTH//4 - len('combatee') * 9, 480, 130, 25):
                    self.botao = 2
                elif self.colisao_ponto_retangulo(mouse_x, mouse_y, self.WIDTH//4 - len('intreações') * 8, 530, 150, 25):
                    self.botao = 3
                else:
                    self.botao = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    from classes.tela_jogo import TelaJogo
                    return TelaJogo()
        return self