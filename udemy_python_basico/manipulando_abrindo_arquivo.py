arquivo = open("meu_arquivo.txt")

#pega as linhas do arquivo e joga em uma lista
linhas = arquivo.readlines()

for linha in linhas:
	print(linha)

#mostrar arquivo completo
texto_completo = arquivo.read()

print(texto_completo)

