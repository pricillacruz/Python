# Crie um loop que, para sair dele a pessoa deve digitar a palavra sair.
while True:
    palavra = input("Digite a palavra secreta para sair: ")
    if palavra == "sair":
        print("Fim")
        break;

    if len(palavra) <= 2:
        print("Palavra muito pequena!")
        continue

    print("Digite \"sair\" para sair!")


# Enquanto a soma for menor que 20, peça um numero

soma = 0
while soma <= 20:
  soma += int(input("Digite um número: "))

print(f"A soma total foi de {soma}")

