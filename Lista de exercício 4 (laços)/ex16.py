"""
16 - Faça um programa que recebe o número real x como entrada e devolva uma aproximação do arco tangente de x (em radianos) através da série:

arctan(x) = x - (x**3/3) + (x**5/5) - (x**7/7) + ...

Considere a aproximação para 50 termos.
"""

x = float(input("Digite o valor de x: "))
while x < 0:
	x = float(input("Digite o valor de x: "))

resultado = 0
inverteSinal = 1
num = 1
for i in range(50):
	resultado += x**num/num * (inverteSinal)
	num += 2
	inverteSinal *= -1
print("{:.2f}".format(resultado))