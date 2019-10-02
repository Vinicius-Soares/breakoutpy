from collision import collide_paddle, reset_ball, collide_walls
import turtle
from generate_blocks import (generate_blocks, block_list,
                             block_posxy, block_colors)
import sounds
import variables
from movimentation import paddle_left, paddle_right
import os
import time
from placar import read_highscore, new_highscore
import simpleaudio


def game_play():

    # Tela
    screen = turtle.Screen()
    screen.title("Breakout")
    screen.bgpic("48076.gif")
    screen.setup(width=600, height=1200)
    screen.tracer(0)

    # raquete
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("Steel Blue")
    paddle.fillcolor("blue")
    paddle.shapesize(stretch_wid=1, stretch_len=5)
    paddle.penup()
    paddle.goto(0, -270)

    collide_walls
    # movimentação da raquete

    def paddle_right():
        x = paddle.xcor()
        if x < 250:
            x += 20
        else:
            x = 250
        paddle.setx(x)

    def paddle_left():
        x = paddle.xcor()
        if x > -250:
            x -= 20
        else:
            x = -250
        paddle.setx(x)

    # mapeamento das teclas
    screen.listen()
    screen.onkeypress(paddle_right, "d")
    screen.onkeypress(paddle_left, "a")

    # Bola
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("#f5272a")
    ball.fillcolor("#c90003")
    ball.penup()
    ball.goto(0, -250)
    ball.dx = 2
    ball.dy = 2

    # Chamando função que gera blocos
    generate_blocks(8, 6)
    block_delxy = []
    block_collide = [0]*len(block_posxy)

    # Heads-up display (pontuacao)
    score = 0
    huds = turtle.Turtle()
    huds.speed(0)
    huds.shape("square")
    huds.color("white")
    huds.penup()
    huds.hideturtle()
    huds.goto(-200, 270)
    huds.write("{:04d}".format(score), align="center",
               font=("Press Start 2P", 32, "bold"))

    # Heads-up display (vidas)
    lives = 3
    hudl1 = turtle.Turtle()
    hudl1.speed(0)
    hudl1.shape("square")
    hudl1.color("white")
    hudl1.penup()
    hudl1.hideturtle()
    hudl1.goto(200, 270)
    hudl1.write(" x{}".format(lives), align="center",
                font=("Press Start 2P", 24, "bold"))
    hudl2 = turtle.Turtle()
    hudl2.speed(0)
    hudl2.shape("circle")
    hudl2.color("white")
    hudl2.penup()
    hudl2.goto(145, 284)

    # High Score
    actual_highscore = read_highscore()

    hudl3 = turtle.Turtle()
    hudl3.speed(0)
    hudl3.shape("square")
    hudl3.color("yellow")
    hudl3.penup()
    hudl3.hideturtle()
    hudl3.goto(0, 300)
    hudl3.write("HIGH SCORE", align="center",
                font=("Press Start 2P", 24, "bold"))

    hudl4 = turtle.Turtle()
    hudl4.speed(0)
    hudl4.shape("square")
    hudl4.color("yellow")
    hudl4.penup()
    hudl4.hideturtle()
    hudl4.goto(0, 260)
    hudl4.write("{}".format(actual_highscore), align="center",
                font=("Press Start 2P", 24, "bold"))

    # Linha superior
    line = turtle.Turtle()
    line.speed(0)
    line.shape("square")
    line.color("white")
    line.shapesize(stretch_wid=0.25, stretch_len=30)
    line.penup()
    line.goto(0, 250)

    while (lives > 0):
        screen.update()

        # movimentação da bola
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # colisão bola/parede
        collide_walls(ball)

        # colisão bola/raquete
        collide_paddle(paddle, ball)

        # condição da perda de vida
        if ball.ycor() < -340:
            lives -= 1
            reset_ball(ball)
            hudl1.clear()
            hudl1.write(" x{}".format(lives), align="center",
                        font=("Press Start 2P", 24, "bold"))
            os.system("aplay sounds/failure.wav&")

        # finalização de jogo
        if lives == 0:

            # condição de novo recorde
            if (new_highscore(score)):
                background = "victory1.gif"
                message = "NEW HIGHSCORE"
                color1 = "yellow"
                color2 = "blue"
            else:
                background = "gameover.gif"
                message = "GAME OVER"
                color1 = "red"
                color2 = "white"

            screen.clear()
            screen = turtle.Screen()
            screen.title("Breakout")
            screen.bgpic(background)
            screen.setup(width=600, height=1200)
            screen.tracer(0)

            defeat = turtle.Turtle()
            defeat.speed(0)
            defeat.shape("square")
            defeat.color(color1)
            defeat.penup()
            defeat.hideturtle()
            defeat.goto(0, 100)
            defeat.write(message, align="center",
                         font=("Press Start 2P", 32, "bold"))

            defeat = turtle.Turtle()
            defeat.speed(0)
            defeat.shape("square")
            defeat.color(color2)
            defeat.penup()
            defeat.hideturtle()
            defeat.goto(0, 0)
            defeat.write("SCORE", align="center",
                         font=("Press Start 2P", 32, "bold"))

            defeat = turtle.Turtle()
            defeat.speed(0)
            defeat.shape("square")
            defeat.color(color2)
            defeat.penup()
            defeat.hideturtle()
            defeat.goto(0, -50)
            defeat.write("{}".format(score), align="center",
                         font=("Press Start 2P", 32, "bold"))

            os.system("aplay sounds/you_died.wav&")
            time.sleep(5)
            screen.clear()

            return("sair")

        # condição destruição blocos
        bx, by = ball.xcor(), ball.ycor()
        for posxy in block_posxy:
            if (posxy in block_delxy):
                block_posxy.remove(posxy)

                # Condição de nova fase
                if (len(block_posxy) == 0):
                    block_list.clear()
                    block_posxy.clear()
                    block_colors.clear()
                    block_collide.clear()
                    time.sleep(5)
                    generate_blocks(8, 6)
                    block_collide = [0]*len(block_posxy)
                    block_delxy.clear()
                    ball.goto(0, -250)
                    ball.dx = 2
                    ball.dy = 2

        for block in block_list:
            if (block.pos() in block_delxy):
                block.reset()

        for pos in range(len(block_posxy)):
            if (bx >= block_posxy[pos][0]-50 and
                bx <= block_posxy[pos][0]+50 and
                    by >= block_posxy[pos][1]-20 and
                    by <= block_posxy[pos][1]+20):
                ball.dy *= -1
                if (ball.dx > 0 and ball.dx < 0):
                    ball.dx *= -1

                # dificuldade dos blocos

                # bloco laranja
                if (block_colors[pos] == "Deep Sky Blue"):

                    # velocidade
                    if (ball.dx > 0):
                        ball.dx += 0.01
                    elif (ball.dx < 0):
                        ball.dx -= 0.01
                    if (ball.dy > 0):
                        ball.dy += 0.01
                    elif (ball.dy < 0):
                        ball.dy -= 0.01
                    block_delxy.append(
                        (block_posxy[pos][0], block_posxy[pos][1]))

                    # pontos
                    score += 100
                    os.system("aplay sounds/hit.wav&")

                # bloco esmeralda
                elif (block_colors[pos] == "#048f40"):

                    # velocidade
                    if (ball.dx > 0):
                        ball.dx += 0.02
                    elif (ball.dx < 0):
                        ball.dx -= 0.02
                    if (ball.dy > 0):
                        ball.dy += 0.02
                    elif (ball.dy < 0):
                        ball.dy -= 0.02

                    # pontos
                    if (block_collide[pos] == 1):
                        block_delxy.append(
                            (block_posxy[pos][0], block_posxy[pos][1]))
                        score += 200
                        os.system("aplay sounds/hit.wav&")
                    else:
                        block_collide[pos] += 1
                        os.system("aplay sounds/hit.wav&")

                # bloco gold
                elif (block_colors[pos] == "#ccac00"):

                    # velocidade
                    if (ball.dx > 0):
                        ball.dx += 0.03
                    elif (ball.dx < 0):
                        ball.dx -= 0.03
                    if (ball.dy > 0):
                        ball.dy += 0.03
                    elif (ball.dy < 0):
                        ball.dy -= 0.03

                    # pontos
                    if (block_collide[pos] == 2):
                        block_delxy.append(
                            (block_posxy[pos][0], block_posxy[pos][1]))
                        score += 300
                        os.system("aplay sounds/hit.wav&")
                    else:
                        block_collide[pos] += 1
                        os.system("aplay sounds/hit.wav&")

                # bloco azul escuro
                elif (block_colors[pos] == "#29207a"):

                    # velocidade
                    if (ball.dx > 0):
                        ball.dx += 0.04
                    elif (ball.dx < 0):
                        ball.dx -= 0.04
                    if (ball.dy > 0):
                        ball.dy += 0.04
                    elif (ball.dy < 0):
                        ball.dy -= 0.04

                    # pontos
                    if (block_collide[pos] == 3):
                        block_delxy.append(
                            (block_posxy[pos][0], block_posxy[pos][1]))
                        score += 400
                        os.system("aplay sounds/hit.wav&")
                    else:
                        block_collide[pos] += 1
                        os.system("aplay sounds/hit.wav&")

                # bloco cinza
                elif (block_colors[pos] == "gray"):

                    # velocidade
                    if (ball.dx > 0):
                        ball.dx += 0.05
                    elif (ball.dx < 0):
                        ball.dx -= 0.05
                    if (ball.dy > 0):
                        ball.dy += 0.05
                    elif (ball.dy < 0):
                        ball.dy -= 0.05

                    # pontos
                    if (block_collide[pos] == 4):
                        block_delxy.append(
                            (block_posxy[pos][0], block_posxy[pos][1]))
                        score += 500
                        os.system("aplay sounds/beat_impact.wav&")
                    else:
                        block_collide[pos] += 1
                        os.system("aplay sounds/beat_impact.wav&")

                # atualização pontos
                huds.clear()
                huds.write("{:04d}".format(score), align="center",
                           font=("Press Start 2P", 32, "bold"))
