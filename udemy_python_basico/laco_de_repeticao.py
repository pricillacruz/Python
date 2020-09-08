#while
x = 1 

while x < 10:
	print(x)
	x += 1

print("------------")

#for
lista1 = [1, 2, 3, 4, 5]
lista2 = ["ola", "mundo", "Pri"]
lista3 = [0, "Pricilla", 30, "dog", 10]


for i in lista1:
	print(i)
	

print("------------")
for i in lista2:
	print(i)
	

print("------------")
for i in lista3:
	print(i)

print("------------")
#Combinando for com o range
for i in range(11):
	print(i)

print("------------")
#vai imprimir de 10 a 20	
for i in range(10,20):
	print(i)

print("------------")
#vai imprimir de 10 a 20 de 2 em 2	
for i in range(10,20,2):
	print(i)