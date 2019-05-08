"""
13.	Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações: 

•	Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado; 
•	Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa; 
•	Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário; 
•	Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 
 
"""
print("ax2 + bx + c")
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a != 0:
  delta = (b**2) - (4 * a * c)
  if delta < 0:
    print("Delta negativo({:.2f}). Não existe raizes reais".format(delta))
  elif delta == 0:
    print("Delta = 0. A equação possui apenas uma raiz real")
  elif delta > 0:
    print("Delta positivo({:.2f}), a equação possui duas raiz reais".format(delta))
else:
  print("a = {}. A equação não é do segundo grau".format(a))