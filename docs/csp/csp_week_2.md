{% include navigation.html %}

# CSP

{% include csp_nav.html %}

## Week 2 - [Ticket](https://github.com/Archkitten/CS-AP-2/issues/6)

### 5.5 Notes

* Intellectual Property - Creative invention/product where an individual has ownership over (Intellectual property/rights).
  * Like things protected by copyright! ©
* Creative Commons license:
  * Creative Commons provides free licenses that can be modified based on the author's needs.
  * [Creative Commons Website - About CC Licenses](https://creativecommons.org/about/cclicenses/)
* Open Source:
  * Anyone else can freely redistribute or modify the program.
* Open Access:
  * Online research free of any and all restrictions, including copyright or license restrictions.
* Always give credit if you use someone else's works!

### [Tri 3 TPT 2.0 Legal and Ethical Concerns 5.5](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3-TPT-2.0-Legal-and-Ethical-Concerns-5.5)

1. When you create a GitHub repository it requests a license type. Review the license types in relationship to this Tech Talk and make some notes in GitHub pages.
* [GNU General Public License V3](https://www.youtube.com/watch?v=sQIVclmxvdQ)
  * Information
    * Anything you release must be open source.
    * You are allowed to sell your product, but there is no piracy protection (because the code is open source).
    * If anybody uses your code, their product automatically inherits the GNU General Public License V3.
  * Target
    * If your want to develop an open source project, this is the license for you. It garentees that nobody in the future will be able to close source the project.
    * If a company wants to make money, this is not the right license to use. A company should also avoid using any code that is under the GNU General Public License V3.

2. Make a license for your personal and Team project. Document license you picked and why.
* We chose the GNU General Public License V3 because we don't plan to generate revenue off of the project we build. We acknowledge that our skills are still improving, and that the things we create are not ready for commercial use. Therefore, if anybody wishes to build off of our code, they may be allowed to do so. By using this license, we are also avoiding potential plagiarism where somebody tries to make a profit off our code without our knowledge.

### 5.6 Notes

Daily Video 1:
* Personally Identifiable Information (PII) - Information specific to an individual
  * Basically, personal information. Cell phone number, email address, age, search history, location...
  * Can be used for good: Autofill, convenience sake, recommended based on your interests...
  * Can be used for bad: If privacy is breached, all of a sudden a bunch of sensitive information is now out in the open.
* Information placed online is difficult to get rid of :( ← Digital Footprint

Daily Video 2:
* Authentication (Passwords)
* Multi-Factor Authentication (Fingerprint, Physical Card, Link to Phone or Email)
* Virus - Duplicate themselves across systems.
* Malware - Infiltrate a system through impersonation (email, 'friendly' website), damaging the system after getting in.
* Encryption and Decryption
  * Caesar Cipher
  * [Rumkin Tools](http://rumkin.com/tools/cipher/) ← This website is really cool, holding tons of different ways to encrypt and decrypt a message. Try it!
* Asymmetric Encryption - Public and Private key
  * Public key used to encrypt a message
  * Private key used to decrypt a message
* Digital Certificates - Those public and private keys, but verified :D

Daily Video 3:
* Phishing - Trick the user into providing personal information, usually an email or 'friendly' website.
* Keylogger - Records user keystrokes in order to gain passwords or other confidential information.
* Rogue Access Point - Intercepting data across a network.

### [Tri 3 TPT 2.0 Safe Computing 5.6](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3-TPT-2.0-Safe-Computing-5.6)

1. Describe PII you have seen on project in CompSci Principles.
* About Page, voluntary PII.

2. What are your feelings about PII and your exposure?
* If I'm willingly giving out PII, I'm okay with it.
* If a company is collecting PII with the correct handling of information, privacy, and security, AND tells me about it, I'm okay with it.
* If a company is secretly building a profile of me without me knowing... I guess I wouldn't know about it, would I?

3. Describe good and bad passwords? What is another step that is used to assist in authentication.
* Good password: Tg^3x&bHFo8#z
* Bad password: user1234
* Multi-Factor authentication adds layers of security in addition to passwords. It's possible an intruder may know one thing about you, but the more authentication methods added the greater the chance that someone bypassing each one is the actual person.

4. Try to describe Symmetric and Asymmetric encryption.
* Smoothie analogy
  * Public key is banana.
  * Your private key is strawberry.
  * Friend's private key is blueberry.
  * You send over strawberry + banana.
  * Friend sends over blueberry + banana.
  * Interceptor receives ? + banana and ? + banana.
  * You add strawberry to the blueberry + banana, resulting in strawberry + blueberry + banana.
  * Friend adds blueberry to the strawberry + banana, resulting in strawberry + blueberry + banana.
* In the end, both you and your friend received the same message while the Interceptor received an encrypted mess.

5. Provide and example of encryption we used in deployment.
* Certbot.

6. Describe a phishing scheme you have learned about the hard way. Describe some other phishing techniques.
* clubpengun.com
  * Your Club Penguin account is not verified. Please enter your login information in order to regain access to your account.
* Other phishing techniques include suspicious emails, false bank account pages, or suspicious texts.

### [Tri 3 TT2 Python Classes](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3-TT2-Python-Classes)

Python Class - the call method
```python
def __call__(self):
    # It's like the main(String[] args) method in java!
    # Run it just by calling the Object!
    # No dot operator needed to run the code.
```

Challenges
1. Organize files, directories and menus for the first 3 weeks. Use Teacher implementation as an example. Make sure that work is organized so it is easy to illustrate this weeks assignments.
2. Write Factorial function using classes, providing implementation of call.
   * Print final number
   * Print sequence
3. Select your own Math function. Write it in Imperative and OOP form. Some Math functions have been provided. Think about inputs and outputs to present to Teacher. It is preferred to have Test data, not input to illustrate code.
4. Write Palindrome function using classes, providing implementation of call.
   * Evaluate if it is a palindrome
   * Evaluate complex algorithms eliminating spaces, case and special characters. "A man, a plan, a canal -- Panama!"
   * Use Test data, not input
   * Illustrate failure

### Challenge 1: Reorganize
main_pattern.py
```python
from src_py.util.menu import Menu
from src_py.pattern_menus.animations import Animations
from src_py.pattern_menus.data_structures import DataStructures
from src_py.pattern_menus.math_algorithms import MathAlgorithms


class MainPattern:
    def __init__(self):
        super().__init__()
        self.name = "Main Menu P"

        one = Animations()
        two = DataStructures()
        three = MathAlgorithms()
        self.options = [one, two, three]

    def main(self):
        m = Menu("----- MAIN MENU P -----", self.options)
        m.menu()
```

### Challenge 2: Factorial
factorial.py
```python
from src_py.util.option import Option


class Factorial(Option):
    def __init__(self):
        super().__init__()
        self.name = "Factorial"

    def __call__(self):
        number = int(input("Input a number to get a factorial from: "))
        f_obj = FactorialClass(number)
        f_obj.factorial()


class FactorialClass:
    def __init__(self, n):
        self.n = n

    def factorial(self):
        factorial = 1
        number = self.n
        while number > 0:
            factorial *= number
            number -= 1

        print(str(self.n) + "! is " + str(factorial))
```

### Challenge 4: Palindrome
palindrome.py
```python
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
```

### Challenge 3: Custom Math Function
tri_angle.py
```python
from src_py.util.option import Option
import math


class TriAngle(Option):
    def __init__(self):
        super().__init__()
        self.name = "Tri Angle"

    def __call__(self):
        print("\nParticle starts at (0, 0) and goes to (5, 5):")
        a = Angles(0, 0, 5, 5)
        a.print_coordinates()

        print("\nParticle starts at (0, 0) and goes to (-3, -3):")
        b = Angles(0, 0, -3, -3)
        b.print_coordinates()

        print("\nParticle starts at (5.5, 8) and goes to (-6.23, 11.1):")
        c = Angles(5.5, 8, -6.23, 11.1)
        c.print_coordinates()


class Angles:
    def __init__(self, x, y, tx, ty):
        self.x = x
        self.y = y
        angle = math.atan2(ty - y, tx - x)
        self.tx = math.cos(angle)
        self.ty = math.sin(angle)

    def print_coordinates(self):
        print("X Rotation: " + str(self.tx))
        print("Y Rotation: " + str(self.ty))
```
