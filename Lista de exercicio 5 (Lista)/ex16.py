"""
16 - Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados
"""
intervaloInicio = [0,0,0,0,0,0,0,0,1000]
intervaloFinal = [0,0,0,0,0,0,0,0,"em diante"]
lista = [0,0,0,0,0,0,0,0,0]

for i in range(1,6):	
	venda = float(input("Valor da venda na semana, vendedor {}: R$".format(i)))
	salarioComComissao = 200 + (venda * 0.09)
	print(salarioComComissao)
	for j in range(2,10):
		if j*100 < salarioComComissao < (j*100)+99:		
			lista[j-2] += 1
		intervaloInicio[j-2] = j*100
		intervaloFinal[j-2] = (j*100)+99
	if salarioComComissao >= 1000:
		lista[-1] += 1

for i in range(len(intervaloInicio)-1):
	print("{} vendedore(s) receberam o salario entre ${} - ${}".format(lista[i], intervaloInicio[i], intervaloFinal[i]))

print("{} vendedore(s) receberam o salario entre ${} - {}".format(lista[-1], intervaloInicio[-1], intervaloFinal[-1]))
#print(lista)
#print(intervaloInicio)
#print(intervaloFinal)