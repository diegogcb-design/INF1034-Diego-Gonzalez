import turtle
from turtle import *


t = Turtle()
t.shape("turtle")

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

# t.penup
t.pu()
t.goto(200,200)
t.pd()

t.color("violet")
t.fillcolor("blue")
t.begin_fill()
for cont in range (4):
    # print (cont) pra ver que esta acontecendo
    t.fd(100)
    t.lt(90)
t.end_fill()


t.pu()
t.goto(-200,200)
t.pd()

t.color("violet")
var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica")
t.fillcolor(var_color)
t.begin_fill()
for cont in range (5):
    t.forward(100)  
    t.left(72)      
t.end_fill()

t.pu()
t.goto(-200,-200)
t.pd()


t.color("green")
var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica")
t.fillcolor(var_color)
t.begin_fill()
for cont in range (3):
    t.forward(100)  
    t.left(120)      
t.end_fill()

t.pu()
t.goto(200,-200)
t.pd()

t.color("orange")
var_color = textinput("Escolha da cor", "Digite a cor da próxima forma geométrica")
t.fillcolor(var_color)
t.begin_fill()
for cont in range (6):
    t.forward(100)  
    t.left(60)      
t.end_fill()

t.pu()
t.goto(100, 100)      
t.setheading(0)       
t.pd()



for radio in range(1, 60, 2):
    t.circle(radio, 90)  

mainloop()