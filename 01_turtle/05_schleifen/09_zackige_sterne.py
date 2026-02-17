import random as rd
import turtle as t

farbe = "red"
t.pencolor(farbe)
t.speed(10)
for _ in range(5):
    a = rd.randrange(50, 201)
    for _ in range(5):
        t.fd(a)
        t.rt(144)
    t.lt(72)
