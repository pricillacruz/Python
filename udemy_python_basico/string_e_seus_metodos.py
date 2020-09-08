nome = "Pricilla"
sobrenome = "Souza"
idade = "25"

concatenar = nome + " " + sobrenome + " tem " + idade + " anos!!" + "\n"

#imprimir texto normal
print(concatenar)
print("--------")

#imprimir tudo em minusculo:
print(concatenar.lower())
print("--------")

#imprimir tudo e maiusculo
print(concatenar.upper())
print("--------")

#imprimir tudo sem espaço n final da concatenação
print(concatenar.strip())
print("--------")

#imprimir converte a sequencia em uma lista, a cada espaço separa as palavras
#e dentro do parenteses do split vc seleciona a regra que vai separar as palavras
#print(concatenar.split(" - "))
print(concatenar.split())
print("--------")

#imprimir buscas dos substring
#"tem" começa na posição i 15
print(concatenar.find("tem"))
print("--------")

#imprimir buscas dos substring
#a partir da palavra "tem" até o fim
busca = concatenar.find("tem")
print(concatenar[busca:])
print("--------")

#imprimir substitui partes de uma string
concatenar = concatenar.replace("tem", "está com ")
print(concatenar)
print("--------")