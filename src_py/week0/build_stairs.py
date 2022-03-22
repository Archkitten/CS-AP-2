from src_py.util.option import Option


class BuildStairs(Option):
    def __init__(self):
        super().__init__()
        self.name = "Build Stairs"
        self.space = ""

    def tester(self):
        counter = 0
        # steps = int(input("How many steps? "))
        steps = 6

        while counter < steps:
            self.stairs()
            counter += 1
        self.space = ""

    def stairs(self):
        print(self.space + "|__")
        self.space = self.space + " - "
