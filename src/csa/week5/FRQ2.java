package csa.week5;
import csa.util.Option;
import java.util.Scanner;

public class FRQ2 extends Option {

    public FRQ2() {
        optionName = "FRQ2";
    }

    public void tester() {
        System.out.println("Answer: TRASH");
        HiddenWord hw = new HiddenWord("TRASH");
        System.out.println("Guess: AUDIO");
        System.out.println(hw.getHint("AUDIO"));
        System.out.println("Guess: TRACK");
        System.out.println(hw.getHint("TRACK"));
        System.out.println("Guess: TRAPS");
        System.out.println(hw.getHint("TRAPS"));
        System.out.println("Guess: TRASH");
        System.out.println(hw.getHint("TRASH"));
    }
}
