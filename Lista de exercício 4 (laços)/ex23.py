"""
23 - O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperatura informada, bem como a média das temperaturas.

"""

n = int(input("Informe a quantidade de temperaturas para analise: "))
temperatura = float(input("Digite uma temperatura: "))

maiorTemp = temperatura
menorTemp = temperatura

tempMaiorRepetida = 0
tempMenorRepetida = 0

for i in range(n-1):
  temperatura = float(input("Digite uma temperatura: "))
  if temperatura > maiorTemp:
    maiorTemp = temperatura
    tempMaiorRepetida = 0
  elif temperatura < menorTemp:
    menorTemp = temperatura
    tempMenorRepetida = 0
  elif maiorTemp == temperatura:
    tempMaiorRepetida += 1
  elif menorTemp == temperatura:
    tempMenorRepetida += 1


print("A maior foi {} C°".format(maiorTemp))
print("A menor foi {} C°".format(menorTemp))

if tempMaiorRepetida == 0:
  print("A media da temperatura maior foi = {}".format(tempMaiorRepetida/n))
else:
  print("A media da temperatura maior foi = {}".format((tempMaiorRepetida + 1) / n))

if tempMenorRepetida == 0:
  print("A media da temperatura menor foi = {}".format(tempMenorRepetida/n))
else:
  print("A media da temperatura menor foi = {}".format((tempMenorRepetida + 1) / n))