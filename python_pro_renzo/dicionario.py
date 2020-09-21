#criando dicionario
#primeiro você coloca a chave'br' dois ponto e seu valor 'Português'
linguas = {'br':'Português', 'eua':'Inglês', 'mexico': 'Espanhol'}

print(linguas['br'])
print(linguas['eua'])
print(linguas['mexico'])

#posso buscar essas chaves com get
print(linguas.get('eua'))

#posso buscar essas chaves com get e passar um segundo parametro caso seja uma chave invalida 
print(linguas.get('es', 'nao encotrado'))

#perguntando se alguma chave está dentro do dicionario
print('br' in linguas)
print('es' in linguas)


#perguntando se alguma chave está dentro da lista
print(5 in list(range(10)))
print('12' in list(range(10)))

#inserindo valor ao dicionario
linguas['es'] = 'spanhol'
print(linguas)

#atualizando alguma inclusão na lista
linguas['es'] = 'espanhol'
print(linguas)


#iterando com dicionario
for chave in linguas:
    print(chave)

#ser mais claro quando for iterar com dicionario - acrescenta o metodo keys()
#dá no mesmo que o anterior
for chave in linguas.keys():
    print(chave)


#imprimir valores com o metodo values()
for valor in linguas.values():
    print(valor)

    
#iterar tanto com as chaves e valores, utilize o metodo items()
for chave, valor in linguas.items():
    print(chave, valor)

#removendo elementos de um dicionario
linguas.pop('br')
print(linguas)

#deletar uilizando del
del linguas['es']
print(linguas)