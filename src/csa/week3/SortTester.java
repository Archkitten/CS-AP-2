package csa.week3;

import csa.util.ITemplateSort;
import csa.util.TestDataGenerator;

import java.time.Duration;
import java.time.Instant;
import java.util.Arrays;

public class SortTester {
    public void tester(ITemplateSort genericSort) {
        TestDataGenerator testDataGenerator = new TestDataGenerator(5000);
        int minimum = 0;
        int maximum = 0;
        int totalTime = 0;

        for (int i = 0; i < 12; i++) {
            int[] testArray = testDataGenerator.getTestData();
            System.out.println("Initial Array: " + Arrays.toString(testArray));

            Instant start = Instant.now();  // time capture -- start
            genericSort.sort(testArray);
            Instant end = Instant.now();    // time capture -- end
            Duration timeElapsed = Duration.between(start, end);

            minimum = Math.min(minimum, timeElapsed.getNano());
            maximum = Math.max(timeElapsed.getNano(), maximum);
            totalTime += timeElapsed.getNano();

            System.out.println("Sorted Array: " + Arrays.toString(testArray));
            System.out.println("Time: " + timeElapsed);
            System.out.println();
        }
        int averageTime = (totalTime - minimum - maximum) / 10;
        double averageTimeInSeconds = averageTime / 1_000_000_000.0;
        System.out.println("Average Time (in seconds): " + averageTimeInSeconds);
    }
}
