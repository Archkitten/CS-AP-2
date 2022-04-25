package csa.week5;
import csa.util.Option;
import java.util.Scanner;

public class FRQ2 extends Option {

    public FRQ2() {
        optionName = "FRQ2";
    }

    public void tester() {
        HiddenWord test = new HiddenWord("APPLE");
        System.out.println("APPLE");
        System.out.println("Guessing: AUDIO");
        System.out.println(test.getHint("AUDIO"));
    }
}
