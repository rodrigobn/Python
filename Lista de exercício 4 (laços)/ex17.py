"""
17 - Faça um programa que mostre os n termos da Série a seguir: 

  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série. 

"""
n = int(input("Digite a quantidade de termos: "))

somatorio = 0
for i in range(1, n+1):
  somatorio += i/(i + i - 1)
  print("{}/{}".format(i, i + (i - 1)))

print("{:.2f}".format(somatorio))