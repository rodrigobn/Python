"""
6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
  
"""
medias = []

for i in range(1, 5):
	notas = 0
	for j in range(1, 5):
		nota = float(input("{}° Aluno. {}° Nota: ".format(i, j)))
		if nota < 0:
			while nota < 0:
				nota = float(input("Digite uma nota positiva: ".format(i, j)))
		notas += nota
			
	medias.append(notas/4)
		
contador = 0
for i in range(len(medias)):
	if medias[i] >= 7:
		contador += 1

print("{} alunos com media maior que 7.0".format(contador))