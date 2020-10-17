
temperatura = int(input("Digite a temperatura: "))
umidade = int(input("Digite a umidade: "))

if temperatura < 10 or temperatura > 25:
  print("Nada acontece!")
else:
    if temperatura < 15:
        if umidade < 40:
             print("Blusa de frio e guarda chuva")
        else:
             print("Blusa de frio, regata e guarda-chuva")
    elif temperatura < 20:
        if umidade < 40:
             print("Blusa de frio e guarda chuva")
        else:
             print("Blusa de frio, regata e guarda-chuva")
    else:
        if umidade < 40:
             print("Regata")
        else:
             print("Regata e guarda-chuva")