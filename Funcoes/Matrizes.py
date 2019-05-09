from random import randint

def imprimeLinhaSeparadora(caracter, tamanho):
	"""
	Imprime no terminal uma sequencia, passada por parametro, de caracter
	"""
	print(tamanho * caracter)

def imprimeMatriz(matriz):
	"""imprime uma matrize não formatada"""
	print(matriz)

def imprimeMatrizPorLinha(matriz):
	"""imprime uma matrize linha por linha"""
	for i in range(len(matriz)):
		print(matriz[i])

def imprimeMatrizPorElemento(matriz):
	"""imprime uma matrize elemento por elemento"""
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			print("linha {}, coluna {} = elemento {}".format(i,j,matriz[i][j]))

def imprimeListaComElementosZero(x):
	"""imprime uma lista de tamanho passado pro parametro com elementos zero"""
	lista = []
	for i in range(x):
		lista.append(0)
	print(lista)

def imprimeMatrizComElementosZero(i, j):
	"""Mostra uma matriz com elementos zero, de dimensoes linha x coluna passado por parametro"""
	matriz = []
	for i in range(i):
		matriz.append([0]*j)
	print(matriz)

def imprimeMatrizComDimensaoDefinidaPeloUsuario():
	"""Mostra uma matriz com dimensoes definida pelo usuario com os elementos zero"""
	linhas = int(input("Linhas da matriz: "))
	colunas = int(input("Colunas da matriz: "))
	matriz = []
	for i in range(linhas):
		matriz.append([0]*colunas)

	imprimeMatrizPorLinha(matriz)

def imprimeMatrizCompleta():
	"""Mostra uma matriz com dimensoes e os elementos definidos pelo usuario"""
	linhas = int(input("Linhas da matriz: "))
	colunas = int(input("Colunas da matriz: "))
	matriz = []
	for i in range(linhas):
		matriz.append([0]*colunas)

	for linha in range(len(matriz)):
		for coluna in range(len(matriz)):
			matriz[linha][coluna] = int(input("Informe o elemento da linha {} e coluna {}: ".format(linha, coluna)))

	imprimeMatrizPorLinha(matriz)

def criaMatrizZerada(linha, coluna):
	"""
	Cria uma Matriz de dimensão linha x coluna com valores 0
	"""
	matriz = []
	for i in range(linha):
		matriz.append([0] * coluna)
	
	return matriz

def criaMatrizAleatoria(linha, coluna, valorMin, valorMax):
	"""
    Cria uma Matriz de dimensão linha x coluna com valores aleatorios entre valorMin e valorMax
    """
	matriz = criaMatrizZerada(linha, coluna)
	for i in range(linha):
		for j in range(coluna):
			matriz[i][j] = randint(valorMin, valorMax)
	return matriz

matriz = criaMatrizAleatoria(4, 4, 0, 10)
'''
imprimeMatriz(matriz)
imprimeLinhaSeparadora("*", 30)
imprimeMatrizPorLinha(matriz)
imprimeLinhaSeparadora("*", 30)
imprimeMatrizPorElemento(matriz)
imprimeLinhaSeparadora("*", 30)
imprimeListaComElementosZero(2)
imprimeLinhaSeparadora("*", 30)
imprimeMatrizComDimensaoDefinidaPeloUsuario()
imprimeLinhaSeparadora("*", 30)
imprimeMatrizComElementosZero(2, 2)
imprimeLinhaSeparadora("*", 30)
imprimeMatrizCompleta()
imprimeLinhaSeparadora("*", 30)
'''

nome = input()
print(nome)