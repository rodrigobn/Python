"""
20 - Leia uma matriz 4 x 4, conte e escreva quantos valores 
maiores que 10 ela possui. 
"""
from matrizes import *

matriz = criaMatrizAleatoria(4,4,0,20)
maiorQue10 = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        if matriz[linha][coluna] > 10:
            maiorQue10 += 1

imprimeMatrizPorLinha(matriz)
print("Quantidade de valores maiores que 10:", maiorQue10)