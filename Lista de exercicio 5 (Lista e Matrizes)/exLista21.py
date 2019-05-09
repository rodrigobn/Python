"""
21.	Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 
os demais elementos. Escreva ao ﬁnal a matriz obtida.7
"""

from matrizes import *

matriz = criaMatrizAleatoria(5, 5, 0, 20)
matriz2 = criaMatrizZerada(5, 5)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if linha == coluna:
            matriz2[linha][coluna] = 1
        else:
            matriz2[linha][coluna] = 0

imprimeMatrizPorLinha(matriz)
imprimeLinhaSeparadora("-", 30)
imprimeMatrizPorLinha(matriz2)