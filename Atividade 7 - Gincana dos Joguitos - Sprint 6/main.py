
from random import choice

lista = ["banana", "laranja", "maca", "abacaxi", "kiwi"]
numeros = "1234567890"
jogar = "s"

while jogar == "s":

    palavra_aleatoria = choice(lista)
    palavra_oculta = "_ " * len(palavra_aleatoria)
    vidas = 6

    print(palavra_oculta)
    print("Vidas:", vidas)

    while "_" in palavra_oculta and vidas > 0:

        letra = input("Digite uma letra da palavra: ")

        if letra in palavra_aleatoria:

            palavra_aux = ""
            
            for i in range(len(palavra_aleatoria)):

                if letra == palavra_aleatoria[i]:
                    palavra_aux += letra + " "
                else:
                    palavra_aux += palavra_oculta[2*i] + " "

            palavra_oculta = palavra_aux

        elif letra in numeros:
                print("Numeros nao sao validos!")

        else:
            print("Errou!")
            vidas -= 1

        print(palavra_oculta)
        print("Vidas:", vidas)

    if "_" not in palavra_oculta:
        print("Parabéns! Você ganhou!")

    else:
        print("Você perdeu!")
        print("A palavra era:", palavra_aleatoria)

    jogar = input("Deseja jogar novamente? (sim/n): ")

print("Fim do jogo!")
