package com;

import java.util.Scanner;

public class Main {

    private static boolean running = true;

    public static void main(String[] args) {
        Option numberSwap = new NumberSwap();
        Option matrixToText = new MatrixToText();
        Option bestSongHackathon = new BestSongHackathon();

        Option[] option_array_editable = new Option[] {numberSwap, matrixToText, bestSongHackathon};
        while (running) {
            menu("Choose an option!", option_array_editable);
        }
    }

    public static void menu(String banner, Option[] options_array) {
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

        String userInput = scanObj.nextLine();
        int selection = 0;
        try {
            selection = Integer.parseInt(userInput);
        }
        catch (NumberFormatException e) {
            e.printStackTrace();
        }
        // Checks if user input matches a menu option.
        for (int o = 0; o < options_array.length; o++) {
            if (selection == 0) {
                running = false;
            }
            else if (selection == o + 1) {
                options_array[o].process(scanObj);
                options_array[o].tester();
            }
        }
    }
}
