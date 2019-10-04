import turtle


def read_highscore():

    file = open("highscore.txt", "r")
    highscore = int(file.readlines()[0].strip())
    file.close()
    return(highscore)


def new_highscore(score):

    if (score > read_highscore()):
        file = open("highscore.txt", "w")
        file.write(str(score))
        file.close()
        return(True)
