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
                System.out.println("Please input an integer from 0 to " + options_array.length + ": ");
                userInput = getValidInput(scanObj);
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
    private int getValidInput(Scanner scanObj) {
        try {
            return Integer.parseInt(scanObj.nextLine());
        }
        catch(Exception e) {
            return -1;
        }
    }
}
