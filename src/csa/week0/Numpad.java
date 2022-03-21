package csa.week0;
import csa.util.Option;

public class Numpad extends Option {

    public Numpad() {
        optionName = "Numpad";
    }

    public void tester() {
        int[][] numpad_array = new int[][] {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {0, 0, 0}};
        for (int[] i : numpad_array) {
            for (int j : i) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }
}
