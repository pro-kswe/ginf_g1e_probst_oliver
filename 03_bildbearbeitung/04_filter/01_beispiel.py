import PIL.Image as img

# Öffnet eine bestehende Bilddatei zur Bearbeitung
bild = img.open("portland.png")

for x in range(0, bild.width):
    for y in range(0, bild.height):

        # Lese die bestehenden Werte für rot,
        # grün und blau an den Koordinaten aus.
        r, g, b = bild.getpixel((x, y))
        
        r_neu = 2 * r
        g_neu = 2 * g
        b_neu = 2 * b
        
        bild.putpixel((x, y), (r_neu, g_neu, b_neu))
bild.save("01_beispiel_ergebnis.png")
