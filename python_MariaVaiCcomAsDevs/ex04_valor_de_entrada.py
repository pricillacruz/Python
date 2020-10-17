# Faça um programa que receba o número de
# brindes do Maria vai com as Devs que a
# Jéssica vai mandar fazer, e imprima
# quanto de entrada ela irá que pagar.
# Considere que cada brinde custa R$25,00
# e a entrada para o fabricante é de 50% do valor total.

valorDoBrinde = 25
numeroDeBrinde = int(input('Digite o numero de brinde a ser produzido: '))
valorTotal = numeroDeBrinde * valorDoBrinde
valorDaEntrada = valorTotal/2
print(f"o valor total é {valorTotal} e o pagamento da entrada é {valorDaEntrada:.2f}")