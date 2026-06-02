import random as rd
import time as ti

print("Willkommen zum Zahlen-Raten-Spiel!")
print(16 * '\U0001F579')

print("Ich wähle eine geheime Zahl zwischen 1 und 100...")
for _ in range(5):
    print("Ich schaue in die...\U0001F52E")
    ti.sleep(1)
geheime_zahl = rd.randrange(1, 101)
print("So nun habe ich die Zahl ausgewählt.")

while True:
    getippte_zahl = int(input("Bitte eine ganze Zahl zwischen 1 und 100 eingeben:"))

    if getippte_zahl < geheime_zahl:
        print("Zu klein! Bitte noch einmal probieren!")
        ti.sleep(3)
    if getippte_zahl > geheime_zahl:
        print("Zu gross! Bitte noch einmal probieren!")
        ti.sleep(3)
    if getippte_zahl == geheime_zahl:
        print("Korrekt!")
        break
