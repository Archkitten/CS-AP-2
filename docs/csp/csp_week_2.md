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
* Response

2. Make a license for your personal and Team project. Document license you picked and why.
* Response

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
* Digital Certificates - Those public and private keys, but verified :D

Daily Video 3:
* Phishing - Trick the user into providing personal information, usually an email or 'friendly' website.
* Keylogger - Records user keystrokes in order to gain passwords or other confidential information.
* Rogue Access Point - Intercepting data across a network.

### [Tri 3 TPT 2.0 Safe Computing 5.6](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3-TPT-2.0-Safe-Computing-5.6)

1. Describe PII you have seen on project in CompSci Principles.
* Response

2. What are your feelings about PII and your exposure?
* Response

3. Describe good and bad passwords? What is another step that is used to assist in authentication.
* Response

4. Try to describe Symmetric and Asymmetric encryption.
* Response

5. Provide and example of encryption we used in deployment.
* Response

6. Describe a phishing scheme you have learned about the hard way. Describe some other phishing techniques.
* Response

### [Tri 3 TT2 Python Classes](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3-TT2-Python-Classes)

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

### Challenge 1: Factorial
factorial.py
```
from src_py.util.option import Option


class Factorial(Option):
    def __init__(self):
        super().__init__()
        self.name = "Factorial"

    def tester(self):
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

### Challenge 2: Palindrome
palindrome.py
```
# Need Test Cases before publishing code
```

### Challenge 3: Custom Math Function
tri_angle.py
```
# Need Test Cases before publishing code
```
