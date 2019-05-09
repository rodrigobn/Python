"""
22.	Leia uma matriz 4 x 4, imprima a matriz e retorne a 
localização (linha e a coluna) do maior valor.
"""
from matrizes import *

matriz = criaMatrizAleatoria(4, 4, 0, 50)
maiorValor = matriz[0][0]
linhaMaiorValor = 0
colunaMaiorValor = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        if matriz[linha][coluna] > maiorValor:
            maiorValor = matriz[linha][coluna]
            linhaMaiorValor = linha
            colunaMaiorValor = coluna

imprimeMatrizPorLinha(matriz)
print("Linha:{}, Coluna:{} esta o maior valor".format(linhaMaiorValor, colunaMaiorValor))