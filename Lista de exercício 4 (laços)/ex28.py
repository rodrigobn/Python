"""
28 - Faça um programa que leia uma quantidade não determinada de números positivos. 

a) Calcule a quantidade de números pares e ímpares.
b) A média de valores pares 
c) A média geral dos números lidos. 

O número que encerrará a leitura será zero.

"""
contadorPar = contadorImpar = contadorNumeros = mediaPar = 0

numero = int(input("Digite um numero inteiro positivo: "))
while numero < 0:
	numero = int(input("Digite um numero inteiro positivo: "))

while numero != 0 and numero > 0:  
	if numero % 2 == 0:
		contadorPar += 1
	else:
		contadorImpar += 1
	contadorNumeros += 1
	numero = int(input("Digite um numero inteiro positivo: "))

print("A quantidade de numeros pares é: ", contadorPar)
print("A quantidade de numeros impares é: ", contadorImpar)

if contadorPar != 0:
  mediaPar = contadorPar / contadorNumeros
print("A media dos numeros pares é: {:.1f}".format(mediaPar))