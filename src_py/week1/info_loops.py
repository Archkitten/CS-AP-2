from src_py.util.option import Option


class InfoLoops(Option):
    def __init__(self):
        super().__init__()
        self.name = "Info Loops"
        self.info_db = [{"first_name": "Arch",
                         "last_name": "Huang",
                         "date_of_birth": "March 22, 2005",
                         "alias": ["Redkitten", "Flamewave", "Arch05", "Archkitten", "Crah05", "Ro"],
                         "minor_alias": ["Firekitten", "Starlight", "Orchid", "Sunset", "Shadow/Void"]}]
        self.info_db.append({"first_name": "??????",
                             "last_name": "???",
                             "date_of_birth": "XXXX XX, 2003",
                             "alias": ["Fallen Ferric"],
                             "minor_alias": ["???? ??????"]})

    def __call__(self):
        print("For Loop:")
        self.for_loop()
        print("While Loop:")
        self.while_loop()
        print("Recursion:")
        self.recursive_loop(0)

    def print_data(self, n):
        # using comma puts space between values
        print(self.info_db[n]["first_name"], self.info_db[n]["last_name"], self.info_db[n]["date_of_birth"])
        # \t is a tab indent, end="" make sure no return occurs
        print("\t", "Alias: ", end="")
        # join allows printing a string list with separator
        print(", ".join(self.info_db[n]["alias"]))
        # ----- Repeat -----
        print("\t", "Minor Alias: ", end="")
        print(", ".join(self.info_db[n]["minor_alias"]))
        # ------------------
        print()

    def for_loop(self):
        for n in range(len(self.info_db)):
            self.print_data(n)

    def while_loop(self):
        n = 0
        while n < len(self.info_db):
            self.print_data(n)
            n += 1
        return

    def recursive_loop(self, n):
        if n < len(self.info_db):
            self.print_data(n)
            self.recursive_loop(n + 1)
        return
