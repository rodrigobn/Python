"""
2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.  
"""

lista = [1,2,3,4,5,6,7,8,9,10]

if lista == []:
	print("Lista vazia")
else:
	for i in range(len(lista)-1, -1, -1):
		print(lista[i])
