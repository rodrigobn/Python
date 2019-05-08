"""
8.	As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: 
 •	salários até R$ 280,00 (incluindo) : aumento de 20% 
 •	salários entre R$ 280,00 e R$ 700,00 : aumento de 15% 
 •	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10% 
 •	salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela: 
 •	o salário antes do reajuste; 
 •	o percentual de aumento aplicado; 
 •	o valor do aumento; 
 •	o novo salário, após o aumento. 
"""

salario = float(input("Digite o valor do salario R$ "))

if salario > 0:
  if salario <= 280:
    percentualReajuste = 0.2
  elif salario > 280 and salario <= 700:
    percentualReajuste = 0.15
  elif salario > 700 and salario <= 1500:
    percentualReajuste = 0.1
  elif salario > 1500:
    percentualReajuste = 0.05
    
  print("Salario antes do reajuste R${:.2f}".format(salario))
  print("Percentual de aumento {}".format(percentualReajuste))
  valorReajuste = salario * percentualReajuste
  print("Valor do aumento R${:.2f}".format(valorReajuste))
  salarioReajustado = salario + valorReajuste
  print("Novo salario R${:.2f}".format(salarioReajustado))
else:
  print("Salario invalido")