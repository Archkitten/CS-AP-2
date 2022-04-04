package csa.week3;
import csa.util.Menu;
import csa.util.Option;

public class WeekThreeA extends Option {

    public WeekThreeA() {
        optionName = "Week 3 - Objective 1 (Array)";
    }

    public void tester() {
        Option one = new BubbleSortTester();
        Option two = new SelectionSortTester();
        Option three = new InsertionSortTester();
        Option four = new MergeSortTester();

        Option[] options = new Option[] {one, two, three, four};

        Menu menu = new Menu();
        menu.run("\n----- WEEK 3 OBJECTIVE 1 -----", options);
    }
}
