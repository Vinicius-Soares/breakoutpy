import turtle
import os


# colisão bola/raquete
def collide_paddle(paddle, ball):
    px, py = paddle.xcor(), paddle.ycor()
    bx, by = ball.xcor(), ball.ycor()

    if (bx + 10 >= px - 50 and bx - 10 <= px + 50 and
            by - 10 <= py + 10 and by + 10 >= py - 10):
        ball.dy *= -1
        if abs(bx - px) < 10:
            ball.dx = 0
            os.system("aplay sounds/bounce.wav&")
        elif abs(bx - px) < 20:
            if bx > px:
                ball.dx = 2
                os.system("aplay sounds/bounce.wav&")
            else:
                ball.dx = -2
                os.system("aplay sounds/bounce.wav&")
        elif abs(bx - px) < 30:
            if bx > px:
                ball.dx = 1.5
                os.system("aplay sounds/bounce.wav&")
            else:
                ball.dx = -1.5
                os.system("aplay sounds/bounce.wav&")
        elif abs(bx - px) < 40:
            if bx > px:
                ball.dx = 1
                os.system("aplay sounds/bounce.wav&")
            else:
                ball.dx = -1
                os.system("aplay sounds/bounce.wav&")
        else:
            if bx > px:
                ball.dx = 0.5
                os.system("aplay sounds/bounce.wav&")
            else:
                ball.dx = -0.5
                os.system("aplay sounds/bounce.wav&")


def reset_ball(ball, paddle):
    paddle.goto(0, -270)
    ball.goto(0, -249)
    ball.dx = 1
    ball.dy = 1


# colisão bola/parede
def collide_walls(ball):
    bx, by = ball.xcor(), ball.ycor()
    if by + 10 >= 249 or by - 10 <= -360:
        ball.dy *= -1
    elif bx + 10 >= 295 or bx - 10 <= -296:
        ball.dx *= -1
