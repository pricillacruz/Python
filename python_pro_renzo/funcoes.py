#criando funções
#dois pontos identifica o inicio do escopo das funcoes
def ola_mundo():
    return 'Olá Mundo'

#chamando a função ola_mundo()
print(ola_mundo())


#função com "etiqueta" formatando a string
def ola(nome, sobrenome):
    return f'Olá {nome} {sobrenome}'

resultado = ola('Pri', 'Souza')

print(resultado)

#deixando um valor padrão(default)
def ola(nome, sobrenome = 'Silva'):
    return f'Olá {nome} {sobrenome}'

resultado = ola('Pri')

print(resultado)


#recebe numeros arbitrarios de parametros justapostos
def soma(*parcelas):
    i = 0
    for valor in parcelas:
        i += valor 
    return i

print(soma(3,4,3))