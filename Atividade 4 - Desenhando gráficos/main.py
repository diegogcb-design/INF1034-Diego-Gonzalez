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



mainloop()
