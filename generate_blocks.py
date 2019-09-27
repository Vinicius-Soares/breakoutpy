import turtle
import random

# Gerador de blocos


def generate_blocks(x, y):
    colors = ["#FF6103", "#00C957", "#458B00", "yellow", "gray"]
    posy_block = 220
    for lines in range(x):
        posx_block = -255
        color_block = random.choice(colors)
        for columns in range(y):
            block = turtle.Turtle("square")
            block.speed(0)
            block.color("black")
            block.fillcolor(color_block)
            block.shapesize(1, 4)
            block.penup()
            block.goto(posx_block, posy_block)
            posx_block += 100
        posy_block -= 35
