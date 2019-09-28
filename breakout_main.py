import turtle
from generate_blocks import generate_blocks
from blocks import block_line1

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
paddle.goto(0, -250)


# movimentação da raquete
def paddle_right():
    x = paddle.xcor()
    if x < 300:
        x += 20
    else:
        x = 300
    paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    if x > -300:
        x -= 20
    else:
        x = -300
    paddle.setx(x)

# mapeamento das teclas
screen.listen()
screen.onkeypress(paddle_right, "d")
screen.onkeypress(paddle_left, "a")

# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -230)

# Chamando função que gera blocos
generate_blocks(8, 6)
# block_line1(1, 1)

# Heads-up display (pontuacao)
score = 0
huds = turtle.Turtle()
huds.speed(0)
huds.shape("square")
huds.color("white")
huds.penup()
huds.hideturtle()
huds.goto(-200, 270)
huds.write("{:04d}".format(score), align="center", font=("Press Start 2P", 32, "normal"))

# Heads-up display (vidas)
hudl1 = turtle.Turtle()
hudl1.speed(0)
hudl1.shape("square")
hudl1.color("white")
hudl1.penup()
hudl1.hideturtle()
hudl1.goto(200, 270)
hudl1.write(" x 3", align="center", font=("Press Start 2P", 24, "normal"))
hudl2 = turtle.Turtle()
hudl2.speed(0)
hudl2.shape("circle")
hudl2.color("white")
hudl2.penup()
hudl2.goto(145, 284)

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
