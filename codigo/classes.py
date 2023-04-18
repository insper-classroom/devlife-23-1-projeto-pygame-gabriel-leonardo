import pygame

class Jogo:
    def __init__(self):
        self.WIDTH = 1024
        self.HEIGHT =  720 
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
    def roda(self):
        self.desenha()
        pygame.display.update()
    
    def update(self):
        pass

class TelaInicial(Jogo):
    def desenha(self):
        self.window.fill((0, 0, 0))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return TelaJogo()
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
