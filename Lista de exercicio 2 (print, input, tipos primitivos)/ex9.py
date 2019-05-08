#9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
temperaturaC = float(input("Digite a temperatura em Celsius C°: "))
temperaturaF = 1.8*temperaturaC + 32
print("{:.2f} F°".format(temperaturaF))