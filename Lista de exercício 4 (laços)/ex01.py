"""
1 - Escreva um programa que efetue a leitura de 20 valores numéricos e apresente no final o total do somatório e a média dos valores lidos.

"""

soma = 0
for i in range(20):
  num = float(input("Digite um numero: "))
  soma += num
media = soma/20
print("Soma = ", soma)
print("Media = ", media)