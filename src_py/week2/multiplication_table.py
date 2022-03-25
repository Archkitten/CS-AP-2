from src_py.util.option import Option


class MultiplicationTable(Option):
    def __init__(self):
        super().__init__()
        self.name = "Multiplication Table"

    def __call__(self):
        t = Tables10To99()
        t(87)
        print()
        t(38)
        print()
        t(92)


class Tables10To99:
    def __init__(self):
        self.table_size = 0

    def __call__(self, number):
        # Convert int into string.
        number_string = str(number)
        # Convert string into array.
        string_array = list(number_string)
        # Turn array of Strings back into array of ints.
        number_array = []
        for s in string_array:
            number_array.append(int(s))
        # Sort array in order to start from the highest digit.
        number_array.sort(reverse=True)

        # Iterate through array, get each digit's factors.
        for digit in number_array:
            # Store factors of digit.
            factor_array = []
            # Factor counter.
            if self.table_size == 0:
                d = digit
                while digit < 100:
                    digit += d
                    factor_array.append(digit)
                    self.table_size += 1
            else:
                i = 0
                d = digit
                while i < self.table_size:
                    digit += d
                    factor_array.append(digit)
            print(factor_array)


