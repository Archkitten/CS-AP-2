from src_py.util.option import Option


class MultiplicationTable(Option):
    def __init__(self):
        super().__init__()
        self.name = "Multiplication Table"

    def __call__(self):
        a = Tables10To99(87)
        a()
        print()
        b = Tables10To99(38)
        b()
        print()
        c = Tables10To99(92)
        c()


class Tables10To99:
    def __init__(self, number):
        # Convert int into string.
        number_string = str(number)
        # Convert string into array.
        string_array = list(number_string)
        # Turn array of Strings back into array of ints.
        number_array = []
        for s in string_array:
            number_array.append(int(s))
        # Sort array in order to start from the highest digit.
        self.flipped = False
        if number_array[0] < number_array[1]:
            number_array.reverse()
            self.flipped = True

        # Constructor
        self.higher_digit = number_array[0]
        self.lower_digit = number_array[1]

        self.higher_digit_array = []
        self.lower_digit_array = []

        # This is multiplied by the Actual Tens Place, either coming from higher_digit_array or lower_digit_array.
        self.ones_place_tens_column = []
        # This is appended onto the final number.
        self.ones_place_ones_column = []

        # Final Result
        self.final_result = []

        # Counter for how many times the number should be multiplied, must stay consistent between digits.
        self.table_size = 0

    def __call__(self):
        self.create_higher_digit_factors(self.higher_digit)
        self.create_lower_digit_factors(self.lower_digit)

        if self.flipped:
            # Higher is the true ones place, Lower is the true tens place.
            self.split_the_ones_place(self.higher_digit_array)
            self.calculate_final_result(self.lower_digit_array)
            # print(self.lower_digit_array)
            # print(self.higher_digit_array)
        else:
            # Lower is the true ones place, Higher is the true tens place.
            self.split_the_ones_place(self.lower_digit_array)
            self.calculate_final_result(self.higher_digit_array)
            # print(self.higher_digit_array)
            # print(self.lower_digit_array)
        # print(self.ones_place_tens_column)
        # print(self.ones_place_ones_column)
        # print(self.final_result)
        self.format_entire_multiplication_table()

    def format_entire_multiplication_table(self):
        i = 0
        if self.flipped:
            while i < self.table_size:
                print(str(self.lower_digit_array[i]) + "  ", end="")
                print(str(self.ones_place_tens_column[i]) + " ", end="")
                print(str(self.ones_place_ones_column[i]) + " ", end="")
                print("(" + str(self.lower_digit_array[i]) + "+" + str(self.ones_place_tens_column[i]) + ") ", end="")
                print(self.final_result[i])
                i += 1
        else:
            while i < self.table_size:
                print(str(self.higher_digit_array[i]) + "  ", end="")
                print(str(self.ones_place_tens_column[i]) + " ", end="")
                print(str(self.ones_place_ones_column[i]) + " ", end="")
                print("(" + str(self.higher_digit_array[i]) + "+" + str(self.ones_place_tens_column[i]) + ") ", end="")
                print(self.final_result[i])
                i += 1

    def create_higher_digit_factors(self, digit):
        # Digit constant
        d = digit
        # Get the factors, while also recording the max iterations for the other digit.
        while digit < 100:
            self.higher_digit_array.append(digit)
            self.table_size += 1
            digit += d

    def create_lower_digit_factors(self, digit):
        # Digit constant and iterator
        d = digit
        i = 0
        # Get the factors.
        while i < self.table_size:
            self.lower_digit_array.append(digit)
            digit += d
            i += 1

    def split_the_ones_place(self, ones_array):
        for digit in ones_array:
            if digit < 10:
                # Tenths place is 0
                self.ones_place_tens_column.append(0)
                # One's place is digit
                self.ones_place_ones_column.append(digit)
            else:
                # int(digit / 10) gives the value of the number in the tens place
                self.ones_place_tens_column.append(int(digit / 10))
                # digit % 10 gives the value of the number in the ones place (remainder)
                self.ones_place_ones_column.append(digit % 10)

    def calculate_final_result(self, true_ten_list):
        i = 0
        for true_ten in true_ten_list:
            # Tens place added to one's place ten column, then one's place one column is appended to the end.
            self.final_result.append((true_ten + self.ones_place_tens_column[i]) * 10 + self.ones_place_ones_column[i])
            i += 1
