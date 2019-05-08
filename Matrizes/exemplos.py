"""
Matrizes
"""

matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

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
	"""Mostra uma matriz com elementos zero de dimensoes linha x coluna passado por parametro"""
	matriz = []
	for i in range(i):
		matriz.append([0]*j)
	print(matriz)

#inicializa matriz vazia com dimensoes definida pelo usuario com elementos zero
def imprimeMatrizComDimensaoDefinidaPeloUsuario():
	"""Mostra uma matriz com dimensoes definida pelo usuario com os elementos zero"""
	linhas = int(input("Linhas da matriz: "))
	colunas = int(input("Colunas da matriz: "))
	matriz = []
	for i in range(linhas):
		matriz.append([0]*colunas)

	imprimeMatrizPorLinha(matriz)

#inicializa matriz vazia com dimensoes definida pelo usuario com elementos definidos pelo usuario
def imprimeMatrizCompleta():
	"""Mostra uma matriz com dimensoes e os elementos definidos pelo usuario"""
	linhas = int(input("Linhas da matriz: "))
	colunas = int(input("Colunas da matriz: "))
	matriz2 = []
	for i in range(linhas):
		matriz2.append([0]*colunas)

	for linha in range(len(matriz2)):
		for coluna in range(len(matriz2)):
			matriz2[linha][coluna] = int(input("Informe o elemento da linha {} e coluna {}: ".format(linha, coluna)))

	imprimeMatrizPorLinha(matriz2)


imprimeMatriz(matriz)