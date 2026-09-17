from pygame import *

init()

screen = display.set_mode((1280, 720))
running = True

while running:

    for ev in event.get():
        if ev.type == QUIT:
            running = False

    # Fundo
    screen.fill("#97D1FA")

    display.update()

quit()