import calendar as cal
import random as rd

anzahl = rd.randrange(1, 13)
print(f"Sie erhalten {anzahl} Stücke von diesem leckeren Apfelkuchen.")
for _ in range(anzahl):
    print("Kuchenstück")
