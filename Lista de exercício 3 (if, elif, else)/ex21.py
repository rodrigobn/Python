"""
21.	Uma fruteira está vendendo frutas com a seguinte tabela de preços: 
                  Até 5 Kg              Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

"""

morangos = float(input("Digite o valor em kg dos morangos: "))
macas = float(input("Digite o valor em kg dos maçãs: "))

while morangos < 0 or macas < 0:
    print("Digite um valor valido")
    morangos = float(input("Digite o valor em kg dos morangos: "))
    macas = float(input("Digite o valor em kg dos maçãs: "))

if morangos <= 5:
    valorMorango = morangos * 2.5
else:
    valorMorango = morangos * 2.2

if macas <= 5:
    valorMaca = macas * 1.8
else:
    valorMaca = macas * 1.5

valorTotal = valorMaca + valorMorango

if morangos + macas >= 8 or valorTotal >= 25:
    valorTotal = valorTotal + (valorTotal * 0.1)

print("Valor total a pagar R${:.2f}".format(valorTotal))