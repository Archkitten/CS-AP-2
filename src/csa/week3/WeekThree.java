package csa.week3;
import csa.util.Menu;
import csa.util.Option;

public class WeekThree extends Option {

    public WeekThree() {
        optionName = "Week 3";
    }

    public void tester() {
        Option one = new BubbleSort();
        Option two = new SelectionSort();
        Option three = new InsertionSort();
        Option four = new MergeSort();

        Option[] options = new Option[] {one, two, three, four};

        Menu menu = new Menu();
        menu.run("\n----- WEEK 3 -----", options);
    }
}
