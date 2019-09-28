import turtle
from generate_blocks import generate_blocks
from blocks import generate_blocks1 

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
paddle.goto(0, -450)

# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -428)

# Chamando função que gera blocos
generate_blocks(8, 6)
# generate_blocks1(1, 1)

# Heads-up display (pontuacao)
score = 0
huds = turtle.Turtle()
huds.speed(0)
huds.shape("square")
huds.color("white")
huds.penup()
huds.hideturtle()
huds.goto(-200, 440)
huds.write("{:04d}".format(score), align="center", font=("Press Start 2P", 32, "normal"))

# Heads-up display (vidas)
hudl1 = turtle.Turtle()
hudl1.speed(0)
hudl1.shape("square")
hudl1.color("white")
hudl1.penup()
hudl1.hideturtle()
hudl1.goto(200, 450)
hudl1.write(" x 3", align="center", font=("Press Start 2P", 24, "normal"))
hudl2 = turtle.Turtle()
hudl2.speed(0)
hudl2.shape("circle")
hudl2.color("white")
hudl2.penup()
hudl2.goto(145, 464)

# Linha superior
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=0.25, stretch_len=30)
line.penup()
line.goto(0, 420)
while True:
    screen.update()
