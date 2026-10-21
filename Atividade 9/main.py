import turtle
from random import randint


def randomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))

# espiral revursiva

def recursiveSpiral(t, size, angle):
  if size < 5:
    return
  t.fd(size)
  t.lt(angle)
  recursiveSpiral(t, size - 3, angle)


# triangulos recursivos

def drawTriangle(t, size):
  for i in range(3):
    t.fd(size)
    t.lt(120)


def triangleFractal(t, size, minSize):
  if size < minSize:
    return

  t.pencolor(randomColor())
  drawTriangle(t, size)

  for i in range(3):
    t.fd(size)
    triangleFractal(t, size / 2, minSize)
    t.lt(120)


# floco de neve de Koch

def kochFractal(t, size, nivel, angle=60):
  # Quando chega no nivel 0, desenha uma linha e termina a recursao
  if nivel == 0:
    t.fd(size)
    return

  # Cada nova linha tem 1/3 do tamanho da linha anterior
  newSize = size / 3

  # Primeiro segmento
  kochFractal(t, newSize, nivel - 1, angle)

  # Gira para a esquerda para subir
  t.lt(angle)

  # Segundo segmento
  kochFractal(t, newSize, nivel - 1, angle)

  # Gira para a direita para descer
  t.rt(angle * 2)

  # Terceiro segmento
  kochFractal(t, newSize, nivel - 1, angle)

  # Volta para a direcao inicial
  t.lt(angle)

  # Quarto segmento
  kochFractal(t, newSize, nivel - 1, angle)


# Funcao que junta 3 fractais de Koch para formar o floco de neve
def drawKochSnowflake(t, size, nivel, angle=60):

  # Repete 3 vezes porque o floco tem a forma inicial de um triangulo
  for i in range(3):

    # Escolhe uma cor aleatoria para cada lado
    t.pencolor(randomColor())

    # Desenha um lado do floco
    kochFractal(t, size, nivel, angle)

    # Gira 120 graus para desenhar o proximo lado
    t.rt(120)


t = turtle.Turtle()
turtle.colormode(255)

t.speed(0)
t.pu()


## Desenhando a espiral recursiva
t.goto(0, -150)
t.pd()
recursiveSpiral(t, 150, 30)


## Desenhando os triangulos
#t.goto(-200, -150)
#t.pd()
#triangleFractal(t, 300, 20)


## Desenhando o floco de neve de Koch
#t.goto(-250, 150)
#t.pd()
#drawKochSnowflake(t, 500, 4)


turtle.done()