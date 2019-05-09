"""
24.	Leia duas matrizes 4x4 e escreva uma terceira com os 
maiores valores de cada posição das matrizes lidas.
"""

from matrizes import *

matriz1 = criaMatrizAleatoria(4, 4, 0, 50)
matriz2 = criaMatrizAleatoria(4, 4, 0, 50)

matriz3 = criaMatrizZerada(len(matriz1), len(matriz2))

for linha in range(len(matriz1)):
    for coluna in range(len(matriz1[0])):
        if matriz1[linha][coluna] > matriz2[linha][coluna]:
            matriz3[linha][coluna] = matriz1[linha][coluna]
        else:
            matriz3[linha][coluna] = matriz2[linha][coluna]

imprimeMatrizPorLinha(matriz1)
imprimeLinhaSeparadora('-', 30)
imprimeMatrizPorLinha(matriz2)
imprimeLinhaSeparadora('-', 30)
imprimeMatrizPorLinha(matriz3)