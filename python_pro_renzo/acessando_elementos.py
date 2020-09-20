#acessando e percorrendo cada array dentro da variavel nome
nome = 'Pricilla'
print(nome[0])
print(nome[3])

#verificando o tamanho da string dentro da variavel nome
print(len(nome))

#printando o ultimo elemento
print(nome[len(nome)-1])

#printando o ultimo elemento de forma 'elegante' do pyhton
print(nome[-1])
print(nome[-2])

#fatiando o objeto com slice - pegando apenas um trecho especifico
print(nome[0:4])
print(nome[3:7])
print(nome[:-3])
print(nome[:3])

#pegando um indice do objeto de 2 em 2
print(nome[:6:2])

#printando o objeto de forma reversa
print(nome[::-1])
