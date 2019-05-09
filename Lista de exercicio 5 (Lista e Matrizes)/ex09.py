"""
9 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

"""
vetorA = [1,2,3,4,5,6,7,8,9,10]
soma = 0

for i in range(len(vetorA)):
	soma += vetorA[i]**2

print(soma)