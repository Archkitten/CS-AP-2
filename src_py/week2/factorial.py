from src_py.util.option import Option


class Factorial(Option):
    def __init__(self):
        super().__init__()
        self.name = "Factorial"

    def __call__(self):
        # number = int(input("Input a number to get a factorial from: "))
        # f_obj = FactorialClass(number)
        # f_obj.factorial()
        zero_factorial = FactorialClass(0)
        zero_factorial.factorial()

        three_factorial = FactorialClass(3)
        three_factorial.factorial()

        four_factorial = FactorialClass(4)
        four_factorial.factorial()

        six_factorial = FactorialClass(6)
        six_factorial.factorial()


class FactorialClass:
    def __init__(self, n):
        self.n = n

    def factorial(self):
        factorial = 1
        number = self.n
        while number > 0:
            factorial *= number
            number -= 1

        print(str(self.n) + "! is " + str(factorial))
