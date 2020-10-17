vagas_disponiveis = int(input("Número de vagas disponiveis: "))
pessoas_participou = int(input("Número de pessoas que já participaram: "))
pessoas_interessadas = int(input("Número de pessoas interessadas: "))

if pessoas_interessadas == vagas_disponiveis:
  print("Todos irão! Oba!")
elif (pessoas_interessadas - pessoas_participou) <= vagas_disponiveis:
  print("Irá apenas quem não foi ainda!")
else:
  print("Haverá sorteio!")