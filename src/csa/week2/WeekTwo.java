package csa.week2;
import csa.util.Menu;
import csa.util.Option;

public class WeekTwo extends Option {

    public WeekTwo() {
        optionName = "Week 2";
    }

    public void tester() {
        Option one = new CalculatorTester();

        Option[] options = new Option[] {one};

        Menu menu = new Menu();
        menu.run("\n----- WEEK 2 -----", options);
    }
}
