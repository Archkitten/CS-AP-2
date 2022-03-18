package csa.week0;
import csa.util.Menu;
import csa.util.Option;

public class WeekZero extends Option {

    public WeekZero() {
        optionName = "Week 0";
    }

    public void tester() {
        Option one = new NumberSwap();
        Option two = new MatrixFormat();

        Option[] options = new Option[] {one, two};

        Menu menu = new Menu();
        menu.run("\n----- WEEK 0 -----", options);
    }
}
