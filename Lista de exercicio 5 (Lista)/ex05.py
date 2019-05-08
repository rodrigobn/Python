"""
5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.  
"""

vetor = []
vetorPar = []
vetorImpar = []

for i in range(1, 11):
	numero = int(input("Numero {}: ".format(i)))
	
	if numero <= 0:
		while numero <= 0:
			numero = int(input("Numero {}: ".format(i)))

	if numero % 2 == 0:
		vetorPar.append(numero)
	else:
		vetorImpar.append(numero)

	vetor.append(numero)

print("Lista dos numeros: {}".format(vetor))
print("Lista dos numeros pares: {}".format(vetorPar))
print("Lista dos numeros impares: {}".format(vetorImpar))