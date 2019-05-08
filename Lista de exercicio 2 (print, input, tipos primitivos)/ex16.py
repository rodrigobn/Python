#16.	Escrever um algoritmo que leia o nome de um vendedor, o seu salário 
#fixo e o total de vendas efetuadas por ele no mês (em dinheiro). 
#Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, 
#informar o seu nome, o salário fixo e salário no final do mês.

vendedor = input("Nome do vendedor: ")
salario = float(input("Salario fixo R$ "))
totalVendas = float(input("Total de vendas no mês R$ "))

comissao = 0.15

salarioComissao = salario + (totalVendas * comissao)

print("O(a) vendedor(a) {} recebe R${:.2f} de salario fixo e o seu salario + comissao é de R${:.2f}".format(vendedor, salario, salarioComissao))