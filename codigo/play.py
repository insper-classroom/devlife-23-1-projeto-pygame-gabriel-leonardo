from classes.tela_inicial import TelaInicial
from classes.tela_instrucoes import TelaInstrucoes

if __name__ == '__main__':
    tela_atual = TelaInicial()
    while True:
        tela_atual.roda()
        tela_atual = tela_atual.update()