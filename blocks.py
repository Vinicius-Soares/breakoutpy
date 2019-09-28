import turtle

# gera primeira linha de blocos
def block_line1(position, exist): # posição do bloco na linha e se existe ou não, podem ser guardados em uma lista no main separados por linha
    block = turtle.Turtle("square")
    block.speed(0)
    block.color("yellow")
    block.shapesize(1, 4)
    block.penup()
    posx = -355 + 100 * position
    posy = -25
    if exist:
        block.goto(posx, posy)
    # altera a variavel que representa a existecia no main ao ser tocado e então roda a funçã para eliminar o bloco
    else:
        block.clear()
        return 50
