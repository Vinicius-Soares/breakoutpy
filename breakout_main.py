import turtle

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
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0,-300)

# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,-280)

# Funcao para fazer os blocos (temporario)
def blocks(col, xdir, ydir):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(col)
    paddle.shapesize(stretch_wid=0.5, stretch_len=2.5)
    paddle.penup()
    paddle.goto(xdir,ydir)

# Blocos, matriz 8x10 (temporario) 
xcor = -270
ycor = 100
colors = ["yellow","green","orange","red"]
for i in range(8): # linhas
    x = colors[int(i/2)] # a cada duas linhas ele muda de cor
    for i in range(10): # colunas
        blocks(x,xcor,ycor)
        xcor += 60
    ycor += 15
    xcor = -270

while True:
    screen.update()