"""
17.	Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 

"""

numero = int(input("Digite um número"))

if numero % 2 == 0:
  print("{} é par".format(numero))
else:
  print("{} é impar".format(numero))