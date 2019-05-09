"""
15 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

a) Mostre a quantidade de valores que foram lidos;
b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d) Calcule e mostre a soma dos valores;
e) Calcule e mostre a média dos valores;
f) Calcule e mostre a quantidade de valores acima da média calculada;
g) Calcule e mostre a quantidade de valores abaixo de sete;
h) Encerre o programa com uma mensagem;

"""

valores = []

nota = float(input("Nota: "))
while nota != -1:
	if nota < 0:
		while nota < 0:
			nota = float(input("Digite uma nota positiva: "))
			if nota == -1:
				break
		if nota == -1:
			break
		else:
			valores.append(nota)
	else:
		valores.append(nota)
	
	if nota == -1:
		break
	else:
		nota = float(input("Nota: "))

print("quantidade de valores que foram lidos:", len(valores))
print("todos os valores na ordem em que foram informados:",valores)

soma = media = 0
print("valores na ordem inversa à que foram informados, um abaixo do outro")
for i in range(len(valores)-1, -1, -1):
	print(valores[i])
	soma += valores[i]
print("a soma dos valores:",soma)

if len(valores) > 0:
	media = soma/len(valores)
print("a média dos valores:",media)

contadorAcima = contadorAbaixo = 0
for i in range(len(valores)):
	if valores[i] > media:
		contadorAcima += 1
	elif valores[i] < 7:
		contadorAbaixo += 1

print("quantidade de valores acima da média calculada:", contadorAcima)
print("quantidade de valores abaixo de sete:",contadorAbaixo)