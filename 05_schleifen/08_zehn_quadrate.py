import random as rd
import turtle as t

a = rd.randrange(25, 51)
farbe = "blue"
t.pencolor(farbe)
staerke = rd.randrange(1, 6)
t.pensize(staerke)
for _ in range(10):
    for _ in range(4):
        t.fd(a)
        t.lt(90)
    t.fd(a)
