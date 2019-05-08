"""
46 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
"""

nomeAtleta = input("Nome do atleta: ")
if nomeAtleta != "":
	totalSaltos = 0

	salto = float(input("Salto: "))	
	while salto < 0:
		salto = float(input("Salto positivo: "))
	
	maiorSalto = salto
	menorSalto = salto
	totalSaltos += salto
	for i in range(4):
		salto = float(input("Salto: "))
		while salto < 0:
			salto = float(input("Salto positivo: "))
		if salto > maiorSalto:
			maiorSalto = salto
		elif salto < menorSalto:
			menorSalto = salto
		totalSaltos += salto
		
mediaSaltos = (totalSaltos - menorSalto - maiorSalto) / 3
print("Melhor salto: {} m".format(maiorSalto))
print("Pior salto: {} m".format(menorSalto))
print("Media dos demais saltos: {:.2f} m".format(mediaSaltos))
print("Resultado final: ")
print("{}: {:.2f} m".format(nomeAtleta, mediaSaltos))