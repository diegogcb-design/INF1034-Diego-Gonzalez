from pygame import *

init()

screen = display.set_mode((1280, 720))
running = True

# Fonte
fonte = font.Font("Atividade 5 - Famosa Casinha + Recursos/batmfa__.ttf", 40)
texto = fonte.render("BATMAN HOUSE", True, "black")

# Imagem
batman = image.load("Atividade 5 - Famosa Casinha + Recursos/batman.png")
batman = transform.scale(batman, (150, 150))

mixer.music.load("Atividade 5 - Famosa Casinha + Recursos/batman_1966.mp3")
mixer.music.play(-1)

while running:

    for ev in event.get():
        if ev.type == QUIT:
            running = False

    # Fundo
    #draw.rect(screen, color, (x, y, largura, altura))
    screen.fill("#97D1FA")

    #grama
    draw.rect(screen, "green", (0, 600, 1280, 120))

    # Casa
    draw.rect(screen, "#646464", (310, 360, 300, 240))

    # Telhado
    draw.polygon(screen, "#FF0000", [(310, 360), (610, 360), (460, 250)])



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

    draw.circle(screen, "#FFF251", (170, 120), 55)

    # Raios do sol

    draw.line(screen, "#FFF251", (170, 50), (170, 10), 8)

    draw.line(screen, "#FFF251", (170, 190), (170, 230), 8)

    draw.line(screen, "#FFF251", (100, 120), (55, 120), 8)

    draw.line(screen, "#FFF251", (240, 120), (285, 120), 8)

    draw.line(screen, "#FFF251", (120, 70), (85, 35), 8)

    draw.line(screen, "#FFF251", (220, 70), (255, 35), 8)

    draw.line(screen, "#FFF251", (120, 170), (85, 205), 8)

    draw.line(screen, "#FFF251", (220, 170), (255, 205), 8)

    # Nuvem

    draw.circle(screen, "white", (750, 100), 55)

    draw.circle(screen, "white", (815, 95), 60)

    draw.circle(screen, "white", (880, 100), 60)

    draw.circle(screen, "white", (945, 100), 55)

    # Texto
    screen.blit(texto, (500, 30))

    # Imagem
    screen.blit(batman, (1050, 450))

    display.update()

quit()