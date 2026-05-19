import random as rd

wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
wochentag = rd.choice(wochentage)
speisen = ["Pommes", "Linsen-Dal", "Spaghetti"]
speise = rd.choice(speisen)
print(f"Am {wochentag} gibt es {speise} in der Mensa.")
print("Wie finden wir das?")
anzahl = rd.randrange(1, 7)
for _ in range(anzahl):
    print("Juhu")
