#17.	Faça um Programa que peça 2 números inteiros e um número real. 
#Calcule e mostre: 
#•	o produto do dobro do primeiro com metade do segundo . 
#•	a soma do triplo do primeiro com o terceiro. 
#•	o terceiro elevado ao cubo. 

numero1 = int(input("Primeiro numero inteiro = "))
numero2 = int(input("Segundo numero inteiro = "))
numero3 = float(input("Terceiro numero REAL = "))

equação1 = (numero1 * 2) * (numero2/2)
equação2 = (3 * numero1) + numero3
equação3 = numero3 ** 3

print("1° Equação = {:.2f}".format(equação1))
print("2° Equação = {:.2f}".format(equação2))
print("3° Equação = {:.2f}".format(equação3))