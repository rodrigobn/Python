"""
2 - Escreva um programa que calcula a média de 30 alunos e informa a situação (reprovado, aprovado ou recuperação).

"""

for i in range(30):
  nota1 = float(input("Primeira nota: "))
  nota2 = float(input("Segunda nota: "))
  media = (nota1 + nota2) / 2
  if 0 <= media < 4:
    print("Reprovado")
  elif 4 <= media < 7:
    print("Recuperação")
  else:
    print("aprovado")