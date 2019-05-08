"""
27 - A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
a) Média do salário da população;
b) Média do número de filhos;
c) Maior salário;
d) Percentual de pessoas com salário até R$250,00.

Desenvolver um programa para calcular e escrever o que foi pedido nos itens a, b, c e d. O final da leitura de dados se dará com a entrada de um salário negativo.

"""
salario = 0
contadorPopulacao = 0
contadorFilhos = 0
totalSalario = 0
maiorSalario = 0
contadorRendaBaixa = 0

while salario >= 0:
  salario = float(input("Valor do salario: R$"))
  numeroFilhos = int(input("Numero de filhos: "))
  
  if salario >= 0:
    if salario <= 250:
      contadorRendaBaixa += 1
    if salario > maiorSalario:
      maiorSalario = salario
    
    totalSalario += salario
    contadorPopulacao += 1
    contadorFilhos += numeroFilhos

mediaSalario = totalSalario/contadorPopulacao
print("A media salarial é: R${:.2f}".format(mediaSalario))
mediaFilhos = contadorFilhos/contadorPopulacao
print("A media de filhos é: {:.2f}".format(mediaFilhos))
print("O maior salario foi: R$", maiorSalario)
percentualRendaBaixa = (contadorRendaBaixa/contadorPopulacao)*100
print("Percentual de pessoas com salário até R$250,00 é: {:.1f}%".format(percentualRendaBaixa))