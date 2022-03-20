from src_py.util.option import Option


class Factorial(Option):
    def __init__(self):
        super().__init__()
        self.name = "Factorial"

    def tester(self):
        number = int(input("Input a number to get a factorial from: "))
        f_obj = FactorialClass(number)
        f_obj.factorial()


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
