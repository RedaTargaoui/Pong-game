# Descriptipn : Pong Game
# Author : Reda Targaoui
# Date : 30/05/2022

import turtle

# score :
score1 = 0
score2 = 0

# creating window :
window = turtle.Screen()
window.title('Pong by Reda Targaoui')
window.bgcolor('red')
window.setup(width = 800, height = 600)
window.tracer(0)

# creating padddles :
leftPaddle = turtle.Turtle()
leftPaddle.speed(0)
leftPaddle.shape('square')
leftPaddle.color('black')
leftPaddle.shapesize(stretch_wid = 6, stretch_len = 1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

rightPaddle = turtle.Turtle()
rightPaddle.speed(0)
rightPaddle.shape('square')
rightPaddle.color('black')
rightPaddle.shapesize(stretch_wid = 6, stretch_len = 1)
rightPaddle.penup()
rightPaddle.goto(350, 0)

# create the ball :
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('black')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# add scroe text : 
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# To move the left paddle up :
def leftPaddle_up() : 
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)

# To move th e left paddle down :
def leftPaddle_down() :
    y = leftPaddle.ycor()
    y -= 20
    leftPaddle.sety(y)

# To move the right paddle up :
def rightPaddle_up() : 
    y = rightPaddle.ycor()
    y += 20
    rightPaddle.sety(y)

# To move th e right paddle down :
def rightPaddle_down() :
    y = rightPaddle.ycor()
    y -= 20
    rightPaddle.sety(y)

# To move on with keyboard buttons :
window.listen()
window.onkeypress(leftPaddle_up, 'q')
window.onkeypress(leftPaddle_down, 'w')
window.onkeypress(rightPaddle_up, 'Up')
window.onkeypress(rightPaddle_down, 'Down')


# game loop :
while True :
    window.update()

    # To move tha ball :
    ball.setx(ball.xcor() + (ball.dx / 18))
    ball.sety(ball.ycor() + (ball.dy / 18))

    # So the ball can't go through the frames :
    # Top and Bottom :
    if ( ball.ycor() > 290 ) :
        ball.sety(290)
        ball.dy *= -1
    
    elif ( ball.ycor() < -290 ) :
        ball.sety(-290)
        ball.dy *= -1

    # Left and right :
    if ( ball.xcor() > 350 ) :
        score1 += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ( ball.xcor() < -350 ) :
        score2 += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ( ball.xcor() < -340 and ball.ycor() < leftPaddle.ycor() + 50 and ball.ycor() > leftPaddle.ycor() - 50 ) :
        ball.dx *= -1 
    
    elif ( ball.xcor() > 340 and ball.ycor() < rightPaddle.ycor() + 50 and ball.ycor() > rightPaddle.ycor() - 50 ) :
        ball.dx *= -1