"""
22 - Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

"""

n = int(input("Digite a quantidade de pessoas: "))
idade0a25 = 0
idade26a60 = 0
idadeMaior60 = 0

for i in range(n+1):
  idade = int(input("Digite sua idade: "))
  if 0 <= idade <= 25:
    idade0a25 += 1
  elif 25 < idade <= 60:
    idade26a60 += 1
  elif idade > 60:
    idadeMaior60 += 1
  else:
    print("Idade invalida")

media0a25 = idade0a25/n
media26a60 = idade26a60/n
mediaMaior60 = idadeMaior60/n

if media0a25 > media26a60 > mediaMaior60:
  print("Turma jovem")
elif media26a60 > media0a25 > mediaMaior60:
  print("Turma adulta")
else:
  print("Turma idosa")