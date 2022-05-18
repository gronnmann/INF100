from tabulate import tabulate
import win32clipboard
import time


def get_user_input(start_msg: str, input_msg: str):
    data = []

    print(start_msg)

    print("""Available commands:
    'exit': Exit the input
    '': Copy from clipboard
    'autoclip': automatically copy when clipboard change (copy exit to exit)'""")

    while True:
        user_input = input(input_msg)
        if user_input == "exit":
            return data

        elif user_input == "":
            win32clipboard.OpenClipboard()
            clipboard_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            user_input = clipboard_data

        elif user_input == "autoclip":
            win32clipboard.OpenClipboard()
            win32clipboard.SetClipboardText("")
            start_clipboard_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            while True:
                win32clipboard.OpenClipboard()
                clipboard_data = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()

                if clipboard_data == "exit":
                    win32clipboard.OpenClipboard()
                    win32clipboard.CloseClipboard()
                    break

                if clipboard_data != start_clipboard_data:
                    data.append(clipboard_data)
                    print(f"Auto-detected: {clipboard_data}")

                    start_clipboard_data = clipboard_data

                time.sleep(0.1)

            continue

        data.append(user_input)

        print(f"Registered data: {user_input}")


def mode_0():
    # Stage 1 - variable defining
    for x in get_user_input("Vennligs definer variablane.", "Definisjon:"):
        exec(x)

    # Stage 2 - Executing comparisons

    comparison_table = []  # Skal inneholde tuples i rekkefølge (comparison, bool, float, int, list, (-error), str)

    print("Lets input all the comparisons.")
    for x in get_user_input("Please enter expression to check", "Expression: "):

        try:
            new_variable = eval(x)

            comparison_table.append(
                (x,
                 "X" if isinstance(new_variable, bool) else "",
                 "X" if isinstance(new_variable, float) else "",
                 "X" if isinstance(new_variable, int) else "",
                 "X" if isinstance(new_variable, list) else "",
                 "",
                 "X" if isinstance(new_variable, str) else "",
                 type(new_variable)
                 )
            )

        except Exception:
            comparison_table.append((x, "", "", "", "", "X", "", "ERROR"))

    # Stage 3 - Print it all out neatly

    print(tabulate(comparison_table, headers=("Expression", "bool", "float", "int", "list", "(-error-)", "str", "TYPE"),
                   tablefmt="fancy_grid"))


def mode_1():
    comparison_table = []  # tuple: (expression, true, false)

    for x in get_user_input("Please input expressons to evaluate", "Expression: "):
        try:

            evaluated = eval(x)

            comparison_table.append((x, "X" if evaluated is False else "", "X" if evaluated is True else ""))
        except Exception:
            comparison_table.append(x, "ERR", "ERR")

    print(tabulate(comparison_table, headers=("Expression", "False", "True"), tablefmt="fancy_grid"))


modes = {
    0: ("Find data type", mode_0),
    1: ("Find bool result", mode_1)
}


def start_program():
    print("Vennligs spesifiser operasjonsmodus:")
    for k, v in modes.items():
        print(f"{k}: {v[0]}")
    print("Skriv exit for å avslutte")
    while True:
        user_input = input("Mode: ")

        if user_input == "exit":
            print("Ha det!")
            exit()

        if modes.get(int(user_input), -1) != -1:
            print(f"Using function: {modes[int(user_input)][0]}")

            modes[int(user_input)][1]()

            break


start_program()
