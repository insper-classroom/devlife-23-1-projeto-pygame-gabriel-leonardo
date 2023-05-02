import pygame
from classes.jogo import Jogo
from classes.player import Player
from classes.inimigos import InimigoMeele, InimigoRanged
from classes.tela_win import TelaWin
from classes.plataforma import *
from constantes import *

class TelaJogo(Jogo):
    def __init__(self):
        super().__init__()
        # Inicia as sprites
        self.player = Player()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)

        # Desenha as plataformas
        self.plataforma_sprites = pygame.sprite.Group()
        self.plataforma = Plataforma1_1(2048, 509)
        self.plataforma_sprites.add(self.plataforma)
        self.plataforma = Plataforma1_2(2528, 381)
        self.plataforma_sprites.add(self.plataforma)
        self.plataforma = Plataforma2_1(4448, 509)
        self.plataforma_sprites.add(self.plataforma)
        self.plataforma = Plataforma1_2(4928, 381)
        self.plataforma_sprites.add(self.plataforma)
        self.plataforma = Plataforma2_1(9728, 509)
        self.plataforma_sprites.add(self.plataforma)
        self.plataforma = Plataforma1_2(10208, 381)
        self.plataforma_sprites.add(self.plataforma)

        self.meele_sprites = pygame.sprite.Group()
        self.meele = InimigoMeele(2225, 382, 2080, 2510)
        self.meele_sprites.add(self.meele)
        self.meele = InimigoMeele(5105, 254, 4940, 5400)
        self.meele_sprites.add(self.meele)
        self.meele = InimigoMeele(9885, 382, 9740, 10200)
        self.meele_sprites.add(self.meele)
        self.meele = InimigoMeele(8000, 510, 7700, 8150)
        self.meele_sprites.add(self.meele)

        self.ranged_sprites = pygame.sprite.Group()
        self.ranged = InimigoRanged(4250, 510)
        self.ranged_sprites.add(self.ranged)
        self.ranged = InimigoRanged(5800, 382)
        self.ranged_sprites.add(self.ranged)
        self.ranged = InimigoRanged(7000, 510)
        self.ranged_sprites.add(self.ranged)
        self.ranged = InimigoRanged(10550, 254)
        self.ranged_sprites.add(self.ranged)

        # Inicia o background
        self.BG_1 = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/bg_1.png').convert_alpha()
        self.BG_1 = pygame.transform.scale(self.BG_1, (self.WIDTH, self.HEIGHT))
        self.BG_2 = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/bg_2.png').convert_alpha()
        self.BG_2 = pygame.transform.scale(self.BG_2, (self.WIDTH, self.HEIGHT))
        self.BG_3 = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/bg_3.png').convert_alpha()
        self.BG_3 = pygame.transform.scale(self.BG_3, (self.WIDTH, self.HEIGHT))

        # Variáveis
        self.jogo = Jogo()
        self.rect_surface = pygame.Surface((1024, 720))
        self.rect_surface.fill(BRANCO)
        self.tempo = pygame.time.get_ticks()

    def desenha(self):
        # Desenha o background
        for i in range(7):
           self.window.blit(self.BG_1, ((0 - self.scroll* 0.5) + i * 1024, 0))
        for i in range(9):
           self.window.blit(self.BG_2, ((0 - self.scroll * 0.7) + i * 1024, 0))
        for i in range(12):
            self.window.blit(self.BG_3,(((0 - self.scroll) + i * 1024), 0))

        # Desenha os sprites
        self.meele_sprites.draw(self.window)
        self.sprites.draw(self.window)
        self.plataforma_sprites.draw(self.window)
        self.ranged_sprites.draw(self.window)
        
        # Muda a tela com base na stamina
        if self.player.stamina == 6:
            self.rect_surface.set_alpha(10)
        elif self.player.stamina == 5:
            self.rect_surface.set_alpha(15)
        elif self.player.stamina == 4:
            self.rect_surface.set_alpha(20)
        elif self.player.stamina == 3:
            self.rect_surface.set_alpha(25)
        elif self.player.stamina <= 2:
            self.rect_surface.set_alpha(30)
        else:
            self.rect_surface.set_alpha(0)
        self.window.blit(self.rect_surface, (0, 0))

        # Calcula e desenha o FPS
        self.calc_fps()
        if self.dicionario['show_fps']:
            imagem_fps = FONTE_TEXTO.render(f'FPS:{self.fps:.2f}', True, (255, 255, 255))
            self.window.blit(imagem_fps, (5,5))

        # Atualiza os sprites
        self.meele_sprites.update()
        self.sprites.update()
        self.plataforma_sprites.update()
        self.ranged_sprites.update()

    def update(self):
        # Função que mexe o player quando a tela não se mexe e o player se mexe
        self.player.movimenta_player()
        # Função que verifica se uma tecla esta sendo clicada
        key = pygame.key.get_pressed()

        # Variável da colisão do player com a plataforma
        self.colidindo_direita = False
        self.colidindo_esquerda = False
        player_x_direita = self.scroll - 850

        # Define uma variável para a posição esquerda do player, já que ele se move para a direita e o background é desenhado em sentido contrário:
        if self.scroll < 4000: 
            player_x_esquerda = self.scroll - 1980
        if self.scroll > 4000:
            player_x_esquerda = self.scroll - 4370
        if self.scroll > 5000:
            player_x_esquerda = self.scroll - 4850
        if self.scroll > 10000:
            player_x_esquerda = self.scroll - 9670
        if self.scroll > 10500:
            player_x_esquerda = self.scroll - 10150

        # Verifica a colisão entre o player e as plataformas
        for plataformas in self.plataforma_sprites:
            if pygame.sprite.collide_mask(self.player, plataformas):
                if self.player.rect.y < plataformas.rect.top: 
                    self.player.rect.bottom = plataformas.rect.top
                    self.player.index_pulando = 0
                    self.player.pulos = 0
                    self.player.pulando = False
                    self.player.parado = True
                if self.player.rect.y > plataformas.rect.top:
                    if self.player.direita and player_x_direita > plataformas.rect.x:
                        self.colidindo_direita = True
                    elif self.player.esquerda and player_x_esquerda < plataformas.rect.right:
                        self.colidindo_esquerda = True
                    else:
                        self.colidindo_direita = False
                        self.colidindo_esquerda = False

        # Verifica a colisão entre o player e o meele
        for meeles in self.meele_sprites:
            if pygame.Rect.colliderect(self.player.rect, meeles.rect):
                if meeles.meele_ataque2 == False and meeles.meele_ataque3 == False:
                    meeles.meele_ataque1 = True
                if pygame.sprite.collide_mask(meeles, self.player):
                    meeles.colisao = True
                    self.player.vida -= meeles.dano
            else:
                meeles.meele_ataque1 = False
                meeles.meele_ataque3 = False
                meeles.meele_ataque2 = False
            if meeles.meele_dano == True:
                if self.player.ataque_forte == False:
                    meeles.meele_dano = False

        # Se o player estiver na frente do meele, ele muda de direção
        player_x_relacao_inimigo = 500
        for meeles in self.meele_sprites:
            if player_x_relacao_inimigo > meeles.rect.x:
                meeles.meele_direita = True
                meeles.meele_esquerda = False
            else:
                meeles.meele_direita = False
                meeles.meele_esquerda = True
        for rangeds in self.ranged_sprites:
            if player_x_relacao_inimigo > rangeds.rect.x:
                rangeds.ranged_direita = True
                rangeds.ranged_esquerda = False
            else:
                rangeds.ranged_direita = False
                rangeds.ranged_esquerda = True

        # Ranged atirando: 
        self.tempo_passado = pygame.time.get_ticks() - self.tempo
        if self.tempo_passado > 3000:
            self.tempo = pygame.time.get_ticks()
            for rangeds in self.ranged_sprites:
                rangeds.ranged_atirando = True
                if rangeds.ranged_direita:
                    flecha = INIMIGO_RANGED_FLECHA
                    self.window.blit(flecha, (rangeds.rect.right , rangeds.rect.y + 20))
                    flecha.get_rect().x += 1
                    
                elif rangeds.ranged_esquerda:
                    flecha = pygame.transform.flip(INIMIGO_RANGED_FLECHA, True, False)
                    self.window.blit(flecha, (rangeds.rect.left, rangeds.rect.y + 20))
                    flecha.get_rect().x -= 1

        # Movimentação (e limitação do movimento) do player
        if self.player.vivo == True:
            if self.player.ataque_forte == False and self.player.ataque_fraco == False and self.player.defendendo == False:

                # Movimentação de andar para a esquerda
                if key[pygame.K_a]:
                    if self.scroll == 0:
                        self.player.rect.x -= 1
                    elif self.player.rect.x <= 511 or self.scroll != 11000 and self.scroll != 0:
                        if self.colidindo_esquerda == False:
                            self.scroll -= 1
                            player_x_relacao_inimigo -= 1
                            for meeles in self.meele_sprites:
                                meeles.rect.x += 1
                            for rangeds in self.ranged_sprites:
                                rangeds.rect.x += 1
                            for plat in self.plataforma_sprites:
                                plat.rect.x += 1
                    elif self.scroll == 11000:
                        self.player.rect.x -= 1
                    self.player.andando = True
                    self.player.esquerda = True
                    self.player.direita = False

                # Movimentação de andar para a direita
                if key[pygame.K_d]:
                    if self.scroll == 11000:
                        self.player.rect.x += 1
                    elif self.player.rect.x >= 511 or self.scroll != 11000 and self.scroll != 0:
                        if self.colidindo_direita == False:
                            self.scroll += 1
                            player_x_relacao_inimigo += 1
                            for meeles in self.meele_sprites:
                                meeles.rect.x -= 1
                            for rangeds in self.ranged_sprites:
                                rangeds.rect.x -= 1
                            for plat in self.plataforma_sprites:
                                plat.rect.x -= 1 
                    elif self.scroll == 0:
                        self.player.rect.x += 1
                    self.player.andando = True
                    self.player.direita = True
                    self.player.esquerda = False
                # Movimentação de correr para a esquerda
                if self.player.stamina > 2:
                    if key[pygame.K_LSHIFT] and key[pygame.K_a]:
                        if self.scroll == 0:
                            self.player.rect.x -= 1
                        elif self.player.rect.x <= 511 or self.scroll != 11000 and self.scroll != 0:
                            if self.colidindo_esquerda == False:
                                self.scroll -= 2
                                player_x_relacao_inimigo -= 2
                                for meeles in self.meele_sprites:
                                    meeles.rect.x += 2
                                for rangeds in self.ranged_sprites:
                                    rangeds.rect.x += 2
                                for plat in self.plataforma_sprites:
                                    plat.rect.x += 2
                        elif self.scroll == 11000:
                            self.player.rect.x -= 1
                        self.player.andando = False
                        self.player.correndo = True
                    # Movimentação de correr para a direita
                    if key[pygame.K_LSHIFT] and key[pygame.K_d]:
                        if self.scroll == 11000:
                            self.player.rect.x += 1
                        elif self.player.rect.x >= 511 or self.scroll != 11000 and self.scroll != 0:
                            if self.colidindo_direita == False:
                                self.scroll += 2
                                player_x_relacao_inimigo += 2
                                for meeles in self.meele_sprites:
                                    meeles.rect.x -= 2
                                for rangeds in self.ranged_sprites:
                                    rangeds.rect.x -= 2
                                for plat in self.plataforma_sprites:
                                    plat.rect.x -= 2
                        elif self.scroll == 0:
                            self.player.rect.x += 1
                        self.player.andando = False
                        self.player.correndo = True
                    # Movimentação de pulo
                    if key[pygame.K_SPACE]:
                        if self.player.pulos < self.player.max_pulos:
                            self.player.stamina -= 1
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
                    if self.player.stamina >= 2:
                        if self.player.max_atq_forte < self.player.max_ataques:
                            self.player.stamina -= 2
                            self.player.ataque_forte = True
                            self.player.max_atq_forte += 1
                            if self.dicionario['sons']:
                                pygame.mixer.music.load('../assets/backgrounds/TelaJogo/Background_Parallax/sfx/q.mp3')
                                pygame.mixer.music.set_volume(0.5)
                                pygame.mixer.music.play()
                            if pygame.sprite.collide_mask(self.player, self.meele):
                                if self.dicionario['sons']:
                                    pygame.mixer.music.load('../assets/backgrounds/TelaJogo/Background_Parallax/sfx/q_dano.mp3')
                                    pygame.mixer.music.set_volume(0.5)
                                    pygame.mixer.music.play()
                                for meeles in self.meele_sprites:
                                    meeles.vida -= 1
                                    meeles.meele_dano = True

                #if not pygame.sprite.collide_mask(self.player, self.meele):
                #    self.meele.meele_dano = False
                        if self.player.parado == True:
                            self.player.parado = False
                # Ataque fraco
                if key[pygame.K_e]:
                    if self.player.stamina >= 1:
                        if self.player.max_atq_fraco < self.player.max_ataques:
                            self.player.stamina -= 1
                            self.player.ataque_fraco = True
                            if self.dicionario['sons']:
                                pygame.mixer.music.load('../assets/backgrounds/TelaJogo/Background_Parallax/sfx/e.mp3')
                                pygame.mixer.music.set_volume(0.5)
                                pygame.mixer.music.play()
                            self.player.max_atq_fraco += 1
                            if pygame.sprite.collide_mask(self.player, self.meele):
                                if self.dicionario['sons']:
                                    pygame.mixer.music.load('../assets/backgrounds/TelaJogo/Background_Parallax/sfx/e_dano.mp3')
                                    pygame.mixer.music.set_volume(0.5)
                                    pygame.mixer.music.play()
                                for meeles in self.meele_sprites:
                                    meeles.meele_dano = True
                                    meeles.vida -= 1
                        self.player.ataque_fraco = True
                        if self.player.parado == True:
                            self.player.parado = False
        # Combate em si ( Condições de vida, dano, etc)
            for meeles in self.meele_sprites:
                if meeles.vida <= 0:
                    meeles.meele_dano = False
                    meeles.meele_morrendo = True
            if self.player.vida <= 0:
                self.player.morrendo = True
                self.player.vivo = False

        # Verificacao da borda do scroll (verificação extra para que nao haja bugs):
        if self.scroll < 0:
            self.scroll = 0
        if self.scroll > 11000:
            self.scroll = 11000
        if self.player.rect.x == 950:
            return TelaWin()
        
        # Verifica o evento, se for de sair do jogo, sai, se for de uma tecla pressionada para cima, cancela o movimento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.USEREVENT:
                if self.player.stamina < 10:
                    self.player.stamina += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    from classes.tela_gameover import TelaGameOver
                    return TelaGameOver()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.player.andando = False
                    self.player.parado = True
                    self.player.correndo = False
                if event.key == pygame.K_LSHIFT:
                    self.player.correndo = False
            if self.player.index_morrendo == 5:
                from classes.tela_gameover import TelaGameOver
                return TelaGameOver()
        return self 