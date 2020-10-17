rosa, roxo, azul = map(int, input("Informe separado por virgula quantos participantes por cor: ").split(","))
total_participantes = rosa + roxo + azul

porcentagem_rosa = rosa / total_participantes * 100
porcentagem_roxo = roxo / total_participantes * 100
porcentagem_azul = azul / total_participantes * 100

print(f"{porcentagem_rosa:.2f} % de pessoas preferem rosa.")
print(f"{porcentagem_roxo:.2f} % de pessoas preferem roxo.")
print(f"{porcentagem_azul:.2f} % de pessoas preferem azul.")