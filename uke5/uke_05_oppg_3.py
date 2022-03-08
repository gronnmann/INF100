from math import log10


def pH_from_conc(conc):
    return -1.0 * log10(conc)

def find_acidity(conc):
    pH = pH_from_conc(conc)

    if pH < 7.0:
        return "acidic"
    elif pH > 7.0:
        return "basic"
    else:
        return "neutral"

