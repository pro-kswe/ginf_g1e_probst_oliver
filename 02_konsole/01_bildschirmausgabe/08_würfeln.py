import random as rd

print("Würfel würfeln")
print()
print("Anzahl der Würfe:")
anzahl = rd.randrange(10, 21)
print(anzahl)
print()

for _ in range(anzahl):
    augenzahl = rd.randrange(1, 7)
    print("Der Würfel rollt...")
    print(augenzahl)
    print()
