#1.	Faça um Programa que peça dois números e imprima o maior deles. 

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))

if numero1 > numero2:
  print("O numero maior é o {}".format(numero1))
elif numero2 > numero1:
  print("O numero maior é o {}".format(numero2))
else:
  print("Os numeros são iguais")