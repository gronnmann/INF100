def multiply_5_plus_2(my_number):
    return my_number*5 + 2

def make_excited(text):
    return text + "!"

def name_age(name, gender, age):
    return f"{name} er {gender} og er {age} år gammel."

def my_math(x, y):
    return x**2 + 2*y

def hvem_yngre_string(person, age):
    return f"{person} er {age} år og er yngre."

def hvem_yngre(person1, age1, person2, age2):
    return hvem_yngre_string(person1, age1) if age1 < age2 else hvem_yngre_string(person2, age2)