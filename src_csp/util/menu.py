# Reusable menu() class and function.
class Menu:
    def __init__(self, banner, options_list):
        self.banner = banner
        self.options_list = options_list

    def menu(self):
        running = True
        while running:
            # Print initial message along with a new line.
            print()
            print(self.banner)

            # Prints out all available options.
            print("0 - Exit")
            i = 1
            for o in self.options_list:
                print(i, "-", o.get_name())
                i += 1

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
                        self.options_list[user_input - 1].tester()
                    except IndexError:
                        print("Invalid Input: Selection out of range")
            except ValueError:
                print("Invalid Input: Not a number")
            except UnboundLocalError:
                print("Invalid Input")
