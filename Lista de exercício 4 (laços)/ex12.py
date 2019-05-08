"""
12 - Faça um programa para ler um valor X e calcular Y = X +2X+3X+4X+…+20X
"""

x = float(input("Digite o valor de X: "))
y = 0

for i in range(1, 21):
  y += x * i

print(y)