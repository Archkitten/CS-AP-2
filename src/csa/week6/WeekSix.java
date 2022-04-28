package csa.week6;
import csa.util.Menu;
import csa.util.Option;

public class WeekSix extends Option {

    public WeekSix() {
        optionName = "Week 6";
    }

    public void tester() {
        Option one = new FRQ1();
        Option two = new FRQ2();
        Option three = new FRQ3();
        Option four = new FRQ4();

        Option[] options = new Option[] {one, two, three, four};

        Menu menu = new Menu();
        menu.run("\n----- WEEK 6 -----", options);
    }
}
