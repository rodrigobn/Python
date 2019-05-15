"""
32. Faca um programa que leia duas matrizes A e B e calcule C = A∗B.
"""

from matrizes import *

matriz1 = criaMatrizAleatoria(3,2,1,4)
matriz2 = criaMatrizAleatoria(2,4,1,4)
matriz3 = criaMatrizZerada(len(matriz1),len(matriz2[0]))
soma = 0
if len(matriz1[0]) == len(matriz2):
	for linha in range(len(matriz1)):
		for coluna in range(len(matriz2[0])):
			for somatorio in range(len(matriz1[0])):
				soma += matriz1[linha][somatorio] * matriz2[somatorio][coluna]
			matriz3[linha][coluna] = soma
			soma = 0

	imprimeLinhaSeparadora('-',20)
	print("Matriz A:")
	imprimeMatrizPorLinha(matriz1)
	imprimeLinhaSeparadora('-',20)
	print("Matriz B:")
	imprimeMatrizPorLinha(matriz2)
	imprimeLinhaSeparadora('-',20)
	print("Matriz A*B:")
	imprimeMatrizPorLinha(matriz3)
else:
	print("Não pode ser multiplicada! Coluna de matriz A é diferente de linhas de matriz B")