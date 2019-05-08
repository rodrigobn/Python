"""
30 - Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes 
"""

codigo = 1

contadorCliente = maisAlto = maisBaixo = maisGordo = maisMagro = pesoTotal = alturaTotal = mediaAltura = 0

codigoMaisAlto = codigoMaisBaixo = codigoMaisGordo = codigoMaisMagro = 0

codigo = int(input("Codigo: "))
altura = float(input("Altura: "))
peso = float(input("Peso: "))

if codigo > 0:
	maisAlto = maisBaixo = altura
	alturaTotal += altura
	maisGordo = maisMagro = peso
	pesoTotal += peso
	codigoMaisAlto = codigoMaisBaixo = codigo
	codigoMaisGordo = codigoMaisMagro = codigo
	contadorCliente += 1

while codigo != 0 and codigo > 0:
	codigo = int(input("Codigo: "))
	if codigo != 0 and codigo > 0:
		altura = float(input("Altura: "))
		peso = float(input("Peso: "))
		if altura > maisAlto:
			maisAlto = altura
			codigoMaisAlto = codigo
			alturaTotal += altura
		elif altura < maisBaixo:
			maisBaixo = altura
			codigoMaisBaixo = codigo
			alturaTotal += altura
		else:
			alturaTotal += altura

		if peso > maisGordo:
			maisGordo = peso
			codigoMaisGordo = codigo
			pesoTotal += peso
		elif peso < maisMagro:
			maisMagro = peso
			codigoMaisMagro = codigo
			pesoTotal += peso
		else:
			pesoTotal += peso
		
		contadorCliente += 1

print("O codigo do cliente mais alto é: {} e a sua altura é {}cm".format(codigoMaisAlto, maisAlto))
print("O codigo do cliente mais baixo é: {} e a sua altura é {}cm".format(codigoMaisBaixo, maisBaixo))
print("O codigo do cliente mais gordo é: {} e a seu peso é {}kg".format(codigoMaisGordo, maisGordo))
print("O codigo do cliente mais magro é: {} e a seu peso é {}kg".format(codigoMaisMagro, maisMagro))

if contadorCliente != 0:
	mediaAltura = alturaTotal / contadorCliente
	mediaPeso = pesoTotal / contadorCliente
print("A media das alturas é: {:.2f}m".format(mediaAltura))
print("A media dos pesos é: {:.2f}m".format(mediaPeso))
print(alturaTotal, contadorCliente)