
nome = 'Pricilla'
#no lugar do v de valor
for v in nome:
    print(v)


#imprimindo o indice e seus valores
#range traz o valor
for i in range(len(nome)):
    print(i, nome[i])


#imprimindo o indice e seus valores
#Usando o enumerate
#i = indice
#v = valor
for i, v in enumerate(nome):
    print(i, nome[i])


#deixando mais simples ainda
#imprimindo o indice e seus valores
#Usando o enumerate
#i = indice
#v = valor
for i, v in enumerate(nome):
    print(i, v)