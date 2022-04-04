package csa.week3;
import csa.util.Menu;
import csa.util.Option;

public class WeekThree extends Option {

    public WeekThree() {
        optionName = "Week 3";
    }

    public void tester() {
        Option one = new WeekThreeA();
        Option two = new WeekThreeB();

        Option[] options = new Option[] {one, two};

        Menu menu = new Menu();
        menu.run("\n----- WEEK 3 -----", options);
    }
}
