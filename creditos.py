import turtle


def credits_play():
    # Interface
    screen = turtle.Screen()
    screen.title("BREAKOUT")
    screen.bgcolor("black")
    screen.setup(600, 1200)
    screen.tracer(0)

    credits = turtle.Turtle("square")
    credits.speed(0)
    credits.color("white")
    credits.penup()
    credits.hideturtle()
    credits.goto(0, 180)
    credits.write("CRÉDITOS", align="center",
                  font=("Press Start 2P", 16, "bold"))

    credits = turtle.Turtle("square")
    credits.speed(0)
    credits.color("white")
    credits.penup()
    credits.hideturtle()
    credits.goto(0, -10)
    credits.write("""    - Vinicius Soares da Costa;
    - Natanael da Mota Figueira;
    - Lucas Mendes Sonoda;
    - Caio Andrade Mota;
    - Helder Melik Schramm;""", align="center",
                  font=("Press Start 2P", 16, "bold"))
