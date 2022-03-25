my_fridge_test = ["tomato sauce", "mustard", "potatoes", "carrots", "chicken", "frozen fish"]

meals_test = (
    # name of dish [0], ingredients [1]
    ("fish_sticks", ("frozen fish", "potatoes", "mustard")),
    ("chicken_curry", ("chicken", "curry paste", "carrots", "potatoes", "rice")),
    ("chicken_veg", ("chicken", "potatoes", "carrots")),
    ("pasta", ("spaghetti", "tomato sauce")),
)


def meal_list(fridge, ingredient_list):
    count = 0
    for ingredient in ingredient_list:
        if ingredient in fridge:
            count += 1

    return count == len(ingredient_list)


def meal_options(fridge, meals):
    return [x[0] for x in meals if meal_list(fridge, x[1])]


def to_buy(fridge, ingredient_list):
    return [x for x in ingredient_list if x not in fridge]
