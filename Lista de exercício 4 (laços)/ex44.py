"""
44 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. 

Para finalizar o conjunto de votos tem-se o valor zero.
"""
escolha = 1
nulos = brancos = Alvaro = Cabo = Ciro = Eymael = Fernando = Geraldo = Guilherme = Henrique = Jair = Amoedo = Goulart = Marina = Vera = totalVotos = porcentagemNulos = porcentagemBrancos = 0
while escolha != 0:
	print("""
---------Eleições 2019-------- 

Alvaro Dias (Podemos)------ 19
Cabo Daciolo (Patriota)---- 51
Ciro Gomes (PDT)----------- 12
Eymael (DC)---------------- 27
Fernando Haddad (PT)------- 13
Geraldo Alckmin (PSDB)----- 45
Guilherme Boulos (PSOL)---- 50
Henrique Meirelles (MDB)--- 15
Jair Bolsonaro (PSL)------- 17
João Amoêdo (Novo)--------- 30
João Goulart Filho (PPL)--- 54
Marina Silva (Rede)-------- 18
Vera Lúcia (PSTU)---------- 16

Nulo-------------------------5
Branco-----------------------6
""")
	escolha = int(input("Voto: "))
	if escolha == 19:
		Alvaro += 1
		totalVotos += 1
	elif escolha == 51:
		Cabo += 1
		totalVotos += 1
	elif escolha == 12:
		Ciro += 1
		totalVotos += 1
	elif escolha == 27:
		Eymael += 1
		totalVotos += 1
	elif escolha == 13:
		Fernando += 1
		totalVotos += 1
	elif escolha == 45:
		Geraldo += 1
		totalVotos += 1
	elif escolha == 50:
		Guilherme += 1
		totalVotos += 1
	elif escolha == 15:
		Henrique += 1
		totalVotos += 1
	elif escolha == 17:
		Jair += 1
		totalVotos += 1
	elif escolha == 30:
		Amoedo += 1
		totalVotos += 1
	elif escolha == 54:
		Goulart += 1
		totalVotos += 1
	elif escolha == 18:
		Marina += 1
		totalVotos += 1
	elif escolha == 16:
		Vera += 1
		totalVotos += 1
	elif escolha == 5:
		nulos += 1
		totalVotos += 1
	elif escolha == 6:
		brancos += 1
		totalVotos += 1

#A percentagem de votos nulos sobre o total de votos
if totalVotos != 0:
	porcentagemNulos = nulos/totalVotos * 100
	porcentagemBrancos = brancos/totalVotos * 100

print("""
--------Eleições 2019-----Votos 

Alvaro Dias (Podemos)------ {:.0f}%
Cabo Daciolo (Patriota)---- {:.0f}%
Ciro Gomes (PDT)----------- {:.0f}%
Eymael (DC)---------------- {:.0f}%
Fernando Haddad (PT)------- {:.0f}%
Geraldo Alckmin (PSDB)----- {:.0f}%
Guilherme Boulos (PSOL)---- {:.0f}%
Henrique Meirelles (MDB)--- {:.0f}%
Jair Bolsonaro (PSL)------- {:.0f}%
João Amoêdo (Novo)--------- {:.0f}%
João Goulart Filho (PPL)--- {:.0f}%
Marina Silva (Rede)-------- {:.0f}%
Vera Lúcia (PSTU)---------- {:.0f}%

Nulo------------------------{}
Branco----------------------{}

Total de votos--------------{}

Porcentagem de votos nulos		{:.0f}%
Porcentagem de votos brancos	{:.0f}%
""".format(Alvaro/totalVotos * 100, Cabo/totalVotos * 100, Ciro/totalVotos * 100, Eymael/totalVotos * 100, Fernando/totalVotos * 100, Geraldo/totalVotos * 100, Guilherme/totalVotos * 100, Henrique/totalVotos * 100, Jair/totalVotos * 100, Amoedo/totalVotos * 100, Goulart/totalVotos * 100, Marina/totalVotos * 100, Vera/totalVotos * 100, nulos, brancos, totalVotos, porcentagemNulos, porcentagemBrancos))