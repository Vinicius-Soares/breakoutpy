import turtle
import random


# Alguns parametros do gerador de blocos
block_posxy = []
block_list = []
block_colors = []


# Funçao que gera os blocos
def generate_blocks(x, y):
    colors = ["Deep Sky Blue", "#048f40", "#ccac00", "#29207a", "gray"]
    colors_edge = ["Sky Blue", "#00C957", "#ffdf33", "#3225c2", "Gainsboro"]
    posy_block = 220
    for lines in range(x):
        posx_block = -255
        color_block = random.choice(colors)
        for pos in range(len(colors)):
            if (colors[pos] == color_block):
                edge_block = colors_edge[pos]
        for columns in range(y):
            block = turtle.Turtle("square")
            block.speed(0)
            block.color(edge_block)
            block.fillcolor(color_block)
            block.shapesize(1, 4)
            block.penup()
            block.goto(posx_block, posy_block)
            posx_block += 100
            block_list.append(block)
            block_colors.append(color_block)
            block_posxy.append((block.xcor(), block.ycor()))
        posy_block -= 35
