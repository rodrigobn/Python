"""
15 - Fazer um programa que calcule e escreva a soma dos 50 primeiros termos da seguinte série:

(1000/1) + (997/2) + (994/3) + (991/4) + ...
"""
numerador = 1000
resultado = 0
for i in range(1, 51):
  resultado += numerador/i
  numerador -= 3

print("{:.2f}".format(resultado))