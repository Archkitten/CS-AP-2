package csa.week6;
import csa.util.Menu;
import csa.util.Option;

public class WeekSix extends Option {

    public WeekSix() {
        optionName = "Week 5";
    }

    public void tester() {
        Option one = new FRQ1();
        Option two = new FRQ2();

        Option[] options = new Option[] {one, two};

        Menu menu = new Menu();
        menu.run("\n----- WEEK 6 -----", options);
    }
}
