from src_csp.util.option import Option


class NumberSwap(Option):
    def __init__(self):
        super().__init__()
        self.name = "Number Swap"

    def tester(self):
        print(self.swap(1, 2))
        print(self.swap(60, 30))
        print(self.swap(9, -11))

    def swap(self, a, b):
        if a > b:
            temp = a
            a = b
            b = temp
        return a, b
