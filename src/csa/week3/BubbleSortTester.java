package csa.week3;
import csa.util.ITemplateSort;
import csa.util.Option;
import csa.util.BubbleSort;

public class BubbleSortTester extends Option {

    public BubbleSortTester() {
        optionName = "Bubble Sort";
    }

    public void tester() {
        ITemplateSort genericSort = new BubbleSort();

        SortTester sortTester = new SortTester();
        sortTester.tester(genericSort);
    }
}
