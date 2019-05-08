"""
23.	Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: para homens: (72.7*h) – 58 e para mulheres: (62.1*h) - 44.7 (h = altura)

"""

altura = float(input("Digite a altura em m: "))
while altura <= 0:
  altura = float(input("Digite um valor valido: "))

sexo = input("Digite a letra representando o sexo (H)Homem, (M)Mulher: ")
while sexo != "m" and sexo != "M" and sexo != "h" and sexo != "H":
  sexo = input("Digite uma letra valida (H) ou (M): ")

if sexo == "h" or sexo == "H":
  pesoIdeal = (72.7 * altura) - 58
else:
  pesoIdeal = (62.1 * altura) - 44.7

print("O seu peso idela é = {}kg".format(pesoIdeal))