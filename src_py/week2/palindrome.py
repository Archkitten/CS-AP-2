from src_py.util.option import Option


class Palindrome(Option):
    def __init__(self):
        super().__init__()
        self.name = "Palindrome"

    def __call__(self):
        nd = NotDatabase()
        print("\nTest Case 1: A man, a plan, a canal -- Panama!")
        nd.input_word("A man, a plan, a canal -- Panama!")
        nd.is_it_a_palindrome()

        delta = NotDatabase()
        print("\nTest Case 2: When the light is running low, and the shadows start to grow...")
        delta.input_word("When the light is running low, and the shadows start to grow...")
        delta.is_it_a_palindrome()

        play = NotDatabase()
        print("\nTest Case 3: Are we not pure? “No, sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man—a prisoner up to new era.")
        play.input_word("Are we not pure? “No, sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man—a prisoner up to new era.")
        play.is_it_a_palindrome()


class NotDatabase:
    def __init__(self):
        self.word_array = []
        self.palindrome_array = []

    def input_word(self, test_word):
        for x in test_word:
            self.word_array.append(x)
            self.palindrome_array.append(x)
        # Tests the arrays
        # print(self.word_array)
        # print(self.palindrome_array)
        self.palindrome_array.reverse()

    def is_it_a_palindrome(self):
        # Turns the word array into a string
        word = ''
        for char in self.word_array:
            # Remove special characters like spaces, commas, and other punctuation.
            # char.lower() will automatically make the character lowercase.
            if char.isalnum():
                word = word + char.lower()
        # Turns the palindrome array into a string
        palindrome_word = ''
        for char in self.palindrome_array:
            # Remove special characters like spaces, commas, and other punctuation.
            # char.lower() will automatically make the character lowercase.
            if char.isalnum():
                palindrome_word = palindrome_word + char.lower()

        if word == palindrome_word:
            print(word + ' is a palindrome!')
        else:
            print(word + ' is not a palindrome, because the reverse is ' + palindrome_word)
