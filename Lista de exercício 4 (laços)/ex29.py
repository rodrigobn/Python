"""
29 - Escrever um programa que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0.25], [26,50], [51,75] e [76,100]. A entrada de dados deve terminar quando for lido um número negativo.
"""
contador0a25 = 0
contador26a50 = 0
contador51a75 = 0
contador76a100 = 0

numero = int(input("Digite um numero inteiro positivo: "))
while numero < 0:
    numero = int(input("Digite um numero inteiro positivo: "))
if 0 < numero <= 25:
    contador0a25 += 1
elif 26 <= numero <= 50:
    contador26a50 += 1
elif 51 <= numero <= 75:
    contador51a75 += 1
elif 76 <= numero <= 100:
    contador76a100 += 1

while numero != 0:
    numero = int(input("Digite um numero inteiro positivo: "))
    if 0 < numero <= 25:
        contador0a25 += 1
    elif 26 <= numero <= 50:
        contador26a50 += 1
    elif 51 <= numero <= 75:
        contador51a75 += 1
    elif 76 <= numero <= 100:
        contador76a100 += 1

print("Numeros entre 0 e 25 = ",contador0a25)
print("Numeros entre 26 e 50 = ",contador26a50)
print("Numeros entre 51 e 75 = ",contador51a75)
print("Numeros entre 76 e 100 = ",contador76a100)