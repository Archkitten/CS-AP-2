package csa.week3;

import csa.util.ITemplateSort;
import csa.util.SelectionSort;
import csa.util.Option;

public class SelectionSortQueueTester extends Option {

    public SelectionSortQueueTester() {
        optionName = "Selection Sort Queue";
    }

    public void tester() {
        ITemplateSort genericSort = new SelectionSort();

        SortTester sortTester = new SortTester();
        sortTester.queueTester(genericSort);
    }

    public static void main(String[] args){
        new SelectionSortQueueTester().tester();
    }
}
