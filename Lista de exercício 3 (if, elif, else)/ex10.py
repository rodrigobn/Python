"""
10.	Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 
"""

dia = input("Digite um numero referente ao dia da semana: ")

if dia == "1":
  print("{}-Domingo".format(dia))
elif dia == "2":
  print("{}-Segunda".format(dia))
elif dia == "3":
  print("{}-Terça".format(dia))
elif dia == "4":
  print("{}-Quarta".format(dia))
elif dia == "5":
  print("{}-Quinta".format(dia))
elif dia == "6":
  print("{}-Sexta".format(dia))
elif dia == "7":
  print("{}-Sabado".format(dia))
else:
  print("valor invalido")