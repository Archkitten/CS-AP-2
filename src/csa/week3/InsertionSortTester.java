package csa.week3;
import csa.util.*;

public class InsertionSortTester extends Option {

    public InsertionSortTester() {
        optionName = "Insertion Sort";
    }

    public void tester() {
        ITemplateSort genericSort = new InsertionSort();

        SortTester sortTester = new SortTester();
        sortTester.tester(genericSort);
    }
}
