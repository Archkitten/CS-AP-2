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
            int i = 0;
            System.out.println("99 - Exit");
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
            } while ((userInput < 0 || userInput > options_array.length) && userInput != 99);

            // Checks if user input matches a menu option.
            for (int o = 0; o < options_array.length; o++) {
                if (userInput == 99) {
                    running = false;
                }
                else if (userInput == o) {
                    options_array[o].tester();
                }
            }
        }
    }

    // Error Handling
    private int getValidInput(Scanner scanObj, int arrayLength) {
        try {
            int userInput = Integer.parseInt(scanObj.nextLine());
            if ((userInput <= -1 || userInput > arrayLength - 1) && userInput != 99) {
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
