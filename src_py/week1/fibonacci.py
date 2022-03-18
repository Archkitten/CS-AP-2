from src_py.util.option import Option


class Fibonacci(Option):
    def __init__(self):
        super().__init__()
        self.name = "Fibonacci"
        self.number = [0, 1]

    def tester(self):
        self.fibonacci(1)

    def fibonacci(self, n):
        self.number.append(self.number[n - 1] + self.number[n])
        if n < 10:
            self.fibonacci(n + 1)
