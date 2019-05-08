#3.	Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

sexo = input("Digite o sexo: ")

if sexo == "F":
  print("{} - Feminino".format(sexo))
elif sexo == "M":
  print("{} - Masculino".format(sexo))
else:
  print("Sexo invalido")