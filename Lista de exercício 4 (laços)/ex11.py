"""
11 - Faça um programa para calcular um valor A elevado a um expoente B. Os valores A e B deverão ser lidos. Não usar A** B e sim uma estrutura de repetição.
"""

numA = int(input("Digite o valor de A: "))
expoenteB = int(input("Digite o valor do expoente B: "))

resultado = numA
for i in range(expoenteB-1):
  resultado *= numA

print(resultado)