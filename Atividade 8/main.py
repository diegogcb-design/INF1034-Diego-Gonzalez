from pygame import *


# FUNÇÕES

# Verifica se o email termina com @puc.com
def valida_email(email):
    return email[-8:] == "@puc.com"


# Verifica se a senha possui letra maiúscula
def possui_maiuscula(senha):
    for carac in senha:
        if 'A' <= carac <= 'Z':
            return True
    return False


# Verifica se a senha possui letra minúscula
def possui_minuscula(senha):
    for carac in senha:
        if 'a' <= carac <= 'z':
            return True
    return False


# Verifica se a senha possui número
def possui_numero(senha):
    for carac in senha:
        if carac.isnumeric():
            return True
    return False


# Verifica se a senha é segura
def valida_senha(senha):
    if len(senha) < 8:
        return False

    if not possui_maiuscula(senha):
        return False

    if not possui_minuscula(senha):
        return False

    if not possui_numero(senha):
        return False

    return True


# Criptografia de César +3
def criptografa(senha):
    senha_cripto = ""

    for carac in senha:

        # Só aceita caracteres entre 0 e z da tabela ASCII
        if ord('0') <= ord(carac) <= ord('z'):

            pos_ascii = ord(carac) + 3

            # Se passar do z, volta para o começo
            if pos_ascii > ord('z'):
                pos_ascii = ord('0') + (pos_ascii - ord('z') - 1)

            senha_cripto += chr(pos_ascii)

    return senha_cripto


# CONFIGURAR PYGAME

init()

screen = display.set_mode((1280, 720))
running = True

clock = time.Clock()


# LOGIN

input_email = ""
input_senha = ""

etapa_login = "email"

mensagem = ""

fonte_login = font.Font(None, 50)
fonte_validation = font.Font(None, 25)


# CASINHA

# Fonte
fonte = font.Font(
    "Atividade 5.1 - Casinha melhorada/batmfa__.ttf",
    40
)

texto = fonte.render("BATMAN HOUSE", True, "black")


# Imagem
batman = image.load(
    "Atividade 5.1 - Casinha melhorada/batman.png"
)

batman = transform.scale(batman, (150, 150))


# Movimento da nuvem
nuvem_x = 750
vel_nuvem = 120


# Movimento do sol
sol_x = 170
sol_y = 120
vel_sol = 200


# Estágio do dia
estagio = "tarde"
estagio_anterior = ""


# LOOP PRINCIPAL

while running:

    clock.tick(60)


    # EVENTOS

    for ev in event.get():

        if ev.type == QUIT:
            running = False


        # LOGIN
        if etapa_login != "casinha":

            if ev.type == KEYDOWN:


                # EMAIL
                if etapa_login == "email":

                    if ev.key == K_BACKSPACE:
                        input_email = input_email[:-1]

                    elif ev.key == K_RETURN:

                        if valida_email(input_email):

                            mensagem = "Email válido! Digite sua senha."
                            etapa_login = "senha"

                        else:

                            mensagem = "Email inválido. Digite novamente."

                    else:
                        input_email += ev.unicode


                # SENHA
                elif etapa_login == "senha":

                    if ev.key == K_BACKSPACE:
                        input_senha = input_senha[:-1]

                    elif ev.key == K_RETURN:

                        if valida_senha(input_senha):

                            # Criptografar a senha
                            senha_criptografada = criptografa(
                                input_senha
                            )

                            print(
                                "Senha criptografada:",
                                senha_criptografada
                            )

                            mensagem = "Login realizado!"

                            # Abrir a casinha
                            etapa_login = "casinha"

                        else:

                            mensagem = "Senha não é segura."

                    else:
                        input_senha += ev.unicode


        # EVENTOS DA CASINHA
        else:

            if ev.type == MOUSEMOTION:
                sol_x, sol_y = ev.pos

            if ev.type == MOUSEBUTTONDOWN:

                if ev.button == 1:
                    sol_x, sol_y = ev.pos


    # TELA DE LOGIN

    if etapa_login != "casinha":

        screen.fill("white")


        # Título
        titulo = fonte_login.render(
            "LOGIN",
            True,
            "black"
        )

        screen.blit(titulo, (570, 100))


        # EMAIL

        texto_email = fonte_validation.render(
            "Email:",
            True,
            "black"
        )

        screen.blit(texto_email, (300, 220))


        draw.rect(
            screen,
            "black",
            (300, 250, 680, 60),
            3
        )


        email_render = fonte_login.render(
            input_email,
            True,
            "black"
        )

        screen.blit(
            email_render,
            (315, 255)
        )


        # SENHA

        texto_senha = fonte_validation.render(
            "Senha:",
            True,
            "black"
        )

        screen.blit(texto_senha, (300, 350))


        draw.rect(
            screen,
            "black",
            (300, 380, 680, 60),
            3
        )


        # Esconder a senha com *
        senha_escondida = "*" * len(input_senha)

        senha_render = fonte_login.render(
            senha_escondida,
            True,
            "black"
        )

        screen.blit(
            senha_render,
            (315, 385)
        )


        # MENSAGEM

        if mensagem != "":

            if (
                "inválido" in mensagem
                or "não" in mensagem
            ):
                cor_mensagem = "red"

            else:
                cor_mensagem = "green"


            mensagem_render = fonte_validation.render(
                mensagem,
                True,
                cor_mensagem
            )

            screen.blit(
                mensagem_render,
                (300, 480)
            )


        # Instrução
        instrucao = fonte_validation.render(
            "Pressione ENTER para continuar",
            True,
            "black"
        )

        screen.blit(
            instrucao,
            (300, 550)
        )


        display.update()

        # Não executar a casinha enquanto estiver no login
        continue


    # ------------------------------------------------
    # CASINHA
    # ------------------------------------------------

    dt = clock.get_time() / 1000


    # Movimento automático da nuvem

    nuvem_x = nuvem_x + vel_nuvem * dt


    # Inverter direção ao chegar nos limites da tela

    if nuvem_x + 250 >= 1280:
        vel_nuvem = -120

    elif nuvem_x - 55 <= 0:
        vel_nuvem = 120


    # Movimento do sol pelo teclado

    keys = key.get_pressed()


    if keys[K_RIGHT]:
        sol_x += vel_sol * dt

    if keys[K_LEFT]:
        sol_x -= vel_sol * dt

    if keys[K_DOWN]:
        sol_y += vel_sol * dt

    if keys[K_UP]:
        sol_y -= vel_sol * dt


    # Limites do sol e dos raios

    if sol_x < 115:
        sol_x = 115

    if sol_x > 1165:
        sol_x = 1165

    if sol_y < 110:
        sol_y = 110

    if sol_y > 610:
        sol_y = 610


    # Estágio do dia

    if sol_y > 450:

        background_color = "#1C274C"
        estagio = "noite"

    elif sol_y > 250:

        background_color = "#F7C873"
        estagio = "manha"

    else:

        background_color = "#87CEEB"
        estagio = "tarde"


    # Mudar música quando o estágio muda

    if estagio != estagio_anterior:

        # Parar música anterior
        mixer.music.stop()


        # Carregar música do estágio atual

        if estagio == "manha":

            mixer.music.load(
                "Atividade 5.1 - Casinha melhorada/manha.mp3"
            )


        elif estagio == "tarde":

            mixer.music.load(
                "Atividade 5.1 - Casinha melhorada/tarde.mp3"
            )


        elif estagio == "noite":

            mixer.music.load(
                "Atividade 5.1 - Casinha melhorada/noite.mp3"
            )


        # Tocar até mudar de estágio
        mixer.music.play(-1)


        # Guardar estágio atual
        estagio_anterior = estagio


    # DESENHAR CASINHA

    # Fundo
    screen.fill(background_color)


    # Grama
    draw.rect(
        screen,
        "green",
        (0, 600, 1280, 120)
    )


    # Casa
    draw.rect(
        screen,
        "#646464",
        (310, 360, 300, 240)
    )


    # Telhado
    draw.polygon(
        screen,
        "#FF0000",
        [
            (310, 360),
            (610, 360),
            (460, 250)
        ]
    )


    # Janela
    draw.rect(
        screen,
        "#172675",
        (340, 450, 80, 100)
    )


    # Porta
    draw.rect(
        screen,
        "#8B5A20",
        (460, 430, 100, 170)
    )


    # Maçaneta
    draw.circle(
        screen,
        "black",
        (475, 515),
        7
    )


    # Árvore - tronco
    draw.rect(
        screen,
        "#8B5A20",
        (900, 470, 55, 130)
    )


    # Árvore - copa
    draw.circle(
        screen,
        "#399C22",
        (928, 400),
        120
    )


    # SOL

    draw.circle(
        screen,
        "#FFF251",
        (sol_x, sol_y),
        55
    )


    # Raios do sol

    draw.line(
        screen,
        "#FFF251",
        (sol_x, sol_y - 70),
        (sol_x, sol_y - 110),
        8
    )

    draw.line(
        screen,
        "#FFF251",
        (sol_x, sol_y + 70),
        (sol_x, sol_y + 110),
        8
    )

    draw.line(
        screen,
        "#FFF251",
        (sol_x - 70, sol_y),
        (sol_x - 115, sol_y),
        8
    )

    draw.line(
        screen,
        "#FFF251",
        (sol_x + 70, sol_y),
        (sol_x + 115, sol_y),
        8
    )

    draw.line(
        screen,
        "#FFF251",
        (sol_x - 50, sol_y - 50),
        (sol_x - 85, sol_y - 85),
        8
    )

    draw.line(
        screen,
        "#FFF251",
        (sol_x + 50, sol_y - 50),
        (sol_x + 85, sol_y - 85),
        8
    )

    draw.line(
        screen,
        "#FFF251",
        (sol_x - 50, sol_y + 50),
        (sol_x - 85, sol_y + 85),
        8
    )

    draw.line(
        screen,
        "#FFF251",
        (sol_x + 50, sol_y + 50),
        (sol_x + 85, sol_y + 85),
        8
    )


    # NUVEM

    draw.circle(
        screen,
        "white",
        (nuvem_x, 100),
        55
    )

    draw.circle(
        screen,
        "white",
        (nuvem_x + 65, 95),
        60
    )

    draw.circle(
        screen,
        "white",
        (nuvem_x + 130, 100),
        60
    )

    draw.circle(
        screen,
        "white",
        (nuvem_x + 195, 100),
        55
    )


    # Texto
    screen.blit(
        texto,
        (500, 30)
    )


    # Imagem Batman
    screen.blit(
        batman,
        (1050, 450)
    )


    display.update()


# Parar música ao fechar
mixer.music.stop()

quit()