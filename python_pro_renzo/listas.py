#range é um parametro que inicia em 0 e finaliza um antes do numero colocado
#ele considera o primeiro que é zero(0 é inclusivo) e exclui o ultimo que é 11;
#por isso imprimirá a lista de [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista = list(range(11))
print(lista)

#Portanto range é uma progressão aritietica
#Posso controloar o numero inicial e final
#por isso imprimirá a lista de [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = list(range(1,11))
print(lista)

#Portanto range é uma progressão aritietica
#Posso controloar o numero inicial e final
#E ainda definir uma razão de lista, ex: lista de 2 em 2
#por isso imprimirá a lista de [1, 3, 5, 7, 9]
lista = list(range(1,11, 2))
print(lista)

#Criando lista decrescente
#Controlando valor inicial, final e razão
#por isso imprimirá a lista de [11, 9, 7, 5, 3]
lista = list(range(11,1, -2))
print(lista)


#utilizando metodos do py
#sort = ordenação
lista1 = list([1,4,3,2,8,6,4,5])
lista1.sort()
print(lista1)

#utilizando metodos do py
#append = inclui um valor final da lista
lista1 = list([1,4,3,2,8,6,4,5])
lista1.append(44)
print(lista1)

#utilizando metodos do py
#pop = remove o ultimo valor da lista e retorná-lo
lista1 = list([1,4,3,2,8,6,4,5])
lista1.pop()
print(lista1)

#utilizando metodos do py
#extend = acrescenta os numeros ao fim da lista
lista1 = list([1,4,3,2,8,6,4,5])
lista1.extend([12, 14, 15])
print(lista1)

#utilizando metodos do py
#+ = para concatenar lista com outra lista
lista1 = list([1,4,3,2,8,6,4,5])
print(lista1+[22,21, 25, 20])

#utilizando metodos do py
#* = multiplicando a lista por um numero inteiro
lista2 = [1,3,2]*3
print(lista2)

#utilizando metodos do py
#split = seprando as string em lista, como referencia o espaço
lista3 = 'Pricilla é arquiteta desenvolvedora e QA'.split(' ')
print(lista3)

#utilizando metodos do py
#split = seprando as string em lista, como referencia o hifen
lista3 = 'Pricilla-é-arquiteta-desenvolvedora-e-QA'.split('-')
print(lista3)

#utilizando metodos do py
#join = unindo a lista em uma unica string com separador espaço
lista4 = ['Pricilla', 'é', 'arquiteta', 'desenvolvedora', 'e', 'QA']
print(' '.join(lista4))

#lembre-se que na lista podemos colocar qualquer objeto
lista5 = [1, 1.0, 'Pricilla', []]
print(lista5)