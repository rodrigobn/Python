#3. Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
media = 0
for i in range(4):
    nota = float(input('Digite a nota: '))
    media += nota
print("A media é:", media/4)