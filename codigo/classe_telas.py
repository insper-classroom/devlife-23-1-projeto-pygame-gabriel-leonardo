import pygame
from classe_players import Player, InimigoMeele, InimigoRanged
from constantes import *

# Função principal do jogo
class Jogo:
    def __init__(self):
        # Inicialização do jogo:
        # Tamaho da tela
        self.WIDTH = 1024
        self.HEIGHT =  720
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # Velocidade das nuvens da tela inicial
        self.nuvem1_vel = NUVEM_1_VEL
        self.nuvem4_vel = NUVEM_4_VEL
        self.nuv_dir = 0
        # Variável que controla a tela do jogo
        self.scroll = 0
        # Variáveis de controle
        self.botao = 0
        # Variáveis das opções
        self.musica = True
        self.sons = True
        self.show_fps = False
        # Outros
        self.t0 = -1
        self.deltat = (pygame.time.get_ticks() - self.t0) / 1000

    # Update na tela(não precisa ficar chamando a funcao pygame.display.update):
    def roda(self):
        self.desenha()
        pygame.display.update()

# Primeira tela do jogo   
class TelaInicial(Jogo):
    def desenha(self):
        # Desenha o fundo
        self.window.blit(pygame.transform.scale(FUNDO, (self.WIDTH, self.HEIGHT)), (0, 0))
        self.window.blit(pygame.transform.scale(NUVEM_1, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem1_vel, 0))  
        self.window.blit(pygame.transform.scale(NUVEM_4, (self.WIDTH + 100, self.HEIGHT)), (-50 + self.nuvem4_vel, 0))
        self.window.blit(pygame.transform.scale_by(LUA, 2.5), (-80, 0))
        # Desenha o título
        self.window.blit(FONTE_TITULO.render('SHADOW OF THE NINJA', True, BRANCO), (40, self.HEIGHT/2 + 20))
        # Desenha os botões
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
    # Função que verifica se o mouse está em cima de um botão
    def colisao_ponto_retangulo(self, ponto_x, ponto_y, rect_x, rect_y, rect_w, rect_h):
        if (rect_x <= ponto_x and ponto_x <= rect_x + rect_w and 
        rect_y <= ponto_y and ponto_y <= rect_y + rect_h):
            return True
        else:
            return False
    # Função que atualiza a tela
    def update(self):
        # Movimentação das nuvens
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
            # Verifica se algum botão da tela foi clicado
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
            # Verifica se o mouse está em cima de algum botão para fazer o efeito de pop-up
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
    
# Tela do jogo
class TelaJogo(Jogo):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        
        self.meele = InimigoMeele()
        self.meele_sprites = pygame.sprite.Group()
        self.meele_sprites.add(self.meele)

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
        #self.window.blit(TESTE, (0 - self.scroll, 315))
        self.sprites.draw(self.window)
        self.sprites.update()
        self.meele_sprites.draw(self.window)
        self.meele_sprites.update()

    def update(self):
        self.player.movimenta_player()
        key = pygame.key.get_pressed()
        # Movimentação (e limitação do movimento) do player
        if self.player.ataque_forte == False and self.player.ataque_fraco == False and self.player.defendendo == False:
            # Movimentação de andar para a esquerda
            if key[pygame.K_a]:
                if self.scroll == 0:
                    self.player.rect.x -= 1
                elif self.player.rect.x <= 511 or self.scroll != 0:
                    self.scroll -= 1
                    self.meele.rect.x += 1
                # elif self.scroll == 1000:
                #     self.player.rect.x -= 1
                self.player.andando = True
                self.player.esquerda = True
                self.player.direita = False
            # Movimentação de andar para a direita
            if key[pygame.K_d]:
                # if self.scroll == 1000:
                #     self.player.rect.x += 1
                if self.player.rect.x >= 511 or self.scroll != 0:
                    self.scroll += 1
                    self.meele.rect.x -= 1
                elif self.scroll == 0:
                    self.player.rect.x += 1
                self.player.andando = True
                self.player.direita = True
                self.player.esquerda = False
            # Movimentação de correr para a esquerda
            if key[pygame.K_LSHIFT] and key[pygame.K_a]:
                if self.scroll == 0:
                    self.player.rect.x -= 1
                elif self.player.rect.x <= 511 or self.scroll != 0:
                    self.scroll -= 2
                    self.meele.rect.x += 2
                elif self.scroll == 1000:
                    self.player.rect.x -= 1
                self.player.andando = False
                self.player.correndo = True
            # Movimentação de correr para a direita
            if key[pygame.K_LSHIFT] and key[pygame.K_d]: 
                if self.scroll == 1000:
                    self.player.rect.x += 1
                elif self.player.rect.x >= 511 or self.scroll != 0:
                    self.scroll += 2
                    self.meele.rect.x -= 2
                elif self.scroll == 0:
                    self.player.rect.x += 1
                self.player.andando = False
                self.player.correndo = True
            # Movimentação de pulo
            if key[pygame.K_SPACE]:
                if self.player.pulos < self.player.max_pulos:
                    self.player.gravidade = -10
                    self.player.pulos += 1
                    self.player.pulando = True
                    self.player.andando = False
                    self.player.correndo = False
                    self.player.parado = False
            # Ação de defesa
            if key[pygame.K_c]:
                self.player.defendendo = True
                if self.player.parado == True:
                    self.player.parado = False
        # Movimentação de combate
        if self.player.pulando == False:
            # Ataque forte
            if key[pygame.K_q]:
                if self.player.max_atq_forte < self.player.max_ataques:
                    self.player.ataque_forte = True
                    self.player.max_atq_forte += 1
                    if pygame.sprite.collide_mask(self.player, self.meele):
                        self.meele.vida -= 1
                if self.player.parado == True:
                    self.player.parado = False
            # Ataque fraco
            if key[pygame.K_e]:
                if self.player.max_atq_fraco < self.player.max_ataques:
                    self.player.ataque_fraco = True
                    self.player.max_atq_fraco += 1
                    if pygame.sprite.collide_mask(self.player, self.meele):
                        self.meele.vida -= 1
                self.player.ataque_fraco = True
                if self.player.parado == True:
                    self.player.parado = False
        # Combate em si ( Condições de vida, dano, etc)
        if self.meele.vida <= 0:
            self.meele.kill()
        if self.scroll < 0:
            self.scroll = 0
        # if self.scroll > 1000:
        #     self.scroll = 1000
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