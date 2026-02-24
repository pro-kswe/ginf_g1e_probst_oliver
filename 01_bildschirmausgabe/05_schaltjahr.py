import calendar as cal
import random as rd

jahr = rd.randrange(1900, 2027)
print("Zufälliges Jahr:")
print(jahr)
print("Ist es ein Schaltjahr?")
antwort = cal.isleap(jahr)
print(antwort)
