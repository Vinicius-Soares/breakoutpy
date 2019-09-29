import turtle
import random


# Gerador de blocos
block_posx = []
block_posy = []


def generate_blocks(x, y):
    colors = ["#FF6103", "#00C957", "#458B00", "yellow", "gray"]
    posy_block = 220
    count = 0
    for lines in range(x):
        posx_block = -255
        if (lines % 2 == 0):
            count += 1
        color_block = colors[count]
        for columns in range(y):
            block = turtle.Turtle("square")
            block.speed(0)
            block.color(color_block)
            block.shapesize(1, 4)
            block.penup()
            block.goto(posx_block, posy_block)
            posx_block += 100
            block_posx.append(block.xcor())
            block_posy.append(block.ycor())
        posy_block -= 35
