# 6.	Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.  

preco1 = float(input("Digite o primeiro preço: "))
preco2 = float(input("Digite o segundo preço: "))
preco3 = float(input("Digite o terceiro preço: "))

if preco1 < preco2 and preco1 < preco3:
  print("O preço menor é o {}".format(preco1))
elif preco2 < preco1 and preco2 < preco3:
  print("O preço menor é o {}".format(preco2))
elif preco3 < preco1 and preco3 < preco2:
  print("O preço menor é o {}".format(preco3))
else:
  print("Todos os preço são iguais")