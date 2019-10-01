# movimentação da raquete


def paddle_right():
    x = paddle.xcor()
    if x < 250:
        x += 20
    else:
        x = 250
    paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    if x > -250:
        x -= 20
    else:
        x = -250
    paddle.setx(x)
