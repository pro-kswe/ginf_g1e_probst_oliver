import random as rd

farben = ["rot", "grün", "blau"]
anzahl = rd.randrange(1, 11)

for _ in range(anzahl):
    farbe = rd.choice(farben)
    print(farbe)
