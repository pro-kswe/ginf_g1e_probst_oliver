import random as rd

betrag = rd.randrange(100, 2001)
anzahl_tausender = betrag // 1000
rest_1 = betrag % 1000
anzahl_zweihunderter = rest_1 // 200
rest_2 = rest_1 % 200
anzahl_hunderter = rest_2 // 100
rest_3 = rest_2 % 100
anzahl_fuenfziger = rest_3 // 50
rest_4 = rest_3 % 50
anzahl_zwanziger = rest_4 // 20
rest_5 = rest_4 % 20
anzahl_zehner = rest_5 // 10
anzahl_einer = rest_5 % 10
print("RANDOM-Bankomat")
print(f"Es werden CHF {betrag} abgehoben.")
print(f"1000er: {anzahl_tausender}")
print(f"200er: {anzahl_zweihunderter}")
print(f"100er: {anzahl_hunderter}")
print(f"50er: {anzahl_fuenfziger}")
print(f"20er: {anzahl_zwanziger}")
print(f"10er: {anzahl_zehner}")
print(f"Münzen (1er): {anzahl_einer}")
