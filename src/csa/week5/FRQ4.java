package csa.week5;
import csa.util.Option;

public class FRQ4 extends Option {
    public FRQ4() {
        optionName = "FRQ4";
    }

    public void tester() {
        NumberGroup range1 = new Range(-3, 2);
        range1.contains(-5);
        range1.contains(0);
        range1.contains(4);
    }
}
