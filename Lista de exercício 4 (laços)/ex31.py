"""
31 - O cardápio de uma lanchonete é o seguinte: 

Especificação 	  Código 	 	Preço
Cachorro Quente    100     	R$ 1,20
Bauru Simples      101     	R$ 1,30
Bauru com ovo      102     	R$ 1,50
Hambúrguer         103     	R$ 1,20
Cheeseburguer      104     	R$ 1,30
Refrigerante       105     	R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado

"""

totalPedido = 0
cardapioProduto = {
    100: "Cachorro Quente",
    101: "Bauru Simples",
    102: "Bauru com ovo",
    103: "Hambúrguer",
    104: "Cheeseburguer",
    105: "Refrigerante"
}
cardapioValor = {100: 1.2, 101: 1.3, 102: 1.5, 103: 1.2, 104: 1.3, 105: 1}
pedido = int(
    input("""
Especificação 	  Código 	Preço
Cachorro Quente    100     	R$ 1,20
Bauru Simples      101     	R$ 1,30
Bauru com ovo      102     	R$ 1,50
Hambúrguer         103     	R$ 1,20
Cheeseburguer      104     	R$ 1,30
Refrigerante       105     	R$ 1,00

Escolha o codigo do produto(digite 0 para finalizar):"""))

if pedido != 0:
    quantidade = int(input("Digite a quantidade: "))
    for i in cardapioValor:
        if i == pedido:
            print("""
Produto: {}
Quantidade: {}
O valor do pedido é: R${:.2f}""".format(cardapioProduto[i], quantidade,
                                        cardapioValor[i] * quantidade))
            totalPedido += cardapioValor[i] * quantidade

while pedido != 0:
    pedido = int(
        input("""
Especificação 	  Código 	Preço
Cachorro Quente    100     	R$ 1,20
Bauru Simples      101     	R$ 1,30
Bauru com ovo      102     	R$ 1,50
Hambúrguer         103     	R$ 1,20
Cheeseburguer      104     	R$ 1,30
Refrigerante       105     	R$ 1,00
  
Escolha o codigo do produto(digite 0 para finalizar):"""))
    if pedido != 0:
        quantidade = int(input("Digite a quantidade: "))
        for i in cardapioValor:
            if i == pedido:
                print("""
Produto: {}
Quantidade: {}
O valor do pedido é: R${:.2f}""".format(cardapioProduto[i], quantidade,
                                        cardapioValor[i] * quantidade))
                totalPedido += cardapioValor[i] * quantidade

print("O total do pedido foi de R${:.2f}".format(totalPedido))