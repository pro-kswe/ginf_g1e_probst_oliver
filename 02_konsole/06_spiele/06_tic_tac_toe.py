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

while True:
    print(f"{feld_1}{feld_2}{feld_3}")
    print(f"{feld_4}{feld_5}{feld_6}")
    print(f"{feld_7}{feld_8}{feld_9}")

    if wer_ist_am_zug == 1:
        symbol = "X"
    if wer_ist_am_zug == 2:
        symbol = "O"
    
    position = int(input(f"Spieler {wer_ist_am_zug}: Wo soll das {symbol} gesetzt werden?"))
    
    if position == 1:
        feld_1 = symbol
    if position == 2:
        feld_2 = symbol
    if position == 3:
        feld_3 = symbol
    if position == 4:
        feld_4 = symbol
    if position == 5:
        feld_5 = symbol
    if position == 6:
        feld_6 = symbol
    if position == 7:
        feld_7 = symbol
    if position == 8:
        feld_8 = symbol
    if position == 9:
        feld_9 = symbol

    if feld_1 == feld_2 and feld_1 == feld_3:
        print(10 * "-")
        print(f"{feld_1}{feld_2}{feld_3}")
        print(f"{feld_4}{feld_5}{feld_6}")
        print(f"{feld_7}{feld_8}{feld_9}")
        print(10 * "-")
        print(f"Spieler {wer_ist_am_zug} gewinnt!")
        break

    if wer_ist_am_zug == 1:
        nächster_spieler = 2
    if wer_ist_am_zug == 2:
        nächster_spieler = 1
    wer_ist_am_zug = nächster_spieler

    print(10 * "-")
