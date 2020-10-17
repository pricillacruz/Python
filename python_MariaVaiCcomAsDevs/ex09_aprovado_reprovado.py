nota_da_prova = float(input("Digite a nota da sua prova: "))
nota_do_trabalho = float(input("Digite a nota do seu trabalho: "))

if nota_da_prova >= 5 and nota_do_trabalho > 6:
  print('Aprovado!')
else:
  print('Reprovado!')