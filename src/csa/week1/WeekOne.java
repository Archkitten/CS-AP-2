package csa.week1;
import csa.util.Menu;
import csa.util.Option;

public class WeekOne extends Option {

    public WeekOne() {
        optionName = "Week 1";
    }

    public void tester() {
        Option one = new ChallengeOne();
        Option two = new ChallengeTwo();

        Option[] options = new Option[] {one, two};

        Menu menu = new Menu();
        menu.run("\n----- WEEK 1 -----", options);
    }
}
