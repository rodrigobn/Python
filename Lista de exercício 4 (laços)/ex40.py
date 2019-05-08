"""
40 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:

Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

"""

totalAcidentes = totalVeiculos = codigoCidadeMaiorNumeroAcidente = codigoCidadeMenorNumeroAcidente = 0

codigoCidade = int(input("Codigo da cidade: "))
numeroVeiculos = int(input("Numero de veiculos de passeio: "))
numeroAcidentes = int(input("Número de acidentes de trânsito com vítimas: "))

maiorNumeroAcidente = numeroAcidentes
menorNumeroAcidente = numeroAcidentes
codigoCidadeMaiorNumeroAcidente = codigoCidade
codigoCidadeMenorNumeroAcidente = codigoCidade

totalVeiculos += numeroVeiculos
if numeroVeiculos < 2000:
	totalAcidentes += numeroAcidentes

for i in range(4):
	codigoCidade = int(input("Codigo da cidade: "))
	numeroVeiculos = int(input("Numero de veiculos de passeio: "))
	numeroAcidentes = int(input("Número de acidentes de trânsito com vítimas: "))
	
	if numeroAcidentes > maiorNumeroAcidente:
		maiorNumeroAcidente = numeroAcidentes
		codigoCidadeMaiorNumeroAcidente = codigoCidade
	elif numeroAcidentes < menorNumeroAcidente:
		menorNumeroAcidente = numeroAcidentes
		codigoCidadeMenorNumeroAcidente = codigoCidade
	
	totalVeiculos += numeroVeiculos
	if numeroVeiculos < 2000:
		totalAcidentes += numeroAcidentes

mediaVeiculos = totalVeiculos / 5
mediaAcidente = totalAcidentes / 5

print("O maior índice de acidentes de transito pretence a cidade {} no total de {} acidentes".format(codigoCidadeMaiorNumeroAcidente, maiorNumeroAcidente))
print("O menor índice de acidentes de transito pretence a cidade {} no total de {} acidentes".format(codigoCidadeMenorNumeroAcidente, menorNumeroAcidente))
print("A média de veículos nas cinco cidades juntas é de {}".format(mediaVeiculos))
print("A média de acidentes de trânsito nas cidades com menos de 2.000 veículos é de {}".format(mediaAcidente))