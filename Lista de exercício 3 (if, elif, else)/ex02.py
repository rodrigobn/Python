#2.	Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

numero = float(input("Digite um numero: "))

if numero < 0:
  print("O numero {} é negativo".format(numero))
elif numero > 0:
  print("O numero {} é positivo".format(numero))
else:
  print("O numero {} é neutro".format(numero))