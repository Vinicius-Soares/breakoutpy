import turtle
from generate_blocks import generate_blocks

# Tela
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=600, height=1200)
screen.tracer(0)

# raquete
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -300)

# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -278)


# Funcao para fazer os blocos (temporario)


def blocks(col, xdir, ydir):
    block = turtle.Turtle()
    block.speed(0)
    block.shape("square")
    block.color(col)
    block.shapesize(stretch_wid=0.5, stretch_len=2.5)
    block.penup()
    block.goto(xdir, ydir)


# Chamando função que gera blocos
generate_blocks(8, 6)

# Linha superior
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=0.25, stretch_len=30)
line.penup()
line.goto(0, 250)
while True:
    screen.update()
