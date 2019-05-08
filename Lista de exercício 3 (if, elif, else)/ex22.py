"""
22.	Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias:  infantil A = 5 - 7 anos; infantil B = 8-10 anos; juvenil A = 11-13 anos; juvenil B = 14-17 anos; adulto = maiores de 18 anos.

"""

idade = int(input("Idade do nadador: "))

if 5 <= idade <= 7:
  categoria = "infantil A"
elif 8 <= idade <= 10:
  categoria = "infantil B"
elif 11 <= idade <= 13:
  categoria = "juvenil A"
elif 14 <= idade <= 17:
  categoria = "juvenil B"
elif idade >= 18:
  categoria = "adulto"
elif 0 < idade < 5:
  categoria = "Idade abaixo do permitido!"
else:
  categoria = "Idade invalida!"

print(categoria)