class MatrixToText:
    def __init__(self):
        self.name = "matrix_to_text"
        self.numpad = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [" ", 0, " "]]

    def get_name(self):
        return self.name

    def process(self):
        for i in self.numpad:
            for j in i:
                print(j, "", end="")
            print()
