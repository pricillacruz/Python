lista1 = ["Pri", "Maria", "Rob"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["abacaxi", 2, 5, "limão"]

lista1.append("Diego")
lista2.append(8)
lista3.append("morango")

print(lista1)
print(lista2)
print(lista3)


#fazendo alguma busca em uma das listas
if 7 in lista2:
	print("não tem 7 na lista2")

if 3 in lista2:
	print("tem 3 na lista2")


#deletando aguma coisa da lista
del lista2[5]
	print(lista2)