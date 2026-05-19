import calendar as cal
import random as rd

print("Nun werden 5 zufällige Jahreszahlen überprüft.")
print()

for _ in range(5):
    jahr = rd.randrange(1900, 2027)
    antwort = cal.isleap(jahr)
    print("Zufälliges Jahr:")
    print(jahr)
    print("Ist es ein Schaltjahr?")
    print(antwort)
    print()
    
print("ENDE")
