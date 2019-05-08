#11. Faça um algoritmo que receba um valor que foi depositado e exiba o valor
# com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a.m.

deposito = float(input("Valor do deposito R$"))
juros = 0.07
rendimento = (deposito * juros)
total = rendimento + deposito
print("Apos um mês o total, com o rendimento de R${:.2f}, sera de R${:.2f}".format(rendimento, total))