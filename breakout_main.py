import turtle
import random

# Tela
screen = turtle.Screen()
screen.title("Breakout")
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


# Blocos, matriz 8x10 (temporario)
xcor = -270
ycor = 50
colors = ["yellow", "green", "orange", "red"]
for i in range(8):  # linhas
    x = colors[int(i/2)]  # a cada duas linhas ele muda de cor
    for i in range(10):  # colunas
        blocks(x, xcor, ycor)
        xcor += 60
    ycor += 15
    xcor = -270

# Heads-up display (pontuacao)
huds = turtle.Turtle()
huds.speed(0)
huds.shape("square")
huds.color("white")
huds.penup()
huds.hideturtle()
huds.goto(-200, 250)
huds.write("0000", align="center", font=("Press Start 2P",32,"normal") )

# Heads-up display (vidas)
hudl1 = turtle.Turtle()
hudl1.speed(0)
hudl1.shape("square")
hudl1.color("white")
hudl1.penup()
hudl1.hideturtle()
hudl1.goto(200, 250)
hudl1.write(" x 3", align="center", font=("Press Start 2P",24,"normal") )
hudl2 = turtle.Turtle()
hudl2.speed(0)
hudl2.shape("circle")
hudl2.color("white")
hudl2.penup()
hudl2.goto(160, 270)

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
