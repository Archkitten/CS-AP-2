from src_csp.util.option import Option


class RecursiveA(Option):
    def __init__(self):
        super().__init__()
        self.name = "Recursive A"
        self.space = ""
        self.counter = 0

    def tester(self):
        print(self.space + "A")
        self.space = self.space + " "
        self.counter += 1
        if self.counter < 10:
            self.tester()
        else:
            self.counter = 0
