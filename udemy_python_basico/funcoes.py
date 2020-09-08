# def é uma palavra reservada para funções em Python
def soma(x, y):
	return x+y
s = soma(2, 3)


def subtrair(p, r):
	return p-r
sub = subtrair(4, 6)


#posso printar o resultado do s com o do sub e somar usando a def soma;
print(soma(s, sub))

#ou printar seus resultados separados
print(s)
print(sub)