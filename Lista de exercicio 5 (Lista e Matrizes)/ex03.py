"""
3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 
"""

notas = []
media = 0
for i in range(4):
    nota = float(input("Nota: "))
    if nota < 0:
        while nota < 0:
            nota = float(input("Digite uma nota valida: "))
    notas.append(nota)

for i in range(len(notas)):
    media += notas[i]

if notas == []:
	print("Lista vazia")
else:
	print(notas)
	print(media / len(notas))