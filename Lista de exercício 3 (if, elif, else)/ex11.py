"""
11.	Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 
•	  Média de Aproveitamento  Conceito
•	  Entre 9.0 e 10.0       A
•	  Entre 7.5 e 9.0         B
•	  Entre 6.0 e 7.5         C
•	  Entre 4.0 e 6.0         D
•	  Entre 4.0 e zero       E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. 

"""

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
  conceito = "A"
  resultado = "APROVADO"
elif media >= 7.5 and media < 9:
  conceito = "B"
  resultado = "APROVADO"
elif media >= 6 and media < 7.5:
  conceito = "C"
  resultado = "APROVADO"
elif media >= 4 and media < 6:
  conceito = "D"
  resultado = "REPROVADO"
elif media >= 0 and media < 4:
  conceito = "E"
  resultado = "REPROVADO"

print("A media é: {:.2f}, Conceito: {}, {}".format(media, conceito, resultado))