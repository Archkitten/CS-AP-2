package csa.week3;
import csa.util.ITemplateSort;
import csa.util.MergeSort;
import csa.util.Option;

public class MergeSortTester extends Option {

    public MergeSortTester() {
        optionName = "Merge Sort";
    }

    public void tester() {
        ITemplateSort genericSort = new MergeSort();

        SortTester sortTester = new SortTester();
        sortTester.tester(genericSort);
    }
}
