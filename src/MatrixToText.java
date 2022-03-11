import java.util.Scanner;

public class MatrixToText extends Option {

    public MatrixToText() {
        optionName = "MatrixToText";
    }

    public String getOptionName() {
        return optionName;
    }

    private void numpad() {
        int[][] numpad_array = new int[][] {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        for (int[] i : numpad_array) {
            for (int j : i) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }

    private void keyboard() {
        char[][] keyboard_array = new char[][] {{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
                {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
                {'z', 'x', 'c', 'v', 'b', 'n', 'm'}};
        for (char[] i : keyboard_array) {
            for (char j : i) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }


    public void process(Scanner scanObj) {
        // super.process() will just run the process() method from Option.java
        super.process(scanObj);
        // Ask user to run numpad or keyboard in the future
        System.out.println("Numpad or Keyboard?");
        System.out.println("1 - Numpad");
        System.out.println("2 - Keyboard");

        String userInput = scanObj.nextLine();

        MatrixToText testObj = new MatrixToText();
        if (userInput.equals("1")) {
            testObj.numpad();
        }
        else if (userInput.equals("2")) {
            testObj.keyboard();
        }
        else {
            System.out.println("Invalid Input: Selection out of range");
        }
    }
}
