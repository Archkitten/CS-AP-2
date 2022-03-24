class Option:
    def __init__(self):
        self.name = "Option"

    def __call__(self):
        print("Selected: " + self.name)

    def get_name(self):
        return self.name
