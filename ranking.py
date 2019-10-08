import turtle


def ranking_generate(score):
    screen = turtle.Screen()
    name = screen.textinput("Nome", "NOME DO JOGADOR:")
    file = open('ranking.txt', 'r')
    ranking = file.readlines()
    ranking.append("{} {}\n".format(name, score))
    ranking.reverse()
    file = open('ranking.txt', 'w')
    file.writelines(ranking)
    file.close()


def ranking_play():
    # Interface
    screen = turtle.Screen()
    screen.title("BREAKOUT")
    screen.bgpic("48076.gif")
    screen.setup(600, 1200)
    screen.tracer(0)

    ranking = turtle.Turtle("square")
    ranking.speed(0)
    ranking.color("yellow")
    ranking.penup()
    ranking.hideturtle()
    ranking.goto(0, 180)
    ranking.write("HIGH SCORES", align="center",
                  font=("Press Start 2P", 30, "bold"))

    file = open('ranking.txt', 'r')
    ranking_text = file.readlines()
    posx_name = -220
    posx_score = 220
    posy = 100
    rank = 1
    for line in range(len(ranking_text)):
        ranking_line = ranking_text[line].strip().split(" ")

        ranking = turtle.Turtle("square")
        ranking.speed(0)
        ranking.color("white")
        ranking.penup()
        ranking.hideturtle()
        ranking.goto(posx_name, posy)
        ranking.write("{}. {}".format(rank, str(ranking_line[0])),
                      align="left", font=("Press Start 2P", 16, "bold"))

        ranking = turtle.Turtle("square")
        ranking.speed(0)
        ranking.color("white")
        ranking.penup()
        ranking.hideturtle()
        ranking.goto(posx_score, posy)
        ranking.write(str(ranking_line[-1]), align="right",
                      font=("Press Start 2P", 16, "bold"))
        posy -= 30
        rank += 1
