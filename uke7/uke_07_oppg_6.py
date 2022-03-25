def pigify(phrase):
    if isVocal(phrase[0]):
        return phrase + "way"
    else:
        to_add = ""
        to_cut = -1
        for i, char in enumerate(phrase):
            if not isVocal(char):
                to_add += char
            else:
                to_cut = i
                break

        if to_cut != -1:
            phrase = phrase[to_cut:]
        else:
            to_add = ""  # om ingen bokstava å kutte, ikke legg til noe

        return phrase + to_add + "ay"


def pigify_sentence(sentence):
    split = sentence.split(" ")

    translated = map(pigify, split)

    return " ".join(translated)


def isVocal(char):
    char = char.upper()
    return True if char in "AEIOUÆØÅ" else False
