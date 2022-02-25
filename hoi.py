import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("pink")
wn.setup(width=800, height=600)
wn.tracer(0)


# score 
score_a = 0
score_b = 0

# paddle A
paddle_a=turtle.Turtle()
paddle_a.shape("square")
paddle_a.speed(0)
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B 
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx = 1.8
Ball.dy = -1.8


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("0-0" , align="center", font=("Courier", 24,"normal"))


# Function 
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)\

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)\

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 
    paddle_b.sety(y)

# Keyboard binding 
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()
    
    # Move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)


    # Border checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        os.system("afplay bounce.wav&")

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
        os.system("afplay bounce.wav&")

    if Ball.xcor() > 390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("{}-{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if Ball.xcor() < -390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("{}-{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < paddle_b.ycor() + 50 and Ball.ycor() > paddle_b.ycor() - 50):
        Ball.setx(340)
        Ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < paddle_a.ycor() + 50 and Ball.ycor() > paddle_a.ycor() - 50):
        Ball.setx(-340)
        Ball.dx *= -1
        os.system("afplay bounce.wav")
