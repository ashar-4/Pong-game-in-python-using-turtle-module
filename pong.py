import turtle
import os

def pong():
	wn = turtle.Screen()
	wn.title("Pong by ashar")
	wn.bgcolor("chocolate")
	wn.setup(width=1400, height=800)
	wn.tracer(0)	# stops the window from updating

	# Score
	score_a = 0
	score_b = 0

	# Paddle A
	paddle_a = turtle.Turtle()
	paddle_a.speed(0)
	paddle_a.shape("square")
	paddle_a.color("black")
	paddle_a.shapesize(stretch_wid=5, stretch_len=1)
	paddle_a.penup()
	paddle_a.goto(-650, 0)

	# Paddle B
	paddle_b = turtle.Turtle()
	paddle_b.speed(0)
	paddle_b.shape("square")
	paddle_b.color("black")
	paddle_b.shapesize(stretch_wid=5, stretch_len=1)
	paddle_b.penup()
	paddle_b.goto(650, 0)

	# Ball
	ball = turtle.Turtle()
	ball.speed(0)
	ball.shape("circle")
	ball.color("blue")
	ball.penup()
	ball.goto(0, 0)
	ball.dx = 0.2
	ball.dy = 0.2

	# Pen
	pen = turtle.Turtle()
	pen.speed(0)
	pen.color("black")
	pen.penup()
	pen.hideturtle()
	pen.goto(0, 300)
	pen.write("Player A: 0\t\t\t\t\t\tPlayer B: 0", align="center", font=("Courier", 24, "normal"))

	#Box
	line1 = turtle.Turtle()
	line1.color("white")
	line1.penup()
	line1.hideturtle()
	line1.goto(0, 300)
	line1.pendown()
	line1.forward(670)
	line1.right(90)
	line1.forward(620)
	line1.right(90)
	line1.forward(1340)
	line1.right(90)
	line1.forward(620)
	line1.right(90)
	line1.forward(670)

	# Function
	def paddle_a_up():
		y = paddle_a.ycor()
		y += 20
		paddle_a.sety(y)

	def paddle_a_down():
		y = paddle_a.ycor()
		y -= 20
		paddle_a.sety(y)

	def paddle_b_up():
		y = paddle_b.ycor()
		y += 20
		paddle_b.sety(y)

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

	# def fun1():
	# 	exit()

	# Main game loop
	while True:
		wn.update()

		# Move the ball
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)

		# Border checking
		if ball.ycor() > 290:
			ball.sety(290)
			ball.dy *= -1
			os.system("aplay bounce.wav&")

		if ball.ycor() < -310:
			ball.sety(-310)
			ball.dy *= -1
			os.system("aplay bounce.wav&")
		
		if ball.xcor() > 690:
			ball.goto(0, 0)
			ball.dx *= -1
			score_a += 1
			pen.clear()
			pen.write("Player A: {}\t\t\t\t\t\tPlayer B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

		if ball.xcor() < -690:
			ball.goto(0, 0)
			ball.dx *= -1
			score_b += 1
			pen.clear()
			pen.write("Player A: {}\t\t\t\t\t\tPlayer B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
		
		# Paddle and ball collisions
		if (ball.xcor() > 640 and ball.xcor() < 650) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
			ball.setx(640)
			ball.dx *= -1
			os.system("aplay bounce.wav&")

		if (ball.xcor() < -640 and ball.xcor() > -650) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
			ball.setx(-640)
			ball.dx *= -1
			os.system("aplay bounce.wav&")

		# wn.exitonclick()
		# onscreenclick(fun1)

def menu():
	wn = turtle.Screen()
	wn.title("Pong by ashar")
	wn.bgcolor("black")
	wn.setup(width=800, height=600)
	# wn.listen()
	pen = turtle.Turtle()
	pen.hideturtle()
	pen.color("white")
	pen.penup()
	pen.goto(-100, 190)
	pen.pendown()
	pen.forward(200)
	def text(posx, posy, str):
		pen.penup()
		pen.goto(posx, posy)
		pen.pendown()
		pen.write(str, align="center", font=("Courier", 28, "normal"))

	def fun1(x, y):
		if y >= 40 and y <= 60:
			pong()
		# text(0,0,"{} {}".format(x, y))
		# return x,y

	text(0, 200, "Main Menu")
	text(0, 50, "New Game")
	text(0, -20, "Options")
	text(0, -90, "Exit")

	while True:
		# wn.update() 
		turtle.onscreenclick(fun1, 1)
		turtle.listen()
		# print(x, y)
		pass

menu()
# pong()