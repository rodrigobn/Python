#20.	Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores
# de forma que a variável A passe a possuir o valor da variável B e a variável B 
# passe a possuir o valor da variável A. Apresentar os valores trocados.

a = input("Valor de A: ")
b = input("Valor de B: ")

c = a
a = b
b = c

print("")
print("Valor de A = {} e valor de B = {}".format(a, b))