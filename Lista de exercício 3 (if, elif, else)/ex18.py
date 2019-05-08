"""
18. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é: 
 • par ou ímpar; 
 • positivo ou negativo; 
 • inteiro ou decimal. 
"""

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

operador = input(
    "Digite o simbolo da operação soma(+), subtração(-), divisão(/) ou multiplicação(*): "
)
while (operador != "+" and operador != "-" and operador != "/"
       and operador != "*"):
    print("Digite um OPERADOR valido")
    operador = input()

#VERIFICA O OPERADOR
if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "/":
    resultado = numero1 / numero2
else:
    resultado = numero1 * numero2

#VERIFICA SE É PAR OU IMPAR
if resultado % 2 == 0:
    resultadoParImpar = "par"
else:
    resultadoParImpar = "impar"

#VERIFICA SE É POSITIVO OU NEGATIVO
if resultado > 0:
    resultadoNegativoPositivo = "positivo"
else:
    resultadoNegativoPositivo = "negativo"

#VERIFICA SE É INTEIRO OU DECIMAL
if resultado.is_integer():
  resultadoInteiroDecimal = "inteiro"
else:
  resultadoInteiroDecimal = "decimal"


print("O resultado da operação {}{}{} = {}".format(numero1, operador, numero2, resultado))
print("O valor do resultado é", resultadoParImpar)
print("O valor do resultado é", resultadoNegativoPositivo)
print("O valor do resultado é", resultadoInteiroDecimal)