"""
45 - Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
"""

sistema = "sim"
while sistema == "sim":
	acertos = erros = 0
	for i in range(1,11):
		resposta = input("{} - ".format(i))
		if i == 1 and (resposta == "A" or resposta == "a"):
			acertos += 1
		elif i == 2 and (resposta == "B" or resposta == "b"):
			acertos += 1
		elif i == 3 and (resposta == "C" or resposta == "c"):
			acertos += 1
		elif i == 4 and (resposta == "D" or resposta == "d"):
			acertos += 1
		elif i == 5 and (resposta == "E" or resposta == "e"):
			acertos += 1
		elif i == 6 and (resposta == "E" or resposta == "e"):
			acertos += 1
		elif i == 7 and (resposta == "D" or resposta == "d"):
			acertos += 1
		elif i == 8 and (resposta == "C" or resposta == "c"):
			acertos += 1
		elif i == 9 and (resposta == "B" or resposta == "b"):
			acertos += 1
		elif i == 10 and (resposta == "A" or resposta == "a"):
			acertos += 1
		else:
			erros += 1
	print("Acertos = {} pontos".format(acertos))
	print("Erros = {}".format(erros))
	
	sistema = input("Continuar usando o sistema? (s)Sim ou (n)Não")
	while sistema != "s" and sistema != "n" and sistema != "Sim" and sistema != "Não":
		sistema = input("Continuar usando o sistema? ")

