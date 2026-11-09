import random
import numpy as np
#Inicialmente, definiremos a lista do jogador e do computador, e a lista das posições do 3x3.
jogador = []
maquina = []
posicoes = [1,2,3,4,5,6,7,8,9]
v = [
    [1,2,3],[4,5,6],[7,8,9], #Linha
    [1,4,7],[2,5,8],[3,6,9], # Coluna
    [1,4,9],[3,5,7] # Diagonal
]
tabuleiro = [' ' for _ in range(1,10)]

#Função que verifica a vitória
def vitoria(lista):
    global v   
    for i in range(len(v)):
        c = set(v[i]).issubset(set(lista))
        if c == True:
            return True
    else: 
        return False

def print_tabuleiro():
    global tabuleiro
    linha1 = f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} "
    linha2 = f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} "
    linha3 = f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} "
    print("\n" + linha1)
    print("---|---|---")
    print(linha2)
    print("---|---|---")
    print(linha3 + "\n")
#Estrutura do jogo
while len(posicoes) > 0:
    try:
        p = int(input('Insira a posição:'))
        jogador.append(p)
        posicoes.remove(p)
        tabuleiro[p-1] = "X"
    except:
        print('Você deve escolher uma posição válida.')
        continue
    if vitoria(jogador) == True:
            print('Vitória do Jogador.')
            print_tabuleiro()
            break
    try:
        m = random.choice(posicoes)
        maquina.append(m)
        posicoes.remove(m)
        tabuleiro[m-1] = "O"
        print_tabuleiro()
    except:
        pass
    if vitoria(maquina) == True:
        print('Vitória da maquina')
        break
if len(posicoes) == 0 and vitoria(jogador) == False and vitoria(maquina) == False:
    print('Empate')
#Parte gráfica no terminal
#Como podemos criar a matriz?
