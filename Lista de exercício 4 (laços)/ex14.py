"""
14 - Faça um programa para: 
a) Ler um valor x qualquer
b) Calcular Y = (x+1)+(x+2)+(x+3)+(x+4)+(x+5)+…(x+100).

"""

x = float(input("Digite o valor de X: "))
y = 0

for i in range(1, 101):
  y += (x+i)

print("{:.2f}".format(y))