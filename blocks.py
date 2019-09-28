import turtle

# gera primeira linha de bolocos
def generate_blocks1(position, exist): # posição do bloco na linha e se existe ou não, podem ser guardados em uma lista no main separados por linha
    block = turtle.Turtle("square")
    block.speed(0)
    block.color("yellow")
    block.shapesize(1, 4)
    block.penup()
    posx = -355 + 100 * position
    posy = 115
    block.goto(posx, posy)
    # repete a função ao ser tocada pela bola, como o bloco existe ele desaparece e retorna um valor de pontuação e a variavel de existencia é alterada no main
    if exist:
        block.clear()
        return 10
