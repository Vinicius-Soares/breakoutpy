import turtle


def boardscore_generate(score):
    screen = turtle.Screen()
    name = screen.textinput("Nome", "NOME DO JOGADOR:")
    file = open('boardscore.txt', 'r')
    boardscore = file.readlines()
    boardscore.append("{} {}\n".format(name, score))
    boardscore.reverse()
    file = open('boardscore.txt', 'w')
    file.writelines(boardscore)
    file.close()
