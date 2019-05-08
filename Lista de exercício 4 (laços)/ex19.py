"""
19 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.


"""

primeiroNumero = int(input("Digite o primeiro numero: "))
segundoNumero = int(input("Digite o segundo numero: "))

for i in range(primeiroNumero + 1, segundoNumero):
  print(i)