from random import choice

print("Escolha um jogo:")
print("1 - Jogo da Forca")
print("2 - Pedra, Papel e Tesoura")

jogo = input("Digite sua escolha: ")


# JOGO DA FORCA

if jogo == "1":

    lista = ["banana", "laranja", "maca", "abacaxi", "kiwi"]
    jogar = "s"

    while jogar == "s":

        # choice escolhe uma palavra aleatoria da lista
        palavra_aleatoria = choice(lista)

        # len conta quantas letras tem a palavra e cria a mesma quantidade de "_"
        palavra_oculta = "_ " * len(palavra_aleatoria)

        vidas = 6

        print(palavra_oculta)
        print("Vidas:", vidas)

        # o jogo continua enquanto ainda tiver "_" na palavra e o jogador tiver vidas
        while "_" in palavra_oculta and vidas > 0:

            letra = input("Digite uma letra ou chute a palavra: ").lower()

            # isalpha verifica se o usuario digitou somente letras
            if not letra.isalpha():
                print("Apenas letras sao validas!")

            # permite que o jogador chute a palavra inteira
            elif letra == palavra_aleatoria:
                palavra_oculta = ""

                # mostra todas as letras da palavra quando o jogador acerta
                for i in range(len(palavra_aleatoria)):
                    palavra_oculta += palavra_aleatoria[i] + " "

            # len maior que 1 significa que o jogador tentou chutar uma palavra
            # se chegou aqui, significa que a palavra estava errada
            elif len(letra) > 1:
                print("Palavra errada!")
                vidas -= 1

            elif letra in palavra_aleatoria:

                palavra_aux = ""

                # percorre cada posicao da palavra para encontrar a letra
                for i in range(len(palavra_aleatoria)):

                    if letra == palavra_aleatoria[i]:
                        palavra_aux += letra + " "
                    else:
                        # 2*i serve porque palavra_oculta tem um espaco depois de cada letra
                        palavra_aux += palavra_oculta[2*i] + " "

                palavra_oculta = palavra_aux

            else:
                print("Errou!")
                vidas -= 1

            print(palavra_oculta)
            print("Vidas:", vidas)

        # se nao tem mais "_" significa que todas as letras foram descobertas
        if "_" not in palavra_oculta:
            print("Parabens! Voce ganhou!")

        else:
            print("Voce perdeu!")
            print("A palavra era:", palavra_aleatoria)

        jogar = input("Deseja jogar novamente? (s/n): ").lower()

    print("Fim do jogo!")


# PEDRA, PAPEL E TESOURA

elif jogo == "2":

    opcoes = ["pedra", "papel", "tesoura"]
    jogar = "s"
    pontos = 0

    while jogar == "s":

        jogador = input("Escolha pedra, papel ou tesoura: ").lower()

        # o computador escolhe uma opcao aleatoria da lista
        computador = choice(opcoes)

        print("Voce escolheu:", jogador)
        print("O computador escolheu:", computador)

        if jogador == computador:
            print("Empate!")

        # as proximas tres condicoes verificam todas as formas do jogador ganhar
        elif jogador == "pedra" and computador == "tesoura":
            print("Voce ganhou!")
            pontos += 1

        elif jogador == "tesoura" and computador == "papel":
            print("Voce ganhou!")
            pontos += 1

        elif jogador == "papel" and computador == "pedra":
            print("Voce ganhou!")
            pontos += 1

        # se a escolha existe mas nao ganhou e nao empatou, entao perdeu
        elif jogador == "pedra" and computador == "papel":
            print("Voce perdeu!")

        elif jogador == "papel" and computador == "tesoura":
            print("Voce perdeu!")

        elif jogador == "tesoura" and computador == "pedra":
            print("Voce perdeu!")

        # se nao escreveu nenhuma das tres opcoes
        else:
            print("Opcao invalida!")

        print("Pontuacao:", pontos)

        jogar = input("Deseja jogar novamente? (s/n): ").lower()

    print("Fim do jogo!")


else:
    print("Jogo invalido!")