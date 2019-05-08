"""
8 - Faça um programa para somar os números pares positivos < 1000 e ao final escrever o resultado.
"""

soma = 0
for i in range(1, 10):
  if i % 2 == 0:
    soma += i

print(soma)