from turtle import *

def soma_10(x):
    return x + 10

t = Turtle()
grafica = Turtle()
t.speed(0)

# Plano cartesiano

# Eixo dos X
grafica.pu()
grafica.goto(-300, 0)
grafica.pd()
grafica.goto(300, 0)
grafica.stamp()

# Eixo dos Y
grafica.pu()
grafica.goto(0, -300)
grafica.pd()
grafica.goto(0, 300)
grafica.lt(90)
grafica.stamp()


# t.pu()
# t.goto(-100, soma_10(-100))
# t.pd()
# t.goto(100, soma_10(100))

# O range vai do primeiro valor até o último -1
# print(list(range(-100, 100)))

# for x in range(-100, 100):
#     print(x)


#y = √x
def raiz(x):
    y= x ** 0.5
    return y 

t.color("red")
t.pu()
t.goto(0,0)
t.pd()
for x in range (0,101):
    y= raiz(x)
    t.goto(x*3, y*15)
t.up()
t.clear()

#y = 1/x
t.goto(0,0)
def inversa(x):
    y= 1/x
    return y

t.color("red")
t.pu()
for x in range(-100, 0):
    y = inversa(x)
    t.goto(x * 3, y * 100)
    t.pd()

t.color("red")
t.pu()
for x in range(1, 101):
    y = inversa(x)
    t.goto(x * 3, y * 100)
    t.pd()
t.clear()


#y = 2^x
def dois_elevado_a(x):
    y= 2 ** x
    return y 

t.color("red")
t.pu()
t.goto(-10*5,dois_elevado_a(-10)*15)
t.pd()
t.speed(1)
for x in range (-10,5):
    y= dois_elevado_a(x)
    t.goto(x*5, y*15)
t.up()
t.clear()

# y = 5 - x^2
def cinco_menos_x_ao_quadrado(x):
    y = 5 - x ** 2
    return y

t.color("red")
t.pu()
t.goto(-8*15,cinco_menos_x_ao_quadrado(-8)*5)
t.pd()
for x in range (-8,9):
    y= cinco_menos_x_ao_quadrado(x)
    t.goto(x*15, y*5)
t.up()
t.clear()

#y = x^2 - 5x + 6
def x_ao_quadrado_menos_5x_mais_6(x):
    y = x ** 2 - 5 * x + 6
    return y

t.color("red")
t.pu()
t.goto(-10*15,x_ao_quadrado_menos_5x_mais_6(-10)*2)
t.pd()
for x in range (-9,16):
    y= x_ao_quadrado_menos_5x_mais_6(x)
    t.goto(x*15, y*2)   
t.up()  
t.clear()

#y = x^3 - x^2 - x + 1
def x_ao_cubo_menos_x_ao_quadrado_menos_x_mais_1(x):
    y = x ** 3 - x ** 2 - x + 1
    return y

t.color("red")
t.pu()
t.goto(-5*15,x_ao_cubo_menos_x_ao_quadrado_menos_x_mais_1(-5)*2)
t.pd()
for x in range (-4,7):
    y= x_ao_cubo_menos_x_ao_quadrado_menos_x_mais_1(x)
    t.goto(x*15, y*2)
t.up()
t.clear()   

#extra
import turtle as t
import random

def corrida_de_tartarugas(N):

    tartaruga1 = t.Turtle()
    tartaruga2 = t.Turtle()

    tartaruga1.shape("turtle")
    tartaruga2.shape("turtle")

    tartaruga1.penup()
    tartaruga2.penup()

    tartaruga1.goto(-300, 50)
    tartaruga2.goto(-300, -50)

    for i in range(N):
        tartaruga1.forward(random.randint(1, 10))
        tartaruga2.forward(random.randint(1, 10))


corrida_de_tartarugas(100)

t.done()

mainloop()
