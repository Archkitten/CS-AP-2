from number_swap import NumberSwap
from matrix_to_text import MatrixToText
from christmas_tree import ChristmasTree

# List of options, easily editable. Let's go lazy programming!
number_swap = NumberSwap()
matrix_to_text = MatrixToText()
christmas_tree = ChristmasTree()
options_list_editable = [number_swap, matrix_to_text, christmas_tree]


# Reusable menu() function.
def menu(banner, options_list):
    running = True
    while running:
        # Print initial message along with a new line.
        print()
        print(banner)

        # Prints out all available options.
        i = 1
        for o in options_list:
            print(i, "-", o.get_name())
            i += 1
        print("0 - exit")

        # Asks for user input.
        user_input = input(">")
        try:
            user_input = int(user_input)
            # Break out of while loop if user_input is 0.
            if user_input == 0:
                running = False
            # Otherwise, run the selection.
            else:
                try:
                    options_list[user_input - 1].process()
                except IndexError:
                    print("Invalid Input: Selection out of range")
        except ValueError:
            print("Invalid Input: Not a number")
        except UnboundLocalError:
            print("Invalid Input")


# Run menu().
menu("Pick an option below!", options_list_editable)
