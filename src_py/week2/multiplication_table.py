from src_py.util.option import Option


class MultiplicationTable(Option):
    def __init__(self):
        super().__init__()
        self.name = "Multiplication Table"

    def __call__(self):
        t = Tables10To99()
        t(87)
        t(38)
        t(92)


class Tables10To99:
    def __init__(self):
        pass

    def __call__(self, number):
        pass
