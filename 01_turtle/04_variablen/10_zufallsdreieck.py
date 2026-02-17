import turtle
import random

# Bei randrange daran denken, dass
# die zweite Zahl um 1 grösser sein muss
x_1 = random.randrange(-100, 101)
x_2 = random.randrange(-100, 101)
x_3 = random.randrange(-100, 101)
y_1 = random.randrange(-200, 201)
y_2 = random.randrange(-200, 201)
y_3 = random.randrange(-200, 201)
d = random.randrange(10, 26)
turtle.pensize(2)
turtle.pu()
turtle.goto(x_1, y_1)
turtle.pd()
turtle.pencolor("red")
turtle.dot(d)
turtle.goto(x_2, y_2)
turtle.pencolor("green")
turtle.dot(d)
turtle.goto(x_3, y_3)
turtle.pencolor("blue")
turtle.dot(d)
turtle.goto(x_1, y_1)
