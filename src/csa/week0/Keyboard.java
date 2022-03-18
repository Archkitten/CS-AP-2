package csa.week0;
import csa.util.Option;

public class Keyboard extends Option {

    public Keyboard() {
        optionName = "Keyboard";
    }

    public void tester() {
        char[][] keyboard_array = new char[][] {{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}, {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}, {'z', 'x', 'c', 'v', 'b', 'n', 'm'}};
        for (char[] i : keyboard_array) {
            for (char j : i) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }

}
