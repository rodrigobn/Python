"""
28.	Leia uma matriz de 3 x 3 elementos. 
Calcule a soma dos elementos que estão na diagonal secundária. 
"""
from matrizes import *

matriz = criaMatrizAleatoria(3, 3, 0, 20)
soma = 0
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        if linha + coluna == len(matriz) - 1:
            soma += matriz[linha][coluna]

imprimeMatrizPorLinha(matriz)
print(soma)