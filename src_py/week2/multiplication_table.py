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

        self.table_size = 0

    def __call__(self):
        self.create_higher_digit_factors(self.higher_digit)
        self.create_lower_digit_factors(self.lower_digit)

        print(self.higher_digit_array)
        print(self.lower_digit_array)

    def create_higher_digit_factors(self, digit):
        # Digit constant
        d = digit
        # Get the factors, while also recording the max iterations for the other digit.
        while digit < 100:
            digit += d
            self.higher_digit_array.append(digit)
            self.table_size += 1

    def create_lower_digit_factors(self, digit):
        # Digit constant and iterator
        d = digit
        i = 0
        # Get the factors.
        while i < self.table_size:
            digit += d
            self.lower_digit_array.append(digit)
            i += 1
