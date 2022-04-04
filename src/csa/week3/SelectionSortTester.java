package csa.week3;
import csa.util.SelectionSort;
import csa.util.Option;
import csa.util.TestDataGenerator;

import java.time.Duration;
import java.time.Instant;
import java.util.Arrays;

public class SelectionSortTester extends Option {

    public SelectionSortTester() {
        optionName = "Selection Sort";
    }

    public void tester() {
        TestDataGenerator testDataGenerator = new TestDataGenerator(5000);
        SelectionSort selectionArray = new SelectionSort();
        for (int i = 0; i < 12; i++) {
            int[] testArray = testDataGenerator.getTestData();
            System.out.println("Initial Array: " + Arrays.toString(testArray));

            Instant start = Instant.now();  // time capture -- start
            selectionArray.sort(testArray);
            Instant end = Instant.now();    // time capture -- end
            Duration timeElapsed = Duration.between(start, end);

            System.out.println("Sorted Array: " + Arrays.toString(testArray));
            System.out.println("Time: " + timeElapsed);
            System.out.println();
        }
    }
}
