"""
31. Faça um programa que leia duas matrizes 2 x 2 com valores reais. Ofereça ao
usuário um menu de opções: (a) somar as duas matrizes (b) subtrair a primeira
matriz da segunda (c) adicionar uma constante `as duas matrizes (d) imprimir
as matrizes 

Nas duas primeiras opções uma terceira matriz deve ser criada. 
Na terceira opção o valor da constante deve ser lido e o resultado da adição da
constante deve ser armazenado na própria matriz.
"""

from matrizes import *

matriz1 = criaMatrizAleatoria(2,2,0,9)
matriz2 = criaMatrizAleatoria(2,2,0,9)
matriz3 = criaMatrizZerada(2,2)
menu = ""

while menu != 'e':
	menu = input("""
	Selecione uma das opções:
	(a) Somar as duas matrizes 
	(b) Subtrair a primeira matriz da segunda 
	(c) Adicionar uma constante as duas matrizes 
	(d) Imprimir as matrizes
	(e) Sair
	""")

	while menu != 'a' and menu != 'b' and menu != 'c' and menu != 'd' and menu != 'e':
		menu = input("""
	Selecione uma das opções:
	(a) Somar as duas matrizes 
	(b) Subtrair a primeira matriz da segunda 
	(c) Adicionar uma constante as duas matrizes 
	(d) Imprimir as matrizes
	(e) Sair
	""")

	if menu == 'a':
		for linha in range(len(matriz1)):
			for coluna in range(len(matriz1[0])):
				matriz3[linha][coluna] = matriz1[linha][coluna] + matriz2[linha][coluna]

	elif menu == 'b':
		for linha in range(len(matriz1)):
			for coluna in range(len(matriz1[0])):
				matriz3[linha][coluna] = matriz1[linha][coluna] - matriz2[linha][coluna]

	elif menu == 'c':
		constante = int(input('Digite a constante: '))
		for linha in range(len(matriz1)):
			for coluna in range(len(matriz1[0])):
				matriz1[linha][coluna] += constante
				matriz2[linha][coluna] += constante

	elif menu == 'd':
		print("Matriz 1:")
		imprimeMatrizPorLinha(matriz1)
		imprimeLinhaSeparadora('-',30)
		print("Matriz 2:")
		imprimeMatrizPorLinha(matriz2)
		imprimeLinhaSeparadora('-',30)
		print("Matriz Resultado:")
		imprimeMatrizPorLinha(matriz3)
		matriz3 = criaMatrizZerada(len(matriz1),len(matriz1[0]))