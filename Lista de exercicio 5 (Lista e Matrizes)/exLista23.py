"""
23.	Leia uma matriz 5 x 5. Leia também um valor X. 
O programa deverá fazer uma busca desse valor na matriz e, 
ao ﬁnal, escrever a localizacão (linha e coluna) 
ou uma mensagem de “não encontrado”. 
"""

from matrizes import *

matriz = criaMatrizAleatoria(5, 5, 0, 10)
valor = int(input("Valor: "))
linhaValor = []
colunaValor = []

for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        if matriz[linha][coluna] == valor:
            linhaValor.append(linha)
            colunaValor.append(coluna)

if linhaValor == []:
    print("Não encontrado!")
else:
    for i in range(len(linhaValor)):
        print("Linha: {}, Coluna: {} esta localizado o valor: {}".format(linhaValor[i], colunaValor[i], valor))

imprimeMatrizPorLinha(matriz)