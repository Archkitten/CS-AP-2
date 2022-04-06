---
layout: default
---

# CSP

{% include csp_nav.html %}

## Final - [Ticket](https://github.com/Archkitten/CS-AP-2/issues/11)

### Video

<iframe src="https://www.youtube.com/embed/sQAuUaaWoz8?autoplay=1&mute=1" width="800px" height="450px"></iframe>

### Coding Review

* Key Learnings and Challenges found in previous week's pages.
* [GitHub Commits](https://github.com/Archkitten/CS-AP-2/commits?author=Archkitten)
  * [GitHub Contributor Graph](https://github.com/Archkitten/CS-AP-2/graphs/contributors)
* Replit Runtime found on [CSP Main Page](https://archkitten.github.io/CS-AP-2/csp).
* ACTION - Demonstrate IntelliJ Runtime.
* Menu review illustrating use of Lists and navigation:
  * [menu.py](https://github.com/Archkitten/CS-AP-2/blob/master/src_py/util/menu.py)
  * [option.py](https://github.com/Archkitten/CS-AP-2/blob/master/src_py/util/option.py)
  * [main.py](https://github.com/Archkitten/CS-AP-2/blob/master/src_py/main.py) (menu)
    * [week_0.py](https://github.com/Archkitten/CS-AP-2/blob/master/src_py/week0/week_0.py) (submenu - Both a menu and an option)
      * [build_stairs.py](https://github.com/Archkitten/CS-AP-2/blob/master/src_py/week0/build_stairs.py) (option)
* List and Loops:
  * [info_loops.py](https://github.com/Archkitten/CS-AP-2/blob/master/src_py/week1/info_loops.py)
* Class review and understanding:
  * [main_pattern.py](https://github.com/Archkitten/CS-AP-2/blob/master/src_py/pattern_menus/main_pattern.py)
    * [animations.py](https://github.com/Archkitten/CS-AP-2/blob/master/src_py/pattern_menus/animations.py)
      * Matrix Format
      * Build Stairs (Christmas Tree)
      * Cat Laptop (Ship Animation)
    * [math_algorithms.py](https://github.com/Archkitten/CS-AP-2/blob/master/src_py/pattern_menus/math_algorithms.py)
      * Number Swap
      * Fibonacci
      * Factorial
      * Tri Angle (Custom Math Class)
      * Multiplication Table (Special Challenge)
    * [data_structures.py](https://github.com/Archkitten/CS-AP-2/blob/master/src_py/pattern_menus/data_structures.py)
      * Info Loops
      * Palindrome
  * Code with good comments:
    * [palindrome.py](https://github.com/Archkitten/CS-AP-2/blob/master/src_py/week2/palindrome.py)
    * [multiplication_table.py](https://github.com/Archkitten/CS-AP-2/blob/master/src_py/week2/multiplication_table.py)
* Anything else that enhances learning from Python?

### Crossover Contribution

Main branch and replit code: [Commits](https://github.com/Archkitten/sleep/commits/main)
* requirements.txt allows new contributors to automatically have the required packages, instead of needing to search through the code and manually install it themselves.
  * The repository was lacking this file, and I had to manually install each dependancy. In order to prevent this for future contributors, I created a requirements.txt file.
* An issue I noticed was that after running "TPT1 - InfoDB", the program would end. I got rid of the exit() statement that caused the issue.
* An unexplained error message 'TERM environment variable not set' appeared only during IntelliJ runtime due to trying to clear the terminal. I never got to fix the issue, but I did find the source of the error at least.

GitHub Pages branch: [Commits](https://github.com/Archkitten/sleep/commits/gh-pages)
* I imported scss and default.html in order to allow customization of the GitHub theme.
* This allowed me to:
  * Change the background of the header
  * Change text color
  * and customize the header, including adding a navbar
