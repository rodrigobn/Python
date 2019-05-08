"""
13 - Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N. Faça um programa para gerar e mostrar o número H. O número N será fornecido como entrada.
"""

n = int(input("Digite o valor de repetições N: "))
h = 0

for i in range(1, n+1):
  h += 1/i

print("{:.2f}".format(h))