
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


# Desenhar a bandeira do Reino Unido
def desenhar_bandeira_do_reino_unido():
    fundo_azul()
    diagonais_brancas()
    diagonais_vermelhas()
    cruz_branca()
    cruz_vermelha()

desenhar_bandeira_do_reino_unido()

sleep(2)
t.clear()


# Desenhar a bandeira da Inglaterra

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


desenhar_bandeira_inglaterra()

sleep(2)
t.clear()

# Bandeira da Georgia

desenhar_bandeira_inglaterra()



# cruz encima izquerda
t.penup()
t.goto(-150, 75)
t.pendown()
t.color("#C2112C")
t.begin_fill()

for i in range(2):
    t.fd(20)
    t.left(90)
    t.fd(60)
    t.left(90)

t.end_fill()

t.penup()
t.goto(-170, 95)
t.pendown()
t.color("#C2112C")
t.begin_fill()

for i in range(2):

    t.fd(60)
    t.left(90)
    t.fd(20)
    t.left(90)

t.end_fill()

# cruz encima direita
t.penup()
t.goto(130, 75)
t.pendown()
t.color("#C2112C")
t.begin_fill()

for i in range(2):
    t.fd(20)
    t.left(90)
    t.fd(60)
    t.left(90)

t.end_fill()

t.penup()
t.goto(110, 95)
t.pendown()
t.color("#C2112C")
t.begin_fill()

for i in range(2):
    t.fd(60)
    t.left(90)
    t.fd(20)
    t.left(90)

t.end_fill()

# cruz debaixo izquerda
t.penup()
t.goto(-150, -105)
t.pendown()
t.color("#C2112C")
t.begin_fill()

for i in range(2):
    t.fd(20)
    t.left(90)
    t.fd(60)
    t.left(90)

t.end_fill()

t.penup()
t.goto(-170, -85)
t.pendown()
t.color("#C2112C")
t.begin_fill()

for i in range(2):
    t.fd(60)
    t.left(90)
    t.fd(20)
    t.left(90)

t.end_fill()

# cruz debaixo direita
t.penup()
t.goto(130, -105)
t.pendown()
t.color("#C2112C")
t.begin_fill()

for i in range(2):
    t.fd(20)
    t.left(90)
    t.fd(60)
    t.left(90)

t.end_fill()

t.penup()
t.goto(110, -85)
t.pendown()
t.color("#C2112C")
t.begin_fill()

for i in range(2):
    t.fd(60)
    t.left(90)
    t.fd(20)
    t.left(90)

t.end_fill()
sleep(2)
t.clear()


# Bandeira da Franca
t.penup()
t.goto(-300, -150)
t.pendown()
t.color("#0055A4")

t.begin_fill()

for i in range(2):

    t.fd(200)
    t.left(90)
    t.fd(300)
    t.left(90)

t.end_fill()

# Franja blanca

t.penup()
t.goto(-100, -150)
t.pendown()
t.color("white")
t.begin_fill()

for i in range(2):

    t.fd(200)
    t.left(90)
    t.fd(300)
    t.left(90)

t.end_fill()

# Franja roja

t.penup()
t.goto(100, -150)
t.pendown()
t.color("#EF4135")
t.begin_fill()

for i in range(2):

    t.fd(200)
    t.left(90)
    t.fd(300)
    t.left(90)

t.end_fill()

sleep(2)
t.clear()

# Bandeira da Escocia
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


# 2. Diagonais Brancas 
t.color("#FFFFFF")
t.pensize(50)

t.penup()
t.goto(-300, -150)
t.pendown()
t.goto(300, 150)

t.penup()
t.goto(-300, 150)
t.pendown()
t.goto(300, -150)

sleep(2)
t.clear()


# 1. Bandeira da Itália

# Verde
t.penup()
t.goto(-300, -150)
t.setheading(0)
t.pendown()
t.pensize(1)
t.color("#009246")
t.begin_fill()

for i in range(2):
    t.fd(200)
    t.left(90)
    t.fd(300)
    t.left(90)

t.end_fill()

# Branco
t.penup()
t.goto(-100, -150)
t.setheading(0)
t.pendown()
t.color("white")
t.begin_fill()

for i in range(2):
    t.fd(200)
    t.left(90)
    t.fd(300)
    t.left(90)

t.end_fill()

# Vermelho
t.penup()
t.goto(100, -150)
t.setheading(0)
t.pendown()
t.color("#CE2B37")
t.begin_fill()

for i in range(2):
    t.fd(200)
    t.left(90)
    t.fd(300)
    t.left(90)

t.end_fill()

sleep(2)
t.clear()


# 2. Bandeira da Irlanda

# Verde
t.penup()
t.goto(-300, -150)
t.setheading(0)
t.pendown()
t.color("#169B62")
t.begin_fill()

for i in range(2):
    t.fd(200)
    t.left(90)
    t.fd(300)
    t.left(90)

t.end_fill()

# Branco
t.penup()
t.goto(-100, -150)
t.setheading(0)
t.pendown()
t.color("white")
t.begin_fill()

