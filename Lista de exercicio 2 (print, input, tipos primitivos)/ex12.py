#12. A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco)
# prestações sem juros. Faça um algoritmo que receba um valor de uma compra
# e mostre o valor das prestações.

valorCompra = float(input("Valor da compra: R$"))

parcelas = 5
print("Parcelas:")
for i in range(parcelas):
    print(i+1,"x R${:.2f}".format(valorCompra/(i+1)))