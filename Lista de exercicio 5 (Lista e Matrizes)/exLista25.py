"""
25.	Gerar e imprimir uma matriz de tamanho 10 x 10, 
onde seus elementos são da forma: 

a.	A[i][j] = 2i + 7j −2 se i < j; 
b.	A[i][j] = 3i**2 −1 se i = j; 
c.	A[i][j] = 4i3 −5j2 + 1 se i > j. 
"""
from matrizes import *

matriz = []
for linha in range(10):
    matriz.append([0] * 10)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        if linha < coluna:
            matriz[linha][coluna] = 2*linha + 7*coluna - 2
        elif linha == coluna:
            matriz[linha][coluna] = (3*linha)**2 - 1
        else:
            matriz[linha][coluna] = (4*linha)**3 - (5*coluna)**2 + 1

imprimeMatrizPorLinha(matriz)