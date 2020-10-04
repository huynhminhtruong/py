import turtle

# Setup Screen
screen = turtle.Screen()
screen.title("Game 1")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Setup Paddle A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("white")
player_a.penup()
player_a.goto(-350, 0)

# Setup Paddle B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("white")
player_b.penup()
player_b.goto(350, 0)

# Setup Ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Moving
def player_a_moving_up():
    y = player_a.ycor()
    y += 20
    player_a.sety(y)

def player_a_moving_down():
    y = player_a.ycor()
    y -= 20
    player_a.sety(y)

def player_b_moving_up():
    y = player_b.ycor()
    y += 20
    player_b.sety(y)

def player_b_moving_down():
    y = player_b.ycor()
    y -= 20
    player_b.sety(y)

# Handle keyboard input
screen.listen()
screen.onkeypress(player_a_moving_up, "w")
screen.onkeypress(player_a_moving_down, "s")
screen.onkeypress(player_b_moving_up, "Up")
screen.onkeypress(player_b_moving_down, "Down")

# Main game loop
while True:
    screen.update()

    # Moving ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1