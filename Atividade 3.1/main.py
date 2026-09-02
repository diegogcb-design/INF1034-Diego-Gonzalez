import turtle
from turtle import *

from random import randint 

x = randint (10, 350)
y = randint (10, 350)

x2 = randint (-350, -50)
y2 = randint (10, 350)

x3 = randint(-350, -10)
y3 = randint(-350, -70)

x4 = randint (10, 350)
y4 = randint(-350, -90)

def desenha_quadrado(x,y, tam, cor):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for cont in range (4):
        # print (cont) pra ver que esta acontecendo
        t.fd(tam)
        t.lt(90)
    t.end_fill()

def desenha_pentagono (x2,y2,tam,cor):
    t.pu()
    t.goto(x2,y2)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for cont in range (5):
        t.forward(tam)  
        t.left(72)      
    t.end_fill()

def desenha_triangulo(x3,y3, tam,cor):
    t.pu()
    t.goto(x3,y3)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for cont in range (3):
        t.forward(tam)  
        t.left(120)      
    t.end_fill()

def desenha_hexagono (x4,y4,tam,cor):
    t.pu()
    t.goto(x4,y4)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for cont in range (6):
        t.forward(tam)  
        t.left(60)      
    t.end_fill()

t = Turtle()

t.pu()
t.goto(-400, 0)
t.pd()
t.goto(400, 0)
t.stamp()

t.pu()
t.goto(0, -400)
t.pd()
t.goto(0, 400)
t.lt(90)
t.stamp()
t.rt(90)

# for cont in range (4):
    # print (cont) pra ver que esta acontecendo
    # t.fd(100)
    # t.lt(90)

# versão sem repetição
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.lt(90)

cor = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica")
desenha_quadrado(x,y,60,cor)

cor = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica")
desenha_pentagono (x2,y2,45,cor)

cor = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica")
desenha_triangulo (x3,y3,77,cor)

cor = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica")
desenha_hexagono (x4,y4,77,cor)



t.pu()
t.goto(100, 100)      
t.setheading(0)       
t.pd()



for radio in range(1, 60, 2):
    t.circle(radio, 90)  

mainloop()