import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Option numberSwap = new NumberSwap();
        Option matrixToText = new MatrixToText();
        Option[] option_array_editable = new Option[] {numberSwap, matrixToText};
        menu("Hey!", option_array_editable);
    }

    public static void menu(String banner, Option[] options_array) {
        Scanner scanObj = new Scanner(System.in);
        // Prints the banner message.
        System.out.println(banner);
        // Iterator, prints out options of the menu.
        int i = 1;
        for (Option o : options_array) {
            System.out.print(i + " - ");
            i++;
            System.out.println(o.getOptionName());
        }

        String userInput = scanObj.nextLine();
        // Checks if user input matches a menu option.
        for (Option o : options_array) {
            if (userInput.equals(o.getOptionName())) {
                o.process(scanObj);
            }
        }

        /*
        try {
            int selection = Integer.parseInt(userInput);
        }
        catch (NumberFormatException e) {
            e.printStackTrace();
        }
        */
    }
}
