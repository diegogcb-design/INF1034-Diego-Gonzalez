from turtle import *

def soma_10(x):
    return x + 10

t = Turtle()
t.speed(0)

# Plano cartesiano

# Eixo dos X
t.pu()
t.goto(-300, 0)
t.pd()
t.goto(300, 0)
t.stamp()

# Eixo dos Y
t.pu()
t.goto(0, -300)
t.pd()
t.goto(0, 300)
t.lt(90)
t.stamp()

t.color("red")
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


mainloop()
