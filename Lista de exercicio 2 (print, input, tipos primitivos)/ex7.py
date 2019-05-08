#7. Faça um Programa que pergunte quanto você ganha por hora e o número de 
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido 
# mês.
valorHora = float(input("Valor da hora trabalhada: R$"))
horaTrabalhada = float(input("Horas trabalhadas no mês: "))
valorResultado = valorHora * horaTrabalhada
print("Você recebeu R${:.2f}".format(valorResultado))