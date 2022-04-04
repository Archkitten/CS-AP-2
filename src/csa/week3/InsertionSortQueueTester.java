package csa.week3;

import csa.util.ITemplateSort;
import csa.util.InsertionSort;
import csa.util.Option;

public class InsertionSortQueueTester extends Option {

    public InsertionSortQueueTester() {
        optionName = "Insertion Sort Queue";
    }

    public void tester() {
        ITemplateSort genericSort = new InsertionSort();

        SortTester sortTester = new SortTester();
        sortTester.queueTester(genericSort);
    }
}
