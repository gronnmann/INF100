instruction_direction = {
    "left": 1,
    "right": -1,
}


def write_turtle_str(instructions):
    """
    Take a list of instructions and return a turtle program that draws them.
    
    Valid instructions are 
    - left NN
    - right NN
    - forward NN
    - up
    - down
    
    where NN is an integer
    """
    turtle_str = ["import turtle as t"]

    left_size = 0

    for line in instructions:
        try:
            instruction, size = line.split()
        except:
            instruction, size = line.strip(), ""

        if instruction in instruction_direction.keys() and size != "":
            left_size += instruction_direction[instruction] * int(size)  # spesifisert where NN is an integer
        else:
            if left_size != 0:
                turtle_str.append(get_optimized_str(left_size))
                left_size = 0

            turtle_str.append(f"t.{instruction}({size})")

    if left_size != 0:  # i tilfelle left/right er siste kommando og programmet risikere glømme det
        turtle_str.append(get_optimized_str(left_size))

    turtle_str.append("t.done()")

    turtle_str = "\n".join(turtle_str)

    return turtle_str


def get_optimized_str(left_size: int):
    optimized_instruction = "left" if left_size > 0 else "right"  # kan like greitt bruke right når left er negativ
    optimized_size = left_size if left_size > 0 else -1 * left_size  # left(-30) tilsvarer right(30)

    return f"t.{optimized_instruction}({optimized_size})"


############################################
# don't modify after this point ############
############################################

instructions = """\
forward 50
up 
forward 100
down 
forward 50
left 90
right 20
left 30
left 100
right 110
forward 50
left 90
forward 50
left 90
forward 50""".split('\n')

if __name__ == "__main__":
    result = write_turtle_str(instructions)
    print(result)
