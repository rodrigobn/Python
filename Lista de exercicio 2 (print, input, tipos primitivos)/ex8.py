#8. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
temperaturaF = float(input("Digite a temperatura em Farenheit: F° "))
temperaturaC = (5*(temperaturaF-32)/9)
print("{:.2f} C°".format(temperaturaC))