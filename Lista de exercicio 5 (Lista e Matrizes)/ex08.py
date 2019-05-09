"""
8 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

"""

idades = []
alturas = []

for i in range(5):
	idade = int(input("Idade: "))
	if idade <= 0:
		while idade <= 0:
			idade = int(input("Digite uma idade valida: "))
	idades.append(idade)
	altura = float(input("Altura: "))
	if altura <= 0:
		while altura <= 0:
			altura = float(input("Digite uma altura valida: "))
	alturas.append(altura)

for i in range(len(idades)-1, -1, -1):
	print("Idade =", idades[i])
	print("Altura =", alturas[i])