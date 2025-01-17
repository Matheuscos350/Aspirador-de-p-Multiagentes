# -*- coding: utf-8 -*-
"""AspiradorDePo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dLOIkso8El2ZUMX4opLcrrkY4gDukfCo

# ***Código do Aspirador de pó mostrando pelo console.***
"""

import time
from random import randint

agente = "🔘"
limpo = 0

ambiente = [[1,4,0,0,2,0,3],
            [0,0,3,1,0,4,0],
            [0,1,0,0,2,0,0],
            [0,0,2,1,0,1,2],
            [2,0,3,0,3,1,4],
            [0,4,0,0,3,1,4],
            [0,1,1,0,2,3,0]]

def printar(ambiente):
    for secao in ambiente:
        print(secao)
    print(31 * '\n')

def sujaambiente(ambiente):
    for secao in ambiente:
        atual = 0
        for local in secao:
            secao[atual] = randint(0, 7)
            atual += 1
    return ambiente

def aspirador(ambiente):
    for secao in ambiente:
        atual = 0
        for local in secao:
            if local != limpo:
                secao[atual] = agente
                printar(ambiente)
                time.sleep(0.7)
                secao[atual] = limpo
                atual += 1
            else:
                salva = secao[atual]
                secao[atual] = agente
                printar(ambiente)
                secao[atual] = salva
                time.sleep(0.7)
                atual += 1
                continue

    return ambiente

while True:
    printar(aspirador(ambiente))
    ambiente = sujaambiente(ambiente)
    printar(ambiente)
    time.sleep(1)

"""# ***Limpeza do Aspirador de pó gerando imagem do ambiente.***
O código gerará 3 imagens, a situação do ambiente antes da limpeza, a 1° passada do aspirador e a ultima com o ambiente totalmente limpo.
"""

from random import randint
import time
import matplotlib.pyplot as plt

agente = 5
limpo = 0

ambiente = [[1,4,0,0,2,0,3],
            [0,0,3,1,0,4,0],
            [0,1,0,0,2,0,0],
            [0,0,2,1,0,1,2],
            [2,0,3,0,3,1,4],
            [0,4,0,0,3,1,4],
            [0,1,1,0,2,3,0]]

def sujaambiente(ambiente):
    for secao in ambiente:
        for atual in range(len(secao)):
            secao[atual] = randint(0, 4)
    return ambiente

def aspirador(ambiente, before=True):
    if before:
        plt.imshow(ambiente, cmap='viridis', interpolation='nearest')
        plt.title('Antes da Limpeza')
        plt.colorbar()
        plt.show()
    else:
        plt.imshow(ambiente, cmap='viridis', interpolation='nearest')
        plt.title('Depois da Limpeza')
        plt.colorbar()
        plt.show()

    for linha in range(len(ambiente)):
        for coluna in range(len(ambiente[linha])):
            if ambiente[linha][coluna] != limpo:
                ambiente[linha][coluna] = agente
                time.sleep(0.5)
                ambiente[linha][coluna] = limpo
            else:
                salva = ambiente[linha][coluna]
                ambiente[linha][coluna] = agente
                ambiente[linha][coluna] = salva
                time.sleep(0.5)
        if linha == len(ambiente) - 1 and coluna == len(ambiente[linha]) - 1:
            break
    return ambiente

for _ in range(5):  # Run for 5 iterations
    ambiente = aspirador(ambiente, before=True)
    ambiente = sujaambiente(ambiente)
    ambiente = aspirador(ambiente, before=False)
    time.sleep(1)