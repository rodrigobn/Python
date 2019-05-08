# b)	Faça um algoritmo que leia a idade de uma pessoa expressa em anos, 
# meses e dias e mostre-a expressa apenas em dias. Considere que um ano tem 
# 365 dias e um mês tem 30 dias.

idadeAnos = float(input("Idade em anos = "))
idadeMeses = float(input("Idade em meses = "))
idadedias = float(input("Idade em dias = "))

anosDias = idadeAnos * 365
mesesDias = idadeMeses * 30

idadedias += anosDias + mesesDias

print(idadedias)