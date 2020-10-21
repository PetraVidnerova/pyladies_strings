# Napis funkci zamen(retezec, pozice, znak)


def zamen(retezec, pozice, znak):
    """ Tato funkce vrátí řetězec, který má na dané pozici daný znak; 
    jinak je stejný jako původní retezec. 
    Např:
    zamen('palec', 0, 'v') == 'valec'
    zamen('valec', 2, 'j') == 'vajec'
    """
    ...


kouc = "Petr Messner"
jiny_kouc = zamen(kouc, 6, "L")  # Petr Lessner

print("Můj oblíbený kouč je ", kouc, "a", jiny_kouc)
print(" .... a Mirek Brabenec!")
