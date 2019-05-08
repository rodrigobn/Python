"""
4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. 
"""

contador = 0
letras = ["u","y","e","v","j","i","r","a","d","c"]
for i in range(len(letras)):
	if letras[i] != "a" and letras[i] != "e" and letras[i] != "i" and letras[i] != "o" and letras[i] != "u":
		contador += 1
		print("Consoante", letras[i])

print("Quantidade de consoantes", contador)