package csa.week3;
import csa.util.*;

public class SelectionSortTester extends Option {

    public SelectionSortTester() {
        optionName = "Selection Sort";
    }

    public void tester() {
        ITemplateSort genericSort = new SelectionSort();

        SortTester sortTester = new SortTester();
        sortTester.tester(genericSort);
    }
}
