package csa.week3;
import csa.util.Menu;
import csa.util.Option;

public class WeekThreeB extends Option {

    public WeekThreeB() {
        optionName = "Week 3 - Objective 2 (Queue)";
    }

    public void tester() {
        Option five = new BubbleSortQueueTester();
        Option six = new SelectionSortQueueTester();
        Option seven = new InsertionSortQueueTester();
        Option eight = new MergeSortQueueTester();

        Option[] options = new Option[] {five, six, seven, eight};

        Menu menu = new Menu();
        menu.run("\n----- WEEK 3 OBJECTIVE 2 -----", options);
    }
}
