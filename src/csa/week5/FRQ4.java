package csa.week5;
import csa.util.Option;

public class FRQ4 extends Option {
    public FRQ4() {
        optionName = "FRQ4";
    }

    public void tester() {
        System.out.println("NumberGroup range1 = new Range(-3, 2);");
        NumberGroup range1 = new Range(-3, 2);
        System.out.println("range1.contains(-5);");
        System.out.println(range1.contains(-5));
        System.out.println("range1.contains(0);");
        System.out.println(range1.contains(0));
        System.out.println("range1.contains(4);");
        System.out.println(range1.contains(4));
    }
}
