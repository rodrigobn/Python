"""
1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. 
"""

numero = [1,2,3,4,5]

if numero == []:
	print("lista vazia")
else:
	for indice in range(len(numero)):
		print(numero[indice])