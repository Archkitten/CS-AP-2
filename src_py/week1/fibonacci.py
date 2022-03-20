from src_py.util.option import Option


class Fibonacci(Option):
    def __init__(self):
        super().__init__()
        self.name = "Fibonacci"
        self.steps = 0
        self.number = [0, 1]

    def tester(self):
        self.steps = int(input("How many steps? "))
        self.fibonacci(1)
        # Reset
        self.number = [0, 1]

    def fibonacci(self, n):
        print(self.number)
        self.number.append(self.number[n - 1] + self.number[n])
        if n < self.steps:
            self.fibonacci(n + 1)
