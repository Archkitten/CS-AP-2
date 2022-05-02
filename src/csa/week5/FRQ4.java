package csa.week5;
import csa.util.Option;

public class FRQ4 extends Option {
    public FRQ4() {
        optionName = "FRQ4";
    }

    public void tester() {
        NumberGroup range1 = new Range(-3, 2);

        // Delete this later, used for checking
        for (int i : ((Range)range1).getRange()) {
            System.out.println(i);
        }
    }
}
