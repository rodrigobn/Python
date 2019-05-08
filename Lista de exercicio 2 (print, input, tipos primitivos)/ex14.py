#14.	Escrever um algoritmo para determinar o consumo médio de um automóvel 
#sendo fornecida a distância total percorrida pelo automóvel e o total de 
#combustível gasto.

distancia = float(input("Distancia percorrida em km: "))
combustiveGasto = float(input("Quantidade de combustivel gasto em L: "))

resultado = distancia/combustiveGasto

print("O automóvel percorre {:.2f}km por litro".format(resultado))