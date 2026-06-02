import random as rd

geheime_zahl = rd.randrange(1, 101)

while True:
    geratene_zahl = int(input("Bitte eine Zahl zwischen 1 und 100 eingeben:"))

    if geheime_zahl == geratene_zahl:
        print("Juhu! Zahl ist korrekt!")
        break

    if geratene_zahl < geheime_zahl:
        print("Ihre Zahl war zu klein.")

    if geratene_zahl > geheime_zahl:
        print("Ihre Zahl war zu gross.")
