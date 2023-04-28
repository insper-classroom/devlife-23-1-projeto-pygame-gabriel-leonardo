import pygame
from jogo import Jogo
from classes.player import Player
from classes.inimigos import InimigoMeele
from classes.plataforma import Plataforma


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
        for i in range (8):
            self.plataforma = Plataforma(2048 + (i * 480), 637 - 128)
            self.plataforma_sprites.add(self.plataforma)

        self.BG_1 = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/bg_1.png').convert_alpha()
        self.BG_1 = pygame.transform.scale(self.BG_1, (self.WIDTH, self.HEIGHT))
        self.BG_2 = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/bg_2.png').convert_alpha()
        self.BG_2 = pygame.transform.scale(self.BG_2, (self.WIDTH, self.HEIGHT))
        self.BG_3 = pygame.image.load('../assets/backgrounds/TelaJogo/Background_Parallax/bg_3.png').convert_alpha()
        self.BG_3 = pygame.transform.scale(self.BG_3, (self.WIDTH, self.HEIGHT))

        
    def desenha(self):
        self.window.fill((255, 255, 255))

        for i in range(10):
           self.window.blit(self.BG_1, ((0 - self.scroll* 0.5) + i * 1024, 0))
        for i in range(10):
           self.window.blit(self.BG_2, ((0 - self.scroll * 0.7) + i * 1024, 0))
        for i in range(10):
           self.window.blit(self.BG_3, ((0 - self.scroll) + i * 1024, 0))


        self.meele_sprites.draw(self.window)
        self.meele_sprites.update()
        self.sprites.draw(self.window)
        self.sprites.update()
        self.plataforma_sprites.draw(self.window)
        
        


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
                    for plat in self.plataforma_sprites:
                        plat.rect.x += 1
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
                    for plat in self.plataforma_sprites:
                        plat.rect.x -= 1
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
                    for plat in self.plataforma_sprites:
                        plat.rect.x += 2
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
                    for plat in self.plataforma_sprites:
                        plat.rect.x -= 2
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
                        self.meele.meele_dano = True
            #if not pygame.sprite.collide_mask(self.player, self.meele):
            #    self.meele.meele_dano = False
                        
                if self.player.parado == True:
                    self.player.parado = False
            # Ataque fraco
            if key[pygame.K_e]:
                if self.player.max_atq_fraco < self.player.max_ataques:
                    self.player.ataque_fraco = True
                    self.player.max_atq_fraco += 1
                    if pygame.sprite.collide_mask(self.player, self.meele):
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