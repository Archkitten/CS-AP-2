import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Option numberSwap = new NumberSwap();
        Option matrixToText = new MatrixToText();
        menu("Hey!", new Option[] {numberSwap, matrixToText});
    }

    public static void menu(String banner, Option[] options_array) {
        Scanner scanObj = new Scanner(System.in);

        System.out.println(banner);
        for (Option o : options_array) {
            System.out.println(o.getOptionName());
        }

        String userInput = scanObj.nextLine();

        for (Option o : options_array) {
            if (userInput.equals(o.getOptionName())) {
                o.process();
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
