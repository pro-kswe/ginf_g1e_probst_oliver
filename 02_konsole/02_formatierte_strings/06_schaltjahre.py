import calendar as cal
import random as rd

anzahl = rd.randrange(10, 21)
print(f"Es werden {anzahl} zufällige Jahre überprüft.")
for _ in range(anzahl):
    zufallsjahr = rd.randrange(1900, 2027)
    antwort = cal.isleap(zufallsjahr)
    print(f"Es ist das Jahr {zufallsjahr}. Ist es ein Schaltjahr? {antwort}")
