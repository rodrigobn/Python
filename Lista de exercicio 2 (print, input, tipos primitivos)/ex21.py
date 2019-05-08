"""
21. Faça um Programa que pergunte quanto você ganha por hora e o número de 
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido 
mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o 
INSS e 5% para o sindicato, faça um programa que nos dê: 

    a)	salário bruto. 
    b)	quanto pagou ao INSS. 
    c)	quanto pagou ao sindicato. 
    d)	o salário líquido. 
    e)	calcule os descontos e o salário líquido, conforme a tabela abaixo:

    Salário Bruto : R$
    IR (11%) : R$
    INSS (8%) : R$
    Sindicato ( 5%) : R$
    Salário Liquido : R$
"""

valorHora = float(input("Valor da hora trabalhada R$"))
horasTrabalhada = float(input("Quantidade de horas trabalhada no mês: "))

impostoRenda = 0.11
inss = 0.08
sindicato = 0.05

salarioBruto = horasTrabalhada * valorHora
descontoImpostoRenda = salarioBruto * impostoRenda
descontoInss = salarioBruto * inss
descontoSindicato = salarioBruto * sindicato
salarioLiquido = salarioBruto - descontoImpostoRenda - descontoInss - descontoSindicato

print(30*"-")
print ("Salário Bruto : R${:.2f}".format(salarioBruto))
print ("IR (11%) : R${:.2f}".format(descontoImpostoRenda))
print ("INSS (8%) : R${:.2f}".format(descontoInss))
print ("Sindicato (5%) : R${:.2f}".format(descontoSindicato))
print ("Salário Liquido : R${:.2f}".format(salarioLiquido))
print(30*"-")