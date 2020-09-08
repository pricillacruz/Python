# condicional if

#Sintaxe do if: 
#if condição:
#	execute_esta_linha

x = 3
y = 9
z = 1

if x > z:
	print("x é maior que z")
else: 
	print("z é maior")

print("-------------")


if y < x:
	print("z é menor")
else:
	print("z é maior")

print("-------------")

#Caso precise fazer condições encadeadas utilize o elif
#Ele executa a primeira linha verdadeira
if x == y:
	print("numeros iguais")
elif y > x:
	print("y maior que x")
elif x < y:
	print("x menor que y")
else:
	print("numeros diferentes")