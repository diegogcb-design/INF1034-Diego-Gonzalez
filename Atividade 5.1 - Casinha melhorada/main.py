from pygame import *

init()

screen = display.set_mode((1280, 720))
running = True

clock = time.Clock()

# Fonte
fonte = font.Font("Atividade 5.1 - Casinha melhorada/batmfa__.ttf", 40)
texto = fonte.render("BATMAN HOUSE", True, "black")

# Imagem
batman = image.load("Atividade 5.1 - Casinha melhorada/batman.png")
batman = transform.scale(batman, (150, 150))

# Música inicial do Batman
#mixer.music.load("Atividade 5.1 - Casinha melhorada/batman_1966.mp3")
#mixer.music.play()

musica_inicial = True

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

while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False

        if ev.type == MOUSEMOTION:
            sol_x, sol_y = ev.pos

        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                sol_x, sol_y = ev.pos

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

    # Verificar se a música inicial do Batman terminou
    if musica_inicial:
        if not mixer.music.get_busy():
            musica_inicial = False
            estagio_anterior = ""

    # Mudar música dependendo do estágio
    if not musica_inicial and estagio != estagio_anterior:

        mixer.music.stop()

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

        # Repetir música do estágio até mudar
        mixer.music.play(-1)

        estagio_anterior = estagio

    # Fundo
    screen.fill(background_color)

    # Grama
    draw.rect(screen, "green", (0, 600, 1280, 120))

    # Casa
    draw.rect(screen, "#646464", (310, 360, 300, 240))

    # Telhado
    draw.polygon(
        screen,
        "#FF0000",
        [(310, 360), (610, 360), (460, 250)]
    )

    # Janela
    draw.rect(screen, "#172675", (340, 450, 80, 100))

    # Porta
    draw.rect(screen, "#8B5A20", (460, 430, 100, 170))

    # Maçaneta
    draw.circle(screen, "black", (475, 515), 7)

    # Árvore - tronco
    draw.rect(screen, "#8B5A20", (900, 470, 55, 130))

    # Árvore - copa
    draw.circle(screen, "#399C22", (928, 400), 120)

    # Sol
    draw.circle(screen, "#FFF251", (sol_x, sol_y), 55)

    # Raios do sol
    draw.line(
        screen, "#FFF251",
        (sol_x, sol_y - 70),
        (sol_x, sol_y - 110), 8
    )

    draw.line(
        screen, "#FFF251",
        (sol_x, sol_y + 70),
        (sol_x, sol_y + 110), 8
    )

    draw.line(
        screen, "#FFF251",
        (sol_x - 70, sol_y),
        (sol_x - 115, sol_y), 8
    )

    draw.line(
        screen, "#FFF251",
        (sol_x + 70, sol_y),
        (sol_x + 115, sol_y), 8
    )

    draw.line(
        screen, "#FFF251",
        (sol_x - 50, sol_y - 50),
        (sol_x - 85, sol_y - 85), 8
    )

    draw.line(
        screen, "#FFF251",
        (sol_x + 50, sol_y - 50),
        (sol_x + 85, sol_y - 85), 8
    )

    draw.line(
        screen, "#FFF251",
        (sol_x - 50, sol_y + 50),
        (sol_x - 85, sol_y + 85), 8
    )

    draw.line(
        screen, "#FFF251",
        (sol_x + 50, sol_y + 50),
        (sol_x + 85, sol_y + 85), 8
    )

    # Nuvem
    draw.circle(screen, "white", (nuvem_x, 100), 55)
    draw.circle(screen, "white", (nuvem_x + 65, 95), 60)
    draw.circle(screen, "white", (nuvem_x + 130, 100), 60)
    draw.circle(screen, "white", (nuvem_x + 195, 100), 55)

    # Texto
    screen.blit(texto, (500, 30))

    # Imagem
    screen.blit(batman, (1050, 450))

    display.update()

quit()