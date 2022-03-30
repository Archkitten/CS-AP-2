# CSA

{% include csa_nav.html %}

## Week 0 - [Ticket](https://github.com/Archkitten/CS-AP-2/issues/2)

### (TPT) Study Group Challenges

Assignment:
* Java Menu that is not hard coded (Use object array?)
* Number Swap option that sorts two numbers from least to greatest
* Matrix Format option that prints a numpad and keyboard

Test Prep Plans for success:
* Array Data structure needs different classes to run, but Arrays can only have one data type.
* Therefore, Inheritance and Late Binding is needed to store different object types into the same Array.

AP Exam Plans for success:
* Pair Review unfamiliar topics
* Do more MCQ problems
* Review Tri 2 FRQs, maybe rework some or improve upon them

Final Result:
* Link to code + runtime: [CS-AP-2 Java Replit](https://replit.com/@ArchHuang/CS-AP-A?lite=true)
* Ticket: [Ticket](https://github.com/Archkitten/m221-nitro-code/issues/1)

### [Tri 3: Tech Talk 0 Data Structures](https://github.com/nighthawkcoders/nighthawk_csa/wiki/Tri-3:-Tech-Talk-0---Data-Structures)

* Imperative Paradigm: Procedural Programming like Python
* Object-Oriented Programming: Java, uses Objects and Classes, Inheritance, Abstraction, and Polymorphism
* Big Tech Companies Stock: Google, Microsoft, Apple, Amazon
* Assignment: Make a menu based off of a data structure, Challenge 1 and Challenge 2 and Matrix

### Challenge #0: Menu Try Catch
Option.java
```
package csa.util;

public abstract class Option {

    protected String optionName = "Option";

    public String getOptionName() {
        return optionName;
    }

    public void tester() {
        System.out.println("Test");
    }
}
```

Menu.java
```
package csa.util;

import java.util.Scanner;

public class Menu {

    public boolean running = true;

    public void run(String banner, Option[] options_array) {
        while (running) {
            Scanner scanObj = new Scanner(System.in);
            // Prints the banner message.
            System.out.println(banner);
            // Iterator, prints out options of the menu.
            int i = 1;
            System.out.println("0 - Exit");
            for (Option o : options_array) {
                System.out.print(i + " - ");
                i++;
                System.out.println(o.getOptionName());
            }

            // User Input
            int userInput;
            do {
                System.out.print(">");
                userInput = getValidInput(scanObj, options_array.length);
            } while (userInput < 0 || userInput > options_array.length);

            // Checks if user input matches a menu option.
            for (int o = 0; o < options_array.length; o++) {
                if (userInput == 0) {
                    running = false;
                }
                else if (userInput == o + 1) {
                    options_array[o].tester();
                }
            }
        }
    }

    // Error Handling
    private int getValidInput(Scanner scanObj, int arrayLength) {
        try {
            int userInput = Integer.parseInt(scanObj.nextLine());
            if (userInput <= -1 || userInput > arrayLength) {
                System.out.println("Out of Range");
            }
            return userInput;
        }
        catch(NumberFormatException e) {
            System.out.println("Wrong Format");
            return -1;
        }
        catch(Exception e) {
            System.out.println("Unknown Error");
            return -1;
        }
    }
}
```

### Challenge #1: Number Swap
NumberSwap.java
```
package csa.week0;
import csa.util.Option;

public class NumberSwap extends Option {

    public NumberSwap() {
        optionName = "Number Swap";
    }

    public void tester() {
        System.out.println(swap(1, 2));
        System.out.println(swap(60, 30));
        System.out.println(swap(9, -11));
    }

    private String swap(int a, int b) {
        if (a > b) {
            int temp = a;
            a = b;
            b = temp;
        }
        return (a + " " + b);
    }

}
```

### Challenge #2: Matrix Format
Numpad.java
```
package csa.week0;
import csa.util.Option;

public class Numpad extends Option {

    public Numpad() {
        optionName = "Numpad";
    }

    public void tester() {
        int[][] numpad_array = new int[][] CODE IMPLEMENTATION NOT SHOWN;
        for (int[] i : numpad_array) {
            for (int j : i) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }
}
```

Keyboard.java
```
package csa.week0;
import csa.util.Option;

public class Keyboard extends Option {

    public Keyboard() {
        optionName = "Keyboard";
    }

    public void tester() {
        char[][] keyboard_array = new char[][] CODE IMPLEMENTATION NOT SHOWN;
        for (char[] i : keyboard_array) {
            for (char j : i) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }
}
```
