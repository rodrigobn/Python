"""
13 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

"""
import random

idades = []
alturas = []

alturaTotal = mediaAltura = contadorMais13 = 0

# Povoa a lista randomicamente
for i in range(30):
	idades.append(random.randrange(10,70))
	alturas.append(random.randrange(100, 200))

# Calcula a soma total das alturas
for i in range(len(alturas)):
	alturaTotal += alturas[i]

# Calcula a media das alturas
if len(alturas) > 0:
	mediaAltura += alturaTotal/len(alturas)

# Conta quantos alunos tem mais de 13 anos com altura menor que a media
for i in range(len(idades)):
	if idades[i] > 13:
		if alturas[i] < mediaAltura:
			contadorMais13 += 1

print(contadorMais13)