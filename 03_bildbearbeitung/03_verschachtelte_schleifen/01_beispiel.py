import PIL.Image as img

# Ein neues Bild erstellen
bild = img.new("RGB", (500, 1000))

for x in range(0, bild.width):
    for y in range(0, bild.height):
        bild.putpixel((x, y), (200, 50, 100))

# Speichert das Bild in der Bilddatei beispiel.png
bild.save("beispiel.png")
