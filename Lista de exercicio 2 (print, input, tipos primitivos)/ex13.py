#13. Faça um algoritmo que receba o preço de custo de um produto e mostre o 
#valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo 
#com um percentual informado pelo usuário.

custo = float(input("Valor de custo R$"))
acrescimo = float(input("Porcentagem de acréscimo (%): "))

valorVenda = (custo * acrescimo / 100) +custo

print("Valor de venda R${:.2f}".format(valorVenda))