class RecursiveA:
    def __init__(self):
        self.name = "recursive_a"
        self.space = ""
        self.counter = 0

    def get_name(self):
        return self.name

    def tester(self):
        print(self.space + "A")
        self.space = self.space + " "
        self.counter += 1
        if self.counter < 10:
            self.process()
        else:
            self.counter = 0
