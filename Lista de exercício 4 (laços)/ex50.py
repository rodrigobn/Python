"""
50 - Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""

nomeAtleta = input()
print("Atleta: ",nomeAtleta)
nota = float(input("Nota: "))
while nota < 0:
	nota = float(input("Nota positiva: "))

maiorNota = nota
menorNota = nota
totalNotas = 0
if nota < menorNota:
		menorNota = nota
elif nota > maiorNota:
	maiorNota = nota
totalNotas += nota

for i in range(6):
	nota = float(input("Nota: "))
	while nota < 0:
		nota = float(input("Nota positiva: "))
	if nota < menorNota:
		menorNota = nota
	elif nota > maiorNota:
		maiorNota = nota
	totalNotas += nota	

print("Resultado final:")
print("Melhor nota: {:.1f}".format(maiorNota))
print("Pior nota: {:.1f}".format(menorNota))
media = (totalNotas - menorNota - maiorNota) / 5
print("Media: {:.2f}".format(media))