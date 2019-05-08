""" 9.	Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 
•	Desconto do IR: 
•	Salário Bruto até 900 (inclusive) - isento 
•	Salário Bruto até 1500 (inclusive) - desconto de 5% 
•	Salário Bruto até 2500 (inclusive) - desconto de 10% 
•	Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220. 
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS (10%)                  : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

valorHora = float(input("Valor da hora trabalhada R$"))
horasTrabalhada = float(input("Quantidade de horas trabalhada no mês: "))

inss = 0.1
fgts = 0.11
sindicato = 0.03

salarioBruto = horasTrabalhada * valorHora
if salarioBruto <= 900:
  impostoRenda = 0
elif salarioBruto > 900 and salarioBruto <= 1500:
  impostoRenda = 0.05
elif salarioBruto > 1500 and salarioBruto <= 2500:
  impostoRenda = 0.1
else:
  impostoRenda = 0.2

descontoImpostoRenda = salarioBruto * impostoRenda
descontoInss = salarioBruto * inss
descontoFgts = salarioBruto * fgts
descontoSindicato = salarioBruto * sindicato
totalDescontos = descontoImpostoRenda + descontoInss
salarioLiquido = salarioBruto - totalDescontos

print (30*"-")
print ("Salário Bruto: ({} * {})    : R${:.2f}".format(valorHora, horasTrabalhada, salarioBruto))
print ("(-) IR ({}%)                : R${:.2f}".format(impostoRenda*100,descontoImpostoRenda))
print ("(-) INSS (10%)              : R${:.2f}".format(descontoInss))
print ("FGTS (11%)                  : R${:.2f}".format(descontoFgts))
print ("Total de descontos          : R${:.2f}".format(totalDescontos))
print ("Salário Liquido             : R${:.2f}".format(salarioLiquido))
print (30*"-")
