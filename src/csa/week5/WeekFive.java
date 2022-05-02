package csa.week5;
import csa.util.Menu;
import csa.util.Option;

public class WeekFive extends Option {

    public WeekFive() {
        optionName = "Week 5";
    }

    public void tester() {
        Option one = new FRQ1();
        Option two = new FRQ2();
        Option four = new FRQ4();

        Option[] options = new Option[] {one, two, four};

        Menu menu = new Menu();
        menu.run("\n----- WEEK 5 -----", options);
    }
}
