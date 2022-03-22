from src_py.util.option import Option


class Fibonacci(Option):
    def __init__(self):
        super().__init__()
        self.name = "Fibonacci"
        self.steps = 0
        self.number = [0, 1]

    def tester(self):
        # self.steps = int(input("How many steps? "))
        self.steps = 15
        self.fibonacci(1)
        # Print
        for i in self.number:
            print(i, "", end="")
        # Reset
        self.number = [0, 1]

    def fibonacci(self, n):
        self.number.append(self.number[n - 1] + self.number[n])
        if n < self.steps:
            self.fibonacci(n + 1)
