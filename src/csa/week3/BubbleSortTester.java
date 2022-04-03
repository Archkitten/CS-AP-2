package csa.week3;
import csa.util.Option;
import csa.util.BubbleSort;
import csa.util.TestDataGenerator;

import java.util.Arrays;

public class BubbleSortTester extends Option {

    public BubbleSortTester() {
        optionName = "Bubble Sort";
    }

    public void tester() {
        TestDataGenerator testDataGenerator = new TestDataGenerator(5000);
        BubbleSort bubbleArray = new BubbleSort();
        for (int i = 0; i < 12; i++) {
            int[] testArray = testDataGenerator.getTestData();
            System.out.println("Initial Array: " + Arrays.toString(testArray));
            bubbleArray.sort(testArray);
            System.out.println("Sorted Array: " + Arrays.toString(testArray));
            System.out.println();
        }
    }
}
