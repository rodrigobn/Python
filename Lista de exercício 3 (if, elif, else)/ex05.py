# 5.	Faça um Programa que leia três números e mostre o maior deles. 

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
  print("O numero maior é o {}".format(numero1))
elif numero2 > numero1 and numero2 > numero3:
  print("O numero maior é o {}".format(numero2))
elif numero3 > numero1 and numero3 > numero2:
  print("O numero maior é o {}".format(numero3))
else:
  print("Todos os numeros são iguais")