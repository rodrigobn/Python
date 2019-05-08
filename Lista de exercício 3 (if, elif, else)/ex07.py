# 7.	Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.  

print("Que turno você estuda? Digite uma das letras que prepresente o horario")
print("M - Matutino")
print("V - Vespertino")
print("N - Noturno")
horario = input()

if horario == "M":
  print("Bom Dia!")
elif horario == "V":
  print("Boa Tarde!")
elif horario == "N":
  print("Boa Noite!")
else:
  print("Valor Inválido!")