import turtle

# Skapa spelplanen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Poäng
score_a = 0
score_b = 0

# Paddel A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddel B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Boll
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Poängtext
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Spelare A: 0  Spelare B: 0", align="center", font=("Courier", 24, "normal"))

# Tangentstatus
keys = {
    "w": False,
    "s": False,
    "Up": False,
    "Down": False,
}

# Funktioner för tangentstatus
def key_press(key):
    keys[key] = True

def key_release(key):
    keys[key] = False

# Funktioner för rörelse
def move_paddles():
    if keys["w"] and paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor() + 0.5)
    if keys["s"] and paddle_a.ycor() > -240:
        paddle_a.sety(paddle_a.ycor() - 0.5)
    if keys["Up"] and paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor() + 0.5)
    if keys["Down"] and paddle_b.ycor() > -240:
        paddle_b.sety(paddle_b.ycor() - 0.5)

# Tangentbindningar
wn.listen()
wn.onkeypress(lambda: key_press("w"), "w")
wn.onkeypress(lambda: key_press("s"), "s")
wn.onkeypress(lambda: key_press("Up"), "Up")
wn.onkeypress(lambda: key_press("Down"), "Down")
wn.onkeyrelease(lambda: key_release("w"), "w")
wn.onkeyrelease(lambda: key_release("s"), "s")
wn.onkeyrelease(lambda: key_release("Up"), "Up")
wn.onkeyrelease(lambda: key_release("Down"), "Down")

# Spelloopen
while True:
    wn.update()
    
    # Flytta paddlar
    move_paddles()

    # Flytta bollen
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Kolla väggkollisioner
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Spelare A: {score_a}  Spelare B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Spelare A: {score_a}  Spelare B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Kolla kollision med paddel A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Kolla kollision med paddel B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
