import turtle
import sys
import os
import simpleaudio as sa
from breakout_main import game_play
from random import choice


def selection_sound():
    filename = 'selection.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()


# Interface
screen = turtle.Screen()
screen.title("BREAKOUT")
screen.bgcolor("#29207a")
screen.setup(600, 1200)
screen.tracer(0)

# Título do jogo
game_title = turtle.Turtle("square")
game_title.speed(0)
game_title.color("#ccac00")
game_title.penup()
game_title.hideturtle()
game_title.goto(0, 180)
game_title.dx = 15
game_title.dy = 15
game_title.write("BREAKOUT", align="center",
                 font=("Press Start 2P", 24, "bold"))


# Tela de seleção
mode = turtle.Turtle("square")
mode.speed(0)
mode.color("white")
mode.penup()
mode.hideturtle()
mode.goto(0, 50)
mode.write("JOGO", align="center",
           font=("Press Start 2P", 16, "bold"))

mode = turtle.Turtle("square")
mode.speed(0)
mode.color("white")
mode.penup()
mode.hideturtle()
mode.goto(0, 10)
mode.write("OPÇÕES", align="center",
           font=("Press Start 2P", 16, "bold"))

mode = turtle.Turtle("square")
mode.speed(0)
mode.color("white")
mode.penup()
mode.hideturtle()
mode.goto(0, -30)
mode.write("PLACAR", align="center",
           font=("Press Start 2P", 16, "bold"))

# Parâmetros da seleção
selection = turtle.Turtle("square")
selection.speed(0)
selection.turtlesize(1.5, 6)
selection.color('blue')
selection.fillcolor('')
selection.penup()
selection.sety(65)


def selection_up():
    if (selection. ycor() == -15):
        selection.sety(25)
    elif (selection.ycor() == 25):
        selection.sety(65)
    elif (selection.ycor() == 65):
        selection.sety(-15)
    selection_sound()


def selection_down():
    if (selection.ycor() == 65):
        selection.sety(25)
    elif (selection. ycor() == 25):
        selection.sety(-15)
    elif (selection.ycor() == -15):
        selection.sety(65)
    selection_sound()


def selection_mode():
    if (selection.ycor() == 65):
        screen.clear()
        game_play()

    if (selection.ycor() == -15):
        screen.clear()
        pong_2players()


screen.onkeypress(selection_mode, 'Return')
screen.onkeypress(selection_up, 'Up')
screen.onkeypress(selection_down, 'Down')
screen.listen()

while(True):
    screen.update()
