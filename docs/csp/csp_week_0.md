{% include navigation.html %}

# CSP

{% include csp_nav.html %}

## Week 0 - [Ticket](https://github.com/Archkitten/CS-AP-2/issues/1)

### 5.1 Notes

* Drones were made that helps video surveillance through air, helps people by finding lost people, although privacy concerns and illegal flying are negatives of the invention.
* 3D Printers were invented that allows for easy access to many tools, home-printed.

### [Tri 3 TPT 0.1 related to Beneficial and Harmful Effects of Computing Big Idea 5.1](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3-TPT-0.1-related-to-Beneficial-and-Harmful-Effects-of-Computing-Big-Idea-5.1)

1. Come up with three of your own Beneficial and corresponding Harmful Effects of Computing
* Technology allows anyone to share information with anyone, allowing easy access of data. This also means that there is a lot of misinformation or fake information out there.
* Predicting natural disasters is easier.
* GPS allows us to go anywhere and take the fastest route without needing to look up directions ahead of time. Unfortunately, GPS malfunctions or lack of GPS may cause people that were previously dependent on GPS to get lost.

2. Talk about dopamine issues above. Real? Parent conspiracy? Anything that is impacting your personal study and success in High School?
* I've seen dopamine issues effect many people around my age, including myself. Social platforms are sources of dopamine, granting instant gratification through posts, videos, memes, and discussion topics. However, viewing these too often will give an overload of dopamine, causing the brain to create more dopamine receptors (neurons that process dopamine). As a result, doing anything else besides spending time on social platforms will grant a lower proportion of dopamine compared to the new receptors created, causing levels of happiness to be lower than normal.

### 5.2 Notes

* Some people may not have access to technology at all, some people have technology but they don’t know how to use it or how it works. This is the digital divide, and it is best to reduce this as much as possible.
* Digital Divide is increasing because a growing number of wealthy people are getting access to technology and other poorer people do not have ready access to technology when needed.

### [Tri 3 TPT 0.2 related to Digital Divide Big Idea 5.2](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3-TPT-0.2-related-to-Digital-Divide-Big-Idea-5.2)

1. How does someone empower themselves in a digital world?
* Empowerment in a digital world is as simple as having free, easy access to technology.

2. How does someone that is empowered help someone that is not empowered? Describe something you could do at Del Norte HS.
* Providing financial help could allow someone to afford technology of their own. A way to help a bunch of people like students at Del Norte is doing something like creating a public computer lab where anyone can use the computers, or having a bunch of cheap computers available for checkout to students that need it.

3. Is paper or red tape blocking digital empowerment? Are there such barriers at Del Norte? Elsewhere?
* Red Tape somewhat blocks digital empowerment by eliminating the 'freedom' aspect of technology. However, I do get that it keeps students safe by preventing off-topic searches and account break-ins that breach privacy.

### [Tri 3 TT0 Python Menu, Replit, Github](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3---TT0---Python-Menu,-Replit,-Github)

Link to code + runtime: [CS-AP-P Python Replit](https://replit.com/@ArchHuang/CS-AP-P?lite=true)

### Create Task Plan

<table>
    <tr>
        <th>Project Name</th>
        <th>Link</th>
        <th>Description</th>
        <th>Date</th>
    </tr>
    <tr>
        <td>Create Task</td>
        <td><a href="https://www.google.com/">N/A</a></td>
        <td>
            [Project Name] contains user input through mouse clicks and keyboard inputs.
            A list will also be used to store objects that can be displayed on the screen.
            This project will use Object-Oriented Programming, with each object containing functions that allow it to preform tasks like updating position or changing variables based on user input.
            An algorithm will be used to remove objects that aren't needed anymore, as well as iterate through the list in order to display each object on the screen.
        </td>
        <td>TBD</td>
    </tr>
</table>

### Challenge #1: Number Swap
number_swap.py
```
from src_py.util.option import Option


class NumberSwap(Option):
    def __init__(self):
        super().__init__()
        self.name = "Number Swap"

    def tester(self):
        print(self.swap(1, 2))
        print(self.swap(60, 30))
        print(self.swap(9, -11))

    def swap(self, a, b):
        if a > b:
            temp = a
            a = b
            b = temp
        return a, b
```

### Challenge #2: Matrix Format
matrix_format.py
```
from src_py.util.option import Option


class MatrixFormat(Option):
    def __init__(self):
        super().__init__()
        self.name = "Matrix Format"
        self.numpad = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [" ", 0, " "]]

    def tester(self):
        for i in self.numpad:
            for j in i:
                print(j, "", end="")
            print()
```

### Challenge #3: Christmas Tree
build_stairs.py
```
from src_py.util.option import Option


class BuildStairs(Option):
    def __init__(self):
        super().__init__()
        self.name = "Build Stairs"
        self.space = ""

    def tester(self):
        counter = 0
        steps = int(input("How many steps? "))

        while counter < steps:
            self.stairs()
            counter += 1
        self.space = ""

    def stairs(self):
        print(self.space + "|__")
        self.space = self.space + " - "
```

### Challenge #4: Ship Animation
cat_laptop.py
```
import time
from src_py.util.option import Option
# from ..util.option import Option


ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"


class CatLaptop(Option):
    def __init__(self):
        super().__init__()
        self.name = "Cat Laptop"

    def tester(self):
        self.ship()

    def ocean_print(self):
        # print ocean
        # print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)

        print("\n"*4)
        print(OCEAN_COLOR + "  " * 35)

    # print ship with colors and leading spaces
    def ship_print(self, position):
        print(ANSI_HOME_CURSOR)
        print(RESET_COLOR)
        sp = " " * position
        print(sp + "/|")
        print(sp + "||")
        print(sp + "\\|  ᓚᘏᗢ  ")
        print(SHIP_COLOR, end="")
        print(sp + "  \\______/  ")
        print(RESET_COLOR)

    # ship function, iterate into this file
    def ship(self):
        # only need to print ocean once
        self.ocean_print()

        # loop control variables
        start = 0  # start at zero
        distance = 60  # how many times to repeat
        step = 2  # count by 2

        # loop purpose is to animate ship sailing
        for position in range(start, distance, step):
            self.ship_print(position)  # call to function with parameter
            time.sleep(.1)
```
