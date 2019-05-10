"""
29.	Leia uma matriz de 3 x 3 elementos. 
Calcule e imprima a sua transposta. 
"""

from matrizes import *

matriz = criaMatrizAleatoria(3, 3, 0, 20)
matrizTransposta = criaMatrizZerada(len(matriz), len(matriz[0]))

for linha in range(len(matrizTransposta)):
    for coluna in range(len(matrizTransposta[0])):
        matrizTransposta[linha][coluna] = matriz[coluna][linha]

imprimeMatrizPorLinha(matriz)
imprimeLinhaSeparadora('-',30)
imprimeMatrizPorLinha(matrizTransposta)
