import calendar as cal
import random as rd

zufallsjahr = rd.randrange(1900, 2027)
antwort = cal.isleap(zufallsjahr)

print(f"Es ist das Jahr {zufallsjahr}. Ist es ein Schaltjahr? {antwort}")
