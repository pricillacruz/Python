numeroParticipantes = int(input('Dígite o número de participantes do minicurso:'))
litrosRefrigerante = 0.4 * numeroParticipantes
precoRefrigerante = litrosRefrigerante * 4

coxinhas = 10 * numeroParticipantes
precoCoxinhas = coxinhas * 0.50

valorTotal = precoCoxinhas + precoRefrigerante

print(f"Serão necessarios comprar {litrosRefrigerante:.2f} litros de refrigerante")
print(f"Serão necessarios comprar {coxinhas} de coxinhas")
print(f"O valor total ficou:  {valorTotal}")