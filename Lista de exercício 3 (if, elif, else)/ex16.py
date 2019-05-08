"""
16.	Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina. 
•	Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1; 
•	Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. 

"""

saque = int(input("Digite o valor inteiro do saque: R$"))

notas100 = 0
notas50 = 0
notas10 = 0
notas5 = 0
notas1 = 0

centena = saque // 100
dezena = (saque % 100) // 10
unidade = (saque % 100) % 10

notas100 = centena

if dezena > 5:
  notas50 += 1
  notas10 += dezena - 5
else:
  notas10 = dezena

if unidade > 5:
  notas5 += 1
  notas1 += unidade - 5
else:
   notas1 = unidade

print("{} notas de R$100".format(notas100))
print("{} notas de R$50".format(notas50))
print("{} notas de R$10".format(notas10))
print("{} notas de R$5".format(notas5))
print("{} notas de R$1".format(notas1))