import random as rd

print("Prüfungstag")
note = rd.randrange(1, 7)
faecher = ["Informatik", "Mathematik", "Deutsch"]
fach = rd.choice(faecher)
print(f"Notenwürfel für das Fach: {fach}")
print(f"Ihre gewürfelte Note lautet: {note}")
