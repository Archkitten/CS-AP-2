package csa.week3;

import csa.util.ITemplateSort;
import csa.util.MergeSort;
import csa.util.Option;

public class MergeSortQueueTester extends Option {

    public MergeSortQueueTester() {
        optionName = "Merge Sort Queue";
    }

    public void tester() {
        ITemplateSort genericSort = new MergeSort();

        SortTester sortTester = new SortTester();
        sortTester.queueTester(genericSort);
    }
}
