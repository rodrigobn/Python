"""
9 - Faça um programa para calcular a área de N quadriláteros. Fórmula: Área = Lado * Lado.
"""

quadrados = int(input("Informe quantos quadrados: "))

for i in range(quadrados):
  lado = float(input("Informe o lado do quadrado: "))
  area = lado * lado
  print(area)