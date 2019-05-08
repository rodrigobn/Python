"""
24 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela. 
Os juros e a quantidade de parcelas seguem a tabela abaixo: 
Quantidade de Parcelas            % de Juros sobre o valor inicial da dívida
        1                  			                      0
	      3   		    	                                10
	      6       			                                15
	      9       			                                20
	      12      			                                25
Exemplo de saída do programa: 
Valor da Dívida  Valor dos Juros      Quantidade de Parcelas                       Valor da Parcela
R$ 1.000,00            0                         1                                 R$  1.000,00
R$ 1.100,00           100                        3                                 R$    366,00
R$ 1.150,00           150                        6                                 R$    191,67


"""

valorDivida = float(input("Digite o valor da divida: R$"))

parcelas = 3
juros = 1.1

print("Valor da Dívida  Valor dos Juros      Quantidade de Parcelas                       Valor da Parcela")
print("R$ 1.000,00            0                         1                                 R$  1.000,00")


for i in range(5):
  if parcelas == 3:    
    print("R$ {:.2f}            {:.2f}                     {}                                 R$  {:.2f}".format(valorDivida*juros, valorDivida*(juros-1),parcelas, valorDivida*juros/parcelas))
    parcelas += 3
    juros = 1.15
  elif parcelas == 6:
    print("R$ {:.2f}            {:.2f}                     {}                                 R$  {:.2f}".format(valorDivida*juros, valorDivida*(juros-1),parcelas, valorDivida*juros/parcelas))
    parcelas += 3
    juros += 0.05
  elif parcelas == 9:
    print("R$ {:.2f}            {:.2f}                     {}                                 R$  {:.2f}".format(valorDivida*juros, valorDivida*(juros-1),parcelas, valorDivida*juros/parcelas))
    parcelas += 3
    juros += 0.05
  elif parcelas == 12:
    print("R$ {:.2f}            {:.2f}                     {}                                R$  {:.2f}".format(valorDivida*juros, valorDivida*(juros-1),parcelas, valorDivida*juros/parcelas))
    parcelas += 3
    juros += 0.05