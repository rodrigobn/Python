#6. Faça um Programa que calcule a área de um quadrado, em seguida mostre 
# o dobro desta área para o usuário.
lado = float(input("Digite o valor do lado do quadrado: "))
area = lado ** 2
dobroArea = area * 2
print("O valor do dobro da área é = {:.2f}".format(dobroArea))