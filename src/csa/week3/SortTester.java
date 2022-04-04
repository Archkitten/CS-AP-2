package csa.week3;

import csa.util.ITemplateSort;
import csa.util.Queue;
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

    public void queueTester(ITemplateSort genericSort) {
        TestDataGenerator testDataGenerator = new TestDataGenerator(5000);
        int minimum = 0;
        int maximum = 0;
        int totalTime = 0;

        for (int i = 0; i < 12; i++) {
            Queue<Integer> testQueue = testDataGenerator.createQueueTestData();
            System.out.print("Initial Queue ");
            printQueue(testQueue);

            Instant start = Instant.now();  // time capture -- start
            genericSort.sort(testQueue);
            Instant end = Instant.now();    // time capture -- end
            Duration timeElapsed = Duration.between(start, end);

            minimum = Math.min(minimum, timeElapsed.getNano());
            maximum = Math.max(timeElapsed.getNano(), maximum);
            totalTime += timeElapsed.getNano();

            System.out.print("Sorted Queue ");
            printQueue(testQueue);

            System.out.println("Time: " + timeElapsed);
            System.out.println();
        }
        int averageTime = (totalTime - minimum - maximum) / 10;
        double averageTimeInSeconds = averageTime / 1_000_000_000.0;
        System.out.println("Average Time (in seconds): " + averageTimeInSeconds);
    }

    private void printQueue(Queue<Integer> queue) {
        System.out.print("data: ");
        for (Integer data : queue) {
            System.out.print(data + " ");
        }
        if (queue.getHead() == null) {
            System.out.print("null");
        }
        System.out.println();
    }
}
