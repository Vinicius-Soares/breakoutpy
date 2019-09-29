import turtle


# colisão bola/raquete
def collide_paddle(paddle, ball):
    px, py = paddle.xcor(), paddle.ycor()
    bx, by = ball.xcor(), ball.ycor()

    if (bx + 10 >= px - 50 and bx - 10 <= px + 50 and by - 10 <= py + 10 and by + 10 >= py - 10):
        ball.dy *= -1
        if abs(bx - px) < 10:
            ball.dx = 0
        elif abs(bx - px) < 20:
            if bx > px:
                ball.dx = 2
            else:
                ball.dx = -2
        elif abs(bx - px) < 30:
            if bx > px:
                ball.dx = 1.5
            else:
                ball.dx = -1.5
        elif abs(bx - px) < 40:
            if bx > px:
                ball.dx = 1
            else:
                ball.dx = -1
        else:
            if bx > px:
                ball.dx = 0.5
            else:
                ball.dx = -0.5


def reset_ball(ball):
    ball.goto(0, -249)


# colisão bola/parede
def collide_walls(ball):
    bx, by = ball.xcor(), ball.ycor()
    if by + 10 >= 249 or by - 10 <= -349:
        ball.dy *= -1
    elif bx + 10 >= 295 or bx - 10 <= -296:
        ball.dx *= -1
