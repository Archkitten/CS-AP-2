class NumberSwap:
    def __init__(self):
        self.name = "number_swap"
        self.a = 0
        self.b = 0

    def get_name(self):
        return self.name

    def process(self):
        self.a = input("Input first integer: ")
        self.b = input("Input second integer: ")
        if self.a > self.b:
            temp = self.a
            self.a = self.b
            self.b = temp
        print(self.a, self.b)
