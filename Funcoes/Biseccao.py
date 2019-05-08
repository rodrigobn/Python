# encoding: utf-8
from copy import copy
from math import log10, ceil, fabs
	
def biseccao(intervalo = [0,0], condParada = 0):
	
	funcao = "x**3 - 9*x + 3"
	print("Função =",funcao)

	# numero aproximado de iterações
	k = (log10(intervalo[1] - intervalo[0])	- log10(condParada)) / log10(2)
	
	a = intervalo[0]
	b = intervalo[1]	
	
	print("Intervalo = [{}, {}]".format(a,b))

	#Arredonda pra cima o numero de iterações k
	for i in range(ceil(k)):
		#resultado da função no intervalo [a,b], subistituindo o x da função principal
		fa = a**3 - a + 1	
		fb = b**3 - b + 1
		
		#xn = ponto Medio do intervalo, subistituindo o x da função principal
		xn = (a+b)/2
		fxn = xn**3 - xn + 1
		
		# novo intervalo dividido ao meio dependendo da condição. [a, xn] ou [xn, b]
		if fa * fxn < 0:
			b = xn
						
		if fb * fxn < 0:
			a = xn
		
		print("[{}, {}]".format(a,b))
	return b, fxn

print("Ponto da raiz aproximada e valor = ", biseccao([-2,-1], 10**-6))
