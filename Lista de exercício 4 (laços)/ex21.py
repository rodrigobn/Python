"""
21 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

"""

numero = int(input("Digite um numero inteiro: "))
while numero < 0:
    numero = int(input("Digite um numero inteiro: "))

divisivelPorOutros = 0

if numero != 0 and numero != 1:
    for i in range(1, numero+1):
        if numero % i == 0:
            divisivelPorOutros += 1
						
    if divisivelPorOutros == 2:
        print("É primo")
    else:
        print("Não é primo")
else:
    print("Não existe esta propriedade")
