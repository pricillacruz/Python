meu_dic = {"P": "Pricilla", "M": "Maria", "R": "Roberto", "D": "Diego"  }

#Para printar a alguma coisa do dicionario, 
#deve indicar as chaves e não o indice
print(meu_dic["M"])

#printar todas as chaves
for chave in meu_dic:
	print(chave)

#printar conteudo das chaves
for chave in meu_dic:
	print(meu_dic[chave])

#printar conteudo e as chaves
for chave in meu_dic:
	print(chave + " = " + meu_dic[chave])