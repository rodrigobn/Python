"""
18 - Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião em relação ao filme: ótimo - 3, bom - 2, regular - 1. Faça um programa que receba a idade e a opinião de 15 espectadores, calcule e imprima:

a) A média das idades das pessoas que responderam ótimo;

b) A quantidade de pessoas que responderam regular;

c) A porcentagem de pessoas que responderam bom entre todos os espectadores analisados.


"""
totalIdade = 0
contadorOtimo = 0
contadorBom = 0
contadorRegular = 0

for i in range(15):
  idade = int(input("Digite a idade: "))
  opiniao = int(input("Digite a sua nota: "))

  if opiniao == 3:
    totalIdade += idade
    contadorOtimo += 1
  elif opiniao == 2:
    contadorBom += 1
  elif opiniao == 1:
    contadorRegular += 1

if contadorOtimo != 0:
  print("Media das idades que responderam ótimo: {:.2f}".format(totalIdade / contadorOtimo))
print(30*"-")
print("Regular = ", contadorRegular)
print(30*"-")
print("Porcentagem da classificação boa = {:.0f}%".format(contadorBom/3*100))