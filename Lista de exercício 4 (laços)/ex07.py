"""
7 - Escreva um programa que calcula o fatorial de um dado número N.
"""

num = int(input("Digite o valor: "))
while num < 0:
	num = int(input("Digite o valor: "))

fatorial = 1; #O valor neutro da multiplicação

for i in range(num, 1, -1):
  fatorial *= i
print(fatorial)