#10. Elaborar um algoritmo que efetue a apresentação do valor da 
#conversão em real (R$) de um valor lido em dólar (US$). 
#O algoritmo deverá solicitar o valor da cotação do dólar e 
#também a quantidade de dólares disponíveis com o usuário.

quantidadeDolares = float(input("Quantos dolares? $"))
valorDolarAtual = float(input("Valor do dolar em reais hoje: RS"))

conversao = quantidadeDolares*valorDolarAtual

print("${:.2f}".format(quantidadeDolares), "dolares custa R${:.2f}".format(conversao))