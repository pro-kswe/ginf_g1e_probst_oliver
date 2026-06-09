import random as rd

# Einmal machen
gegenstände = ["Schere", "Stein", "Papier"]
punkte_computer = 0 
punkte_spieler = 0
runde = 1

while True:
    # Wer zuerst 5 Punkte hat gewinnt das Spiel.
    if punkte_spieler == 5:
        print("Du hast 5 Punkte und gewinnst das Spiel.")
        break
    if punkte_computer == 5:
        print("Der Computer hat 5 Punkte und gewinnt das Spiel.")
        break

    print(f"{runde}. Runde")
    
    # Gegenstände wählen (zufällig und via Eingabe)
    computerwahl = rd.choice(gegenstände)
    # Variable spielerwahl speichert die Eingabe des Spielers
    spielerwahl = input("Bitte wähle Schere, Stein oder Papier:")

    # Eingabe prüfen, falls nicht korrekt nochmal fragen
    while True:
        if spielerwahl != "Schere" and spielerwahl != "Stein" and spielerwahl != "Papier":
            spielerwahl = input("Bitte wähle Schere, Stein oder Papier:")
        if spielerwahl == "Schere" or spielerwahl == "Stein" or spielerwahl == "Papier":
            break
    
    print(f"Du hast {spielerwahl} gewählt.")
    print(f"Computer hat {computerwahl} gewählt.")

    # Unentschieden prüfen (beide haben das gleiche gewählt)
    if computerwahl == spielerwahl:
        print("Unentschieden")
    
    # Variante mit and
    if computerwahl == "Schere" and spielerwahl == "Stein":
        print("Du gewinnst!")
        punkte_spieler = punkte_spieler + 1
    if computerwahl == "Schere" and spielerwahl == "Papier":
        print("Computer gewinnt!")
        punkte_computer = punkte_computer + 1

    # Variante mit verschachtelter if-Anweisung
    if computerwahl == "Stein":
        if spielerwahl == "Schere":
            print("Computer gewinnt!")
            punkte_computer = punkte_computer + 1
        if spielerwahl == "Papier":
            print("Du gewinnst!")
            punkte_spieler = punkte_spieler + 1

    if computerwahl == "Papier":
        if spielerwahl == "Schere":
            print("Du gewinnst!")
            punkte_spieler = punkte_spieler + 1
        if spielerwahl == "Stein":
            print("Computer gewinnt!")
            punkte_computer = punkte_computer + 1

    print("Punktestand")
    print(f"Computer: {punkte_computer}")
    print(f"Du: {punkte_spieler}")
    print(10 * "-")
    runde = runde + 1
