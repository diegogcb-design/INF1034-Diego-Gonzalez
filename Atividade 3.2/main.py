
from turtle import *
from time import sleep

t = Turtle()

# Bandeira do Reino Unido
# 1. Fundo azul
def fundo_azul():
    t.penup()
    t.goto(-300, -150)
    t.pendown()
    t.color("#00247D")
    t.begin_fill()

    for _ in range(2):
        t.fd(600)
        t.left(90)
        t.fd(300)
        t.left(90)

    t.end_fill()


# 2. Diagonais brancas
def diagonais_brancas():
    t.color("#FFFFFF")
    t.pensize(50)

    for y in [-150, 150]:
        t.penup()
        t.goto(-300, y)
        t.pendown()
        t.goto(300, -y)


# 3. Diagonais vermelhas
def diagonais_vermelhas():
    t.color("#C2112C")
    t.pensize(18)

    for y in [140, -140]:
        t.penup()
        t.goto(-280, y)
        t.pendown()
        t.goto(0, 0)
        t.goto(280, -y)


# 4. Cruz branca
def cruz_branca():
    t.pensize(1)
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.color("#FFFFFF")
    t.begin_fill()
    t.setheading(0)

    t.fd(50)
    t.left(90)
    t.fd(100)
    t.right(90)
    t.fd(250)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(250)
    t.right(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.right(90)
    t.fd(250)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(250)
    t.right(90)
    t.fd(100)
    t.left(90)
    t.fd(50)

    t.end_fill()


# 5. Cruz vermelha
def cruz_vermelha():
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.color("#C2112C")
    t.begin_fill()
    t.setheading(0)

    t.fd(30)
    t.left(90)
    t.fd(120)
    t.right(90)
    t.fd(270)
    t.left(90)
    t.fd(60)
    t.left(90)
    t.fd(270)
    t.right(90)
    t.fd(120)
    t.left(90)
    t.fd(60)
    t.left(90)
    t.fd(120)
    t.right(90)
    t.fd(270)
    t.left(90)
    t.fd(60)
    t.left(90)
    t.fd(270)
    t.right(90)
    t.fd(120)
    t.left(90)
    t.fd(30)

    t.end_fill()


# 1. Desenhar a bandeira do Reino Unido
def desenhar_bandeira_do_reino_unido():
    fundo_azul()
    diagonais_brancas()
    diagonais_vermelhas()
    cruz_branca()
    cruz_vermelha()

desenhar_bandeira_do_reino_unido()

sleep(2)
t.clear()


# 2. Desenhar a bandeira da Inglaterra

def desenhar_bandeira_inglaterra():
    cruz_vermelha()

    t.penup()
    t.goto(-300, -150)
    t.pendown()
    t.color("black")
    t.setheading(0)

    for _ in range(2):
        t.fd(600)
        t.left(90)
        t.fd(300)
        t.left(90)

sleep(2)
t.clear()


# Desenhar a bandeira da Georgia

desenhar_bandeira_inglaterra()

def desenhar_cruz(x, y):
    # parte vertical
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#C2112C")
    t.begin_fill()

    for i in range(2):
        t.fd(20)
        t.left(90)
        t.fd(60)
        t.left(90)

    t.end_fill()

    # parte horizontal
    t.penup()
    t.goto(x - 20, y + 20)
    t.pendown()
    t.begin_fill()

    for i in range(2):
        t.fd(60)
        t.left(90)
        t.fd(20)
        t.left(90)

    t.end_fill()

# 3. Desenhar a bandeira da Georgia

desenhar_bandeira_inglaterra()

# cruz encima esquerda
desenhar_cruz(-150, 75)

# cruz encima direita
desenhar_cruz(130, 75)

# cruz debaixo esquerda
desenhar_cruz(-150, -105)

# cruz debaixo direita
desenhar_cruz(130, -105)

sleep(2)
t.clear()


def bandeira_vertical(cor1, cor2, cor3):

    # Primeira faixa
    t.penup()
    t.goto(-300, -150)
    t.setheading(0)
    t.pendown()
    t.color(cor1)
    t.begin_fill()

    for i in range(2):
        t.fd(200)
        t.left(90)
        t.fd(300)
        t.left(90)

    t.end_fill()

    # Segunda faixa
    t.penup()
    t.goto(-100, -150)
    t.pendown()
    t.color(cor2)
    t.begin_fill()

    for i in range(2):
        t.fd(200)
        t.left(90)
        t.fd(300)
        t.left(90)

    t.end_fill()

    # Terceira faixa
    t.penup()
    t.goto(100, -150)
    t.pendown()
    t.color(cor3)
    t.begin_fill()

    for i in range(2):
        t.fd(200)
        t.left(90)
        t.fd(300)
        t.left(90)

    t.end_fill()

# 4. França
bandeira_vertical("#0055A4", "white", "#EF4135")
sleep(2)
t.clear()

# 5. Itália
bandeira_vertical("#009246", "white", "#CE2B37")
sleep(2)
t.clear()

# 6. Irlanda
bandeira_vertical("#169B62", "white", "#FF883E")
sleep(2)
t.clear()

# 7. Bélgica
bandeira_vertical("black", "#FDDA24", "#EF3340")
sleep(2)
t.clear()

def bandeira_horizontal(cor1, cor2, cor3):

    # Faixa superior
    t.penup()
    t.goto(-300, 50)
    t.setheading(0)
    t.pendown()
    t.color(cor1)
    t.begin_fill()

    for i in range(2):
        t.fd(600)
        t.left(90)
        t.fd(100)
        t.left(90)

    t.end_fill()

    # Faixa central
    t.penup()
    t.goto(-300, -50)
    t.pendown()
    t.color(cor2)
    t.begin_fill()

    for i in range(2):
        t.fd(600)
        t.left(90)
        t.fd(100)
        t.left(90)

    t.end_fill()

    # Faixa inferior
    t.penup()
    t.goto(-300, -150)
    t.pendown()
    t.color(cor3)
    t.begin_fill()

    for i in range(2):
        t.fd(600)
        t.left(90)
        t.fd(100)
        t.left(90)

    t.end_fill()

# 8. Alemanha
bandeira_horizontal("black", "#DD0000", "#FFCE00")
sleep(2)
t.clear()

# 9. Países Baixos
bandeira_horizontal("#AE1C28", "white", "#21468B")
sleep(2)
t.clear()

# 10. Áustria
bandeira_horizontal("#ED2939", "white", "#ED2939")
sleep(2)
t.clear()

# 11. Rússia
bandeira_horizontal("white", "#0039A6", "#D52B1E")
sleep(2)
t.clear()

# 12. Hungria
bandeira_horizontal("#CE2939", "white", "#477050")
sleep(2)
t.clear()

# 13. Luxemburgo
bandeira_horizontal("#EF3340", "white", "#00A3E0")
sleep(2)
t.clear()

# 14. Estônia
bandeira_horizontal("#0072CE", "black", "white")
sleep(2)
t.clear()

# 15. Serra Leoa
bandeira_horizontal("#1EB53A", "white", "#0072C6")
sleep(2)

# EXTRA - Escolher a bandeira

pais = t.textinput(
    "Escolher bandeira",
    "Qual bandeira você quer desenhar?"
)

if pais == "França":
    bandeira_vertical("#0055A4", "white", "#EF4135")

if pais == "Itália":
    bandeira_vertical("#009246", "white", "#CE2B37")

if pais == "Irlanda":
    bandeira_vertical("#169B62", "white", "#FF883E")

if pais == "Bélgica":
    bandeira_vertical("black", "#FDDA24", "#EF3340")

if pais == "Alemanha":
    bandeira_horizontal("black", "#DD0000", "#FFCE00")

if pais == "Países Baixos":
    bandeira_horizontal("#AE1C28", "white", "#21468B")

if pais == "Áustria":
    bandeira_horizontal("#ED2939", "white", "#ED2939")

if pais == "Rússia":
    bandeira_horizontal("white", "#0039A6", "#D52B1E")

if pais == "Hungria":
    bandeira_horizontal("#CE2939", "white", "#477050")

if pais == "Luxemburgo":
    bandeira_horizontal("#EF3340", "white", "#00A3E0")

if pais == "Estônia":
    bandeira_horizontal("#0072CE", "black", "white")

if pais == "Serra Leoa":
    bandeira_horizontal("#1EB53A", "white", "#0072C6")



mainloop()



mainloop()