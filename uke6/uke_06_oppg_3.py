def complement(dna_string):
    dna_string = list(map(return_matching, dna_string))  # kjører alle verdiar gjennom returnMatching

    return "".join(dna_string[::-1])  # joiner listen til ein string, blir da string ikke list. Gjer DNAstring omvendt


def return_matching(char):
    if char == "A":
        return "T"
    elif char == "T":
        return "A"
    elif char == "C":
        return "G"
    else:
        return "C"

