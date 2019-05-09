"""
10 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

"""
vetorA = [1,2,3,4,5,6,7,8,9,10]
vetorB = [11,12,13,14,15,16,17,18,19,20]
vetorC = []

if len(vetorA) == len(vetorB):
	for i in range(len(vetorA)):
		vetorC.append(vetorA[i])
		vetorC.append(vetorB[i])

print(vetorC)