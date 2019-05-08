"""
4 - Fazer um programa para ler o sexo de dez pessoas e mostrar a quantidade de pessoas do sexo masculino e do sexo feminino, separadamente.
"""

quantMasculino = 0
quantFeminino = 0

for i in range(10):
	sexo = input("Digite (f) para feminino e (m) para masculino: ")
	while sexo != "f" and sexo != "F" and sexo != "m" and sexo != "M":
		sexo = input("Digite 'f' para feminino e 'm' para masculino: ")
		
	if sexo == "f" or sexo == "F":
		quantFeminino += 1
	elif sexo == "m" or sexo == "M":
		quantMasculino += 1

print("Masculino = ", quantMasculino)
print("Feminino = ", quantFeminino)