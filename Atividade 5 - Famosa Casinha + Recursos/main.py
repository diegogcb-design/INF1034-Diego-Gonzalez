from pygame import *

init()

screen = display.set_mode((1280, 720))
running = True

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


    display.update()

quit()