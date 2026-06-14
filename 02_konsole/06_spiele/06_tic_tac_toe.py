feld_1 = 1
feld_2 = 2
feld_3 = 3
feld_4 = 4
feld_5 = 5
feld_6 = 6
feld_7 = 7
feld_8 = 8
feld_9 = 9

wer_ist_am_zug = 1
anzahl_züge = 0

while True:
    print(f"{feld_1}{feld_2}{feld_3}")
    print(f"{feld_4}{feld_5}{feld_6}")
    print(f"{feld_7}{feld_8}{feld_9}")

    if wer_ist_am_zug == 1:
        symbol = "X"
    if wer_ist_am_zug == 2:
        symbol = "O"

    gültiger_zug = False
    position = int(input(f"Spieler {wer_ist_am_zug}: Wo soll das {symbol} gesetzt werden?"))
    
    while gültiger_zug == False:
        if position == 1 and feld_1 == 1:
            gültiger_zug = True
            feld_1 = symbol
        if position == 2:
            gültiger_zug = True
            feld_2 = symbol
        if position == 3:
            gültiger_zug = True
            feld_3 = symbol
        if position == 4:
            gültiger_zug = True
            feld_4 = symbol
        if position == 5:
            gültiger_zug = True
            feld_5 = symbol
        if position == 6:
            gültiger_zug = True
            feld_6 = symbol
        if position == 7:
            gültiger_zug = True
            feld_7 = symbol
        if position == 8:
            gültiger_zug = True
            feld_8 = symbol
        if position == 9:
            gültiger_zug = True
            feld_9 = symbol

        if gültiger_zug == False:
            position = int(input(f"Ungültige Eingabe! Nochmal: \n Spieler {wer_ist_am_zug}: Wo soll das {symbol} gesetzt werden?"))

    anzahl_züge = anzahl_züge + 1

    if feld_1 == feld_2 and feld_1 == feld_3:
        print(10 * "-")
        print(f"{feld_1}{feld_2}{feld_3}")
        print(f"{feld_4}{feld_5}{feld_6}")
        print(f"{feld_7}{feld_8}{feld_9}")
        print(10 * "-")
        print(f"Spieler {wer_ist_am_zug} gewinnt!")
        break

    if feld_4 == feld_5 and feld_5 == feld_6:
        print(10 * "-")
        print(f"{feld_1}{feld_2}{feld_3}")
        print(f"{feld_4}{feld_5}{feld_6}")
        print(f"{feld_7}{feld_8}{feld_9}")
        print(10 * "-")
        print(f"Spieler {wer_ist_am_zug} gewinnt!")
        break

    if feld_7 == feld_8 and feld_9 == feld_10:
        print(10 * "-")
        print(f"{feld_1}{feld_2}{feld_3}")
        print(f"{feld_4}{feld_5}{feld_6}")
        print(f"{feld_7}{feld_8}{feld_9}")
        print(10 * "-")
        print(f"Spieler {wer_ist_am_zug} gewinnt!")
        break

    if feld_1 == feld_4 and feld_4 == feld_7:
        print(10 * "-")
        print(f"{feld_1}{feld_2}{feld_3}")
        print(f"{feld_4}{feld_5}{feld_6}")
        print(f"{feld_7}{feld_8}{feld_9}")
        print(10 * "-")
        print(f"Spieler {wer_ist_am_zug} gewinnt!")
        break

    if feld_2 == feld_5 and feld_5 == feld_8:
        print(10 * "-")
        print(f"{feld_1}{feld_2}{feld_3}")
        print(f"{feld_4}{feld_5}{feld_6}")
        print(f"{feld_7}{feld_8}{feld_9}")
        print(10 * "-")
        print(f"Spieler {wer_ist_am_zug} gewinnt!")
        break

    if feld_3 == feld_6 and feld_6 == feld_9:
        print(10 * "-")
        print(f"{feld_1}{feld_2}{feld_3}")
        print(f"{feld_4}{feld_5}{feld_6}")
        print(f"{feld_7}{feld_8}{feld_9}")
        print(10 * "-")
        print(f"Spieler {wer_ist_am_zug} gewinnt!")
        break

    if feld_1 == feld_5 and feld_5 == feld_9:
        print(10 * "-")
        print(f"{feld_1}{feld_2}{feld_3}")
        print(f"{feld_4}{feld_5}{feld_6}")
        print(f"{feld_7}{feld_8}{feld_9}")
        print(10 * "-")
        print(f"Spieler {wer_ist_am_zug} gewinnt!")
        break

    if feld_3 == feld_5 and feld_5 == feld_7:
        print(10 * "-")
        print(f"{feld_1}{feld_2}{feld_3}")
        print(f"{feld_4}{feld_5}{feld_6}")
        print(f"{feld_7}{feld_8}{feld_9}")
        print(10 * "-")
        print(f"Spieler {wer_ist_am_zug} gewinnt!")
        break

    if anzahl_züge == 9:
        print(10 * "-")
        print(f"{feld_1}{feld_2}{feld_3}")
        print(f"{feld_4}{feld_5}{feld_6}")
        print(f"{feld_7}{feld_8}{feld_9}")
        print(10 * "-")
        print("Unentschieden!")
        break

    if wer_ist_am_zug == 1:
        nächster_spieler = 2
    if wer_ist_am_zug == 2:
        nächster_spieler = 1
    wer_ist_am_zug = nächster_spieler

    print(10 * "-")
    