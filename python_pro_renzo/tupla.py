#tupla = tuple(em inglês)
#tupla é imutável, ou seja, você não consegue incluir ou remover objetos dela
#A lista já é mutavel
#a impressão da lista é feita dentro de parenteses e não cochetes como a lista

tu = tuple(range(6))
print(tu)

#Linguagem precursora ABC
#ABC pegando cada posição do array
registro = ('Pricilla', 25)
nome, idade = registro
print(nome)
print(idade)

#você tem uma tupla chamada registro
#para pegar em partes essa lista, basta colocar as variaveis de com a ordem da lista e o que você deseja imprimir
registro = (2,'Pricilla', 25, 'libra')
quantidade, nome, idade, signo = registro
print(nome)
print(idade)
print(quantidade)
print(signo)

#Você pode concatenar as listas, e as mesmas não perdem seus valores
registro2 = (3, 'Maria', 34, 'Gemeos')
print(registro+registro2)
print(registro)
print(registro2)

#id, é um codigo unico para identificar o objeto
print(id(registro))
print(id(registro2))
print(id(registro+registro2))
