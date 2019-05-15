"""
30. Escreva um programa que transforme uma matriz 4x4 numa matriz triangular
inferior, ou seja, atribuindo zero a todos os elementos acima da diagonal
principal. Imprima a matriz original e a matriz transformada.
"""

from matrizes import *

matriz = criaMatrizAleatoria(4, 4, 0, 9)
matrizTriangularInferior = criaMatrizZerada(4,4)

linhaDiagonal = 0
colunaDiagonal = 0
for linha in range(len(matriz)):
	for coluna in range(len(matriz[0])):
		if linha + coluna > linhaDiagonal + colunaDiagonal:
			matrizTriangularInferior[linha][coluna] = 0
		else:
			matrizTriangularInferior[linha][coluna] = matriz[linha][coluna]
	linhaDiagonal += 1
	colunaDiagonal += 1

imprimeMatrizPorLinha(matrizTriangularInferior)
imprimeLinhaSeparadora('-',30)