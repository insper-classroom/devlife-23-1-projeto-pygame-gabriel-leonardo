import pygame
from classes.jogo import Jogo
from classes.player import Player
from classes.inimigos import InimigoMeele
from classes.plataforma import *
from constantes import *

class TelaJogo(Jogo):
    def __init__(self):
        
        super().__init__()
        self.player = Player()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)

        self.meele = InimigoMeele()
        self.meele_sprites = pygame.sprite.Group()
        self.meele_sprites.add(self.meele)

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

        
        # self.plataforma = Plataforma2(2528, 509)
        # self.plataforma_sprites.add(self.plataforma)

        # self.plataforma = Plataforma3(3008, 381)
        # self.plataforma_sprites.add(self.plataforma)

        # for i in range (2):
        #     self.plataforma = Plataforma(2048 + (i * 480), 509)
        #     self.plataforma_sprites.add(self.plataforma)
        # for i in range (2):
        #     self.plataforma = Plataforma(3008 + (i * 480), 381)
        #     self.plataforma_sprites.add(self.plataforma)
        # for i in range (0, 3, 2):
        #     self.plataforma = Plataforma(4448 + (i * 480), 509)
        #     self.plataforma_sprites.add(self.plataforma)
        # for i in range(0, 8, 7):
        #     self.plataforma = Plataforma(4928 + (i * 480), 381)
        #     self.plataforma_sprites.add(self.plataforma)
        # for i in range (0, 3, 2):
        #     self.plataforma = Plataforma(6848 + (i * 480), 509)
        #     self.plataforma_sprites.add(self.plataforma)
        # for i in range (2):
        #     self.plataforma = Plataforma(9728 + (i * 480), 509)
        #     self.plataforma_sprites.add(self.plataforma)
            
        # for i in range (0, 11, 5):
        #     self.quina = Quina_Esquerda(2048 + (i * 480), 509)
        #     self.plataforma_sprites.add(self.quina)
        # for i in range (0, 5, 4):
        #     self.quina = Quina_Esquerda(3008 + (i * 480), 381)
        #     self.plataforma_sprites.add(self.quina)
        # for i in range (0, 5, 4):
        #     self.quina = Quina_Esquerda(7808 + (i * 480), 509)
        #     self.plataforma_sprites.add(self.quina)
        # self.quina = Quina_Esquerda(8288, 381)
        # self.plataforma_sprites.add(self.quina)

        # for i in range(0, 4, 3):
        #     self.plataforma = Quina_Direita(3488 + 480 - 64 + (i * 480), 381)
        #     self.plataforma_sprites.add(self.plataforma)
        # self.quina = Quina_Direita(8288 + 480 - 64, 381)
        # for i in range(0, 4, 3):
        #     self.plataforma = Quina_Direita(5408 + 480 - 64 + (i * 480), 509)
        #     self.plataforma_sprites.add(self.plataforma)
        # self.plataforma = Quina_Direita(8288 + 480 - 64, 381)
        # self.plataforma_sprites.add(self.quina)

        self.BG_1 = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/bg_1.png').convert_alpha()
        self.BG_1 = pygame.transform.scale(self.BG_1, (self.WIDTH, self.HEIGHT))
        self.BG_2 = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/bg_2.png').convert_alpha()
        self.BG_2 = pygame.transform.scale(self.BG_2, (self.WIDTH, self.HEIGHT))
        self.BG_3 = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/bg_3.png').convert_alpha()
        self.BG_3 = pygame.transform.scale(self.BG_3, (self.WIDTH, self.HEIGHT))

        self.jogo = Jogo()

        self.rect_surface = pygame.Surface((1024, 720))
        self.rect_surface.fill(BRANCO)



    def desenha(self):
        for i in range(7):
           self.window.blit(self.BG_1, ((0 - self.scroll* 0.5) + i * 1024, 0))
        for i in range(9):
           self.window.blit(self.BG_2, ((0 - self.scroll * 0.7) + i * 1024, 0))
        for i in range(12):
            self.window.blit(self.BG_3,(((0 - self.scroll) + i * 1024), 0))

        self.meele_sprites.draw(self.window)
        self.meele_sprites.update()
        self.sprites.draw(self.window)
        self.plataforma_sprites.draw(self.window)
        
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

        self.calc_fps()
        if self.dicionario['show_fps']:
            imagem_fps = FONTE_TEXTO.render(f'FPS:{self.fps:.2f}', True, (255, 255, 255))
            self.window.blit(imagem_fps, (5,5))

        self.sprites.update()

    def update(self):
        self.player.movimenta_player()
        key = pygame.key.get_pressed()

        # Colisão do player com a plataforma
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
                
        # Movimentação (e limitação do movimento) do player
        if self.player.ataque_forte == False and self.player.ataque_fraco == False and self.player.defendendo == False:
            # Movimentação de andar para a esquerda
            if key[pygame.K_a]:
                if self.scroll == 0:
                    self.player.rect.x -= 1
                elif self.player.rect.x <= 511 or self.scroll != 11000 and self.scroll != 0:
                    if self.colidindo_esquerda == False:
                        self.meele.rect.x += 1
                        self.scroll -= 1
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
                        self.meele.rect.x -= 1
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
                            self.meele.rect.x += 2
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
                            self.meele.rect.x -= 2
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
                            self.meele.vida -= 1
                            self.meele.meele_dano = True
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
                            self.meele.meele_dano = True
                            self.meele.vida -= 1
                        else:    
                            self.meele.meele_dano = False
                    self.player.ataque_fraco = True
                    if self.player.parado == True:
                        self.player.parado = False
        # Combate em si ( Condições de vida, dano, etc)
        if self.meele.vida <= 0:
            self.meele.meele_dano = False
            self.meele.meele_morrendo = True

        # Verificacao da borda do scroll(extra para que nao haja bugs):
        if self.scroll < 0:
            self.scroll = 0
        if self.scroll > 11000:
            self.scroll = 11000

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
        return self 