from classes import *

tela_atual = TelaInicial()
while True:
    tela_atual.roda()
    tela_atual = tela_atual.update()