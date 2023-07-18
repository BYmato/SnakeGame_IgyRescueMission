import turtle
from turtle import *
import time
import random

screen = Screen()
screen.bgcolor("sandybrown")
screen.title("Welcome to SnakeGame")
screen.setup(525, 550)
screen.tracer(False)
screen.title("IGY's rescue mission!")

# SCORE BOARD

score = 0
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("gold")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(240, 220)
score_sign.write("Score: 0", align="right", font=("Verdana", 14, "bold"))

# SCORE BOARD HIGHEST

highest_score = 0
score_sign_highest = Turtle("square")
score_sign_highest.speed(0)
score_sign_highest.color("gold")
score_sign_highest.penup()
score_sign_highest.hideturtle()
score_sign_highest.goto(-250, 220)
score_sign_highest.write("Highest: 0", align="left", font=("Verdana", 14, "bold"))


# EDGE

screen_edge = Turtle("circle")
screen_edge.shapesize(25)
screen_edge.color("skyblue")
screen_edge.goto(-3, 0)


# SNAKE HEAD

head = Turtle("turtle")
head.color("green")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"
head.shapesize(1)

# SMALL TURTLES

small_turtles = []

# FOOD

food = Turtle("turtle")
food.color("lightgreen")
food.penup()
food.goto(100, 100)
food.shapesize(0.7)

# MOVEMENT

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def move_up():
    if head.direction != "down":
        head.direction = "up"
        head.setheading(90)
        head.heading()
        body.setheading(head.heading())
        body.heading()

def move_down():
    if head.direction != "up":
        head.direction = "down"
        head.setheading(270)
        head.heading()
        body.setheading(head.heading())
        body.heading()

def move_left():
    if head.direction != "right":
        head.direction = "left"
        head.setheading(180)
        head.heading()
        body.setheading(head.heading())
        body.heading()

def move_right():
    if head.direction != "left":
        head.direction = "right"
        head.setheading(360)
        head.heading()
        body.setheading(head.heading())
        body.heading()

# KEY INPUTS

screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# MAIN CYCLE

while True:

    screen.update()

    # EDGE COLLISION

    # if head.xcor() > 215 or head.xcor() < -215 or head.ycor() > 215 or head.ycor() < -215:
    if screen_edge.distance(head) > 240:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"

        # HIDING BODY

        for one_body_part in small_turtles:
            one_body_part.goto(1500, 1500)

        small_turtles.clear()

        # RESET SCORE

        score = 0
        score_sign.clear()
        score_sign.write(f"Score: {score}", align="right", font=("Verdana", 14, "bold"))

    # ADDING BODY

    if head.distance(food) < 20:
        food.goto(random.randint(-170, 170), random.randint(-170, 170))

        # ADDING small TURTLES
        body = Turtle("turtle")
        body.color("lightgreen")
        body.shapesize(0.7)
        body.speed(0)
        body.penup()
        small_turtles.append(body)

        # ADDING SCORE

        score += 10

        if score > highest_score:
            highest_score = score

        score_sign.clear()
        score_sign_highest.clear()
        score_sign.write(f"Score: {score}", align="right", font=("Verdana", 14, "bold"))
        score_sign_highest.write(f"Highest: {highest_score}", align="left", font=("Verdana", 14, "bold"))

    for i in range(len(small_turtles) - 1, 0, -1):
        x = small_turtles[i - 1].xcor()
        y = small_turtles[i - 1].ycor()
        small_turtles[i].goto(x, y)
        small_turtles[i].setheading(head.heading())
        small_turtles[i].heading()


    if len(small_turtles) > 0:
        x = head.xcor()
        y = head.ycor()
        small_turtles[0].goto(x, y)

    move()

    # CRASHING IN BODY

    for one_body_part in small_turtles:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"

            for one_body_part in small_turtles:
                one_body_part.goto(1500, 1500)

            small_turtles.clear()

            # RESET SCORE

            score = 0
            score_sign.clear()
            score_sign.write(f"Score: {score}", align="right", font=("Verdana", 14, "bold"))

    time.sleep(0.1)


screen.exitonclick()