"""
10 - Faça um programa para calcular a área de N Círculos. Fórmula: Área = π raio2 π = 3,141592.
"""

circulos = int(input("Informe quantos circulos: "))

for i in range(circulos):
  raio = float(input("Informe o raio do circulo: "))
  area = 3.14 * (raio**2)
  print(area)