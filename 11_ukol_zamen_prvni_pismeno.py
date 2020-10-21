# Pozor, tento program je spatne.
# Dokazes jej opravit?


def zakryj_prvni_pismeno(retezec):
    """
    Funkce vrati retezec shodny se zadanym retezcem, 
    ale prvni pismeno nahradi hvězdičkou.
    """
    retezec[1] = "*"
    return retezec


print(zakryj_prvni_pismeno("PyLadies"))
