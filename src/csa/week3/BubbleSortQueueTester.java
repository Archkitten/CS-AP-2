package csa.week3;

import csa.util.ITemplateSort;
import csa.util.BubbleSort;
import csa.util.Option;

public class BubbleSortQueueTester extends Option {

    public BubbleSortQueueTester() {
        optionName = "Bubble Sort Queue";
    }

    public void tester() {
        ITemplateSort genericSort = new BubbleSort();

        SortTester sortTester = new SortTester();
        sortTester.queueTester(genericSort);
    }

    public static void main(String[] args){
        new BubbleSortQueueTester().tester();
    }
}
