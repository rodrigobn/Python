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

def criaDefinicaoDeMatrizVisual(linha, coluna):
	"""
  Cria a definição matematica de uma Matriz de dimensão i x j com valores Aij
  """
	matriz = criaMatrizZerada(linha, coluna)
	for i in range(linha):
		for j in range(coluna):
			matriz[i][j] = "{}{}".format(i, j)
	return matriz

def criaMatrizTransposta(matriz):
	"""
  Cria uma matriz nova a partir de outra matriz, trocando linha por coluna
  """
	matrizTransposta = criaMatrizZerada(3, 3)

	for linha in range(len(matrizTransposta)):
		for coluna in range(len(matrizTransposta[0])):
			matrizTransposta[linha][coluna] = matriz[coluna][linha]
	
	return matrizTransposta

def criaMatrizTriangularInferior(matriz):
	"""
  Cria uma matriz nova a partir de outra matriz zerando todos os elementos acima da diagonal principal
  """
	matrizTriangularInferior = criaMatrizZerada(len(matriz),len(matriz[0]))

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
	return matrizTriangularInferior

def criaMatrizTriangularSuperior(matriz):
	"""
  Cria uma matriz nova a partir de outra matriz zerando todos os elementos abaixo da diagonal principal
  """
	matrizTriangularSuperior = criaMatrizZerada(len(matriz),len(matriz[0]))

	linhaDiagonal = 0
	colunaDiagonal = 0
	for linha in range(len(matriz)):
		for coluna in range(len(matriz[0])):
			if linha + coluna < linhaDiagonal + colunaDiagonal:
				matrizTriangularSuperior[linha][coluna] = 0
			else:
				matrizTriangularSuperior[linha][coluna] = matriz[linha][coluna]
		linhaDiagonal += 1
		colunaDiagonal += 1
	return matrizTriangularSuperior