for i in range(2):
    t.fd(200)
    t.left(90)
    t.fd(300)
    t.left(90)

t.end_fill()

# Laranja
t.penup()
t.goto(100, -150)
t.setheading(0)
t.pendown()
t.color("#FF883E")
t.begin_fill()

for i in range(2):
    t.fd(200)
    t.left(90)
    t.fd(300)
    t.left(90)

t.end_fill()

sleep(2)
t.clear()


# 3. Bandeira da Bélgica

# Preto
t.penup()
t.goto(-300, -150)
t.setheading(0)
t.pendown()
t.color("black")
t.begin_fill()

for i in range(2):
    t.fd(200)
    t.left(90)
    t.fd(300)
    t.left(90)

t.end_fill()

# Amarelo
t.penup()
t.goto(-100, -150)
t.setheading(0)
t.pendown()
t.color("#FDDA24")
t.begin_fill()

for i in range(2):
    t.fd(200)
    t.left(90)
    t.fd(300)
    t.left(90)

t.end_fill()

# Vermelho
t.penup()
t.goto(100, -150)
t.setheading(0)
t.pendown()
t.color("#EF3340")
t.begin_fill()

for i in range(2):
    t.fd(200)
    t.left(90)
    t.fd(300)
    t.left(90)

t.end_fill()

sleep(2)
t.clear()


# 4. Bandeira da Alemanha

# Preto
t.penup()
t.goto(-300, 50)
t.setheading(0)
t.pendown()
t.color("black")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Vermelho
t.penup()
t.goto(-300, -50)
t.setheading(0)
t.pendown()
t.color("#DD0000")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Amarelo
t.penup()
t.goto(-300, -150)
t.setheading(0)
t.pendown()
t.color("#FFCE00")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

sleep(2)
t.clear()


# 5. Bandeira dos Países Baixos

# Vermelho
t.penup()
t.goto(-300, 50)
t.setheading(0)
t.pendown()
t.color("#AE1C28")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Branco
t.penup()
t.goto(-300, -50)
t.setheading(0)
t.pendown()
t.color("white")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Azul
t.penup()
t.goto(-300, -150)
t.setheading(0)
t.pendown()
t.color("#21468B")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

sleep(2)
t.clear()


# 6. Bandeira da Áustria

# Vermelho superior
t.penup()
t.goto(-300, 50)
t.setheading(0)
t.pendown()
t.color("#ED2939")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Branco
t.penup()
t.goto(-300, -50)
t.setheading(0)
t.pendown()
t.color("white")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Vermelho inferior
t.penup()
t.goto(-300, -150)
t.setheading(0)
t.pendown()
t.color("#ED2939")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

sleep(2)
t.clear()


# 7. Bandeira da Rússia

# Branco
t.penup()
t.goto(-300, 50)
t.setheading(0)
t.pendown()
t.color("white")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Azul
t.penup()
t.goto(-300, -50)
t.setheading(0)
t.pendown()
t.color("#0039A6")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Vermelho
t.penup()
t.goto(-300, -150)
t.setheading(0)
t.pendown()
t.color("#D52B1E")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

sleep(2)
t.clear()


# 8. Bandeira da Hungria

# Vermelho
t.penup()
t.goto(-300, 50)
t.setheading(0)
t.pendown()
t.color("#CE2939")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Branco
t.penup()
t.goto(-300, -50)
t.setheading(0)
t.pendown()
t.color("white")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Verde
t.penup()
t.goto(-300, -150)
t.setheading(0)
t.pendown()
t.color("#477050")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

sleep(2)
t.clear()


# 9. Bandeira de Luxemburgo

# Vermelho
t.penup()
t.goto(-300, 50)
t.setheading(0)
t.pendown()
t.color("#EF3340")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Branco
t.penup()
t.goto(-300, -50)
t.setheading(0)
t.pendown()
t.color("white")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Azul claro
t.penup()
t.goto(-300, -150)
t.setheading(0)
t.pendown()
t.color("#00A3E0")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

sleep(2)
t.clear()


# 10. Bandeira da Estônia

# Azul
t.penup()
t.goto(-300, 50)
t.setheading(0)
t.pendown()
t.color("#0072CE")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Preto
t.penup()
t.goto(-300, -50)
t.setheading(0)
t.pendown()
t.color("black")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Branco
t.penup()
t.goto(-300, -150)
t.setheading(0)
t.pendown()
t.color("white")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

sleep(2)
t.clear()


# 11. Bandeira de Serra Leoa

# Verde
t.penup()
t.goto(-300, 50)
t.setheading(0)
t.pendown()
t.color("#1EB53A")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Branco
t.penup()
t.goto(-300, -50)
t.setheading(0)
t.pendown()
t.color("white")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()

# Azul
t.penup()
t.goto(-300, -150)
t.setheading(0)
t.pendown()
t.color("#0072C6")
t.begin_fill()

for i in range(2):
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)

t.end_fill()
sleep(2)

mainloop()