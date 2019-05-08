#15.	Escreva um programa que leia três números inteiros e positivos 
#(A, B, C) e calcule a seguinte expressão: 

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

R = (a+b)**2
S = (b+c)**2

D = (R+S)/2

print(D)