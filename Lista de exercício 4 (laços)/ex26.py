"""
26 - Uma grande firma deseja saber qual é o empregado mais recente e qual é o mais antigo. Desenvolver um programa para ler um número indeterminado de informações contendo o número do empregado e o número de meses de trabalho deste empregado e imprimir o mais recente e o mais antigo. Obs.: A última informação contém os dois números iguais a zero. Não existem dois empregados admitidos no mesmo mês.
"""

empregado = int(input("Digite o numero do empregado: "))
mesesTrabalhados = int(input("Digite o numero de meses trabalhados deste empregado: "))

empregadoMaisRecente = empregado
empregadoMaisAntigo = empregado

mesesMaisRecente = mesesTrabalhados
mesesMaisAntigo = mesesTrabalhados

while empregado != 0 and mesesTrabalhados != 0:
  empregado = int(input("Digite o numero do empregado: "))
  mesesTrabalhados = int(input("Digite o numero de meses trabalhados deste empregado: "))
  if empregado != 0 and mesesTrabalhados != 0:
    if mesesTrabalhados > mesesMaisAntigo:
      mesesMaisAntigo = mesesTrabalhados
      empregadoMaisAntigo = empregado
    elif mesesTrabalhados < mesesMaisRecente:
      mesesMaisRecente = mesesTrabalhados
      empregadoMaisRecente = empregado
    elif mesesTrabalhados == mesesMaisAntigo or mesesTrabalhados == mesesMaisRecente:
      print("Não existem dois empregados admitidos no mesmo mês!")
    
print("O empregado mais antigo é: ",empregadoMaisAntigo)
print("O empregado mais recente é: ",empregadoMaisRecente)