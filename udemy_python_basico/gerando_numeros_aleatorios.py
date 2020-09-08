import random

#caso seja necessario forçar a escolha de um mesmo numero
#não necessariamente o numero 1
#não é muito utilizado
#random.seed(1)

#sortear de forma aleatoria
numero = random.randint(0, 10)
print(numero)

#escolher um numero de uma lista
lista = [6, 45, 9]
numero = random.choice(lista)
print(numero)