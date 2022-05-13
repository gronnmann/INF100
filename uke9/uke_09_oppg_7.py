def word_comparison(str1, str2):
    str1 = set(str1)
    str2 = set(str2)

    return {
        "In common": str1.intersection(str1, str2),
        "Unique to first word": str1.difference(str2),
        "Unique to second word": str2.difference(str1),
    }


print(word_comparison("computer", "science"))
