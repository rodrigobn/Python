"""
7 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

"""

vetor = [5, 8, 6, 7, 2]
soma = 0
multiplicacao = 1

for i in range(len(vetor)):
	soma += vetor[i]
	multiplicacao *= vetor[i]
	print(vetor[i])

print("Soma = {}, Multiplicação = {}".format(soma, multiplicacao))