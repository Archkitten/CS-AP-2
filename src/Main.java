import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        menu("Hey!", new String[] {"1", "2", "3"});
    }

    public static void menu(String banner, String[] options_array) {
        Scanner scanObj = new Scanner(System.in);

        System.out.println(banner);
        for (String s : options_array) {
            System.out.println(s);
        }

        String userInput = scanObj.nextLine();

        try {
            int selection = Integer.parseInt(userInput);
        }
        catch (NumberFormatException e) {
            e.printStackTrace();
        }
    }
}
