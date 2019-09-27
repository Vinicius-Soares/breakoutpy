import turtle
import random

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

# Blocos
color_block = ["white", "blue", "green", "yellow"]
posy_block = 260
for lines in range(10):
    posx_block = -270
    for columns in range(16):
        block = turtle.Turtle("square")
        block.speed(0)
        block.color(random.choice(color_block))
        block.shapesize(1, 1)
        block.penup()
        block.goto(posx_block, posy_block)
        posx_block += 35
    posy_block -= 35

# Funcao para fazer os blocos (temporario)
def blocks(col, xdir, ydir):
    block = turtle.Turtle()
    block.speed(0)
    block.shape("square")
    block.color(col)
    block.shapesize(stretch_wid=0.5, stretch_len=2.5)
    block.penup()
    block.goto(xdir,ydir)

# Blocos, matriz 8x10 (temporario) 
xcor = -270
ycor = 50
colors = ["yellow","green","orange","red"]
for i in range(8): # linhas
    x = colors[int(i/2)] # a cada duas linhas ele muda de cor
    for i in range(10): # colunas
        blocks(x,xcor,ycor)
        xcor += 60
    ycor += 15
    xcor = -270

# Linha superior
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=0.25, stretch_len=30)
line.penup()
line.goto(0,250)
while True:
    screen.update()
