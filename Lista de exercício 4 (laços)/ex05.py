"""
5 - Escreva um programa que leia 10 números e informe o maior e o menor número.
"""
num = float(input("Digite um numero: "))
maior = num
menor = num

for i in range(9):
  num = float(input("Digite um numero: "))
  if num < menor:
    menor = num
  elif num > maior:
    maior = num
  
print("O numero maior foi: ", maior)
print("O numero menor foi: ", menor)