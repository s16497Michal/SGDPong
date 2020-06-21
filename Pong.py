import turtle

window = turtle.Screen()
window.title("Pong by Michał Kosinski - 16497")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

#implementacja lewego gracza
left_player = turtle.Turtle()
left_player.speed(0)
left_player.shape("square")
left_player.color("red")
left_player.shapesize(stretch_wid=5, stretch_len=1)
left_player.penup()
left_player.goto(-350, 0)

#implementacja prawego gracza
right_player = turtle.Turtle()
right_player.speed(0)
right_player.shape("square")
right_player.color("red")
right_player.shapesize(stretch_wid=5, stretch_len=1)
right_player.penup()
right_player.goto(350, 0)

#wynik
score_left = 0
score_right = 0

#implementacja pilki
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

#komponent zliczający punkty
score = turtle.Turtle()
score.speed(0)
score.color("red")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Left player: 0 Right player: 0", align="center", font=("Courier", 24, "normal"))

#poruszanie lewego gracza

def left_player_up():
    y = left_player.ycor()
    y += 20
    left_player.sety(y)

def left_player_down():
    y = left_player.ycor()
    y -= 20
    left_player.sety(y)

def right_player_up():
    y = right_player.ycor()
    y += 20
    right_player.sety(y)

def right_player_down():
    y = right_player.ycor()
    y -= 20
    right_player.sety(y)

#obsluga klawiszy
window.listen()
window.onkeypress(left_player_up, "w")
window.onkeypress(left_player_down, "s")
window.onkeypress(right_player_up, "Up")
window.onkeypress(right_player_down, "Down")

while True:
    window.update()

    #kontrola ruchu piłki
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #ustawienia ramek
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        score.clear()
        score.write("Left player: {} Right player: {}".format(score_right, score_left), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        score.clear()
        score.write("Left player: {} Right player: {}".format(score_right, score_left), align="center", font=("Courier", 24, "normal"))

    #kontrola poprawnego zachowania - prawy gracz
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_player.ycor() + 50 and ball.ycor() > right_player.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_player.ycor() + 50 and ball.ycor() > left_player.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1