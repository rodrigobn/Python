"""
20.	Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
Álcool: 
•	até 20 litros, desconto de 3% por litro 
•	acima de 20 litros, desconto de 5% por litro 
Gasolina: 
•	até 20 litros, desconto de 4% por litro 
•	acima de 20 litros, desconto de 6% por litro.

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 

"""

litros = float(input("Digite a quantidade de litros: "))
combustivel = input("Digite a letra do tipo de combustivel (A-álcool, G-gasolina): ")

valorGasolinaLitro = 2.5
valorAlcoolLitro = 1.9

if combustivel == "g":
  if 0 > litros >= 20:
    desconto = 0.04
  else:
    desconto = 0.06
  resultado = (valorGasolinaLitro * litros) + (valorGasolinaLitro * litros * desconto)
else:
  if 0 > litros >= 20:
    desconto = 0.03
  else:
    desconto = 0.05
  resultado = (valorAlcoolLitro * litros) + (valorAlcoolLitro * litros * desconto)

print("O valor a ser pago é de R${:.2f}".format(resultado))