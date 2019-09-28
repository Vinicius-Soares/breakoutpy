import turtle

# colisão bola/raquete
def collide_paddle(paddle, ball):
    px, py = paddle.xcor(), paddle.ycor()
    bx, by = ball.xcor(), ball.ycor()

    if bx + 10 >= px - 50 and bx - 10 <= px + 50 and by - 10 <= py + 10 and by + 10 >= py - 10:
        ball.dy *= -1
        if (bx - px) < 10:
            ball.dx = 0
        elif (bx - px) < 20:
            if (bx > px):
                ball.dx = 1
            else:
                ball.dx = -1
        elif (bx - px) < 30:
            if (bx > px):
                ball.dx = 0.8
            else:
                ball.dx = -0.8
        elif (bx - px) < 40:
            if (bx > px):
                ball.dx = 0.4
            else:
                ball.dx = -0.4
        else:
            if (bx > px):
                ball.dx = 0.2
            else:
                ball.dx = -0.2



# colisão bola/parede
def collide_walls(ball):
    bx, by = ball.xcor(), ball.ycor()

    if by + 10 >= 250 or by - 10 <= -350:
        ball.dy *= -1
    elif bx + 10 >= 300 or bx - 10 <= -300:
        ball.dx *= -1