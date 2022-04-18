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
        int minTime, maxTime, totalTime;
        maxTime = totalTime = 0;
        minTime = Integer.MAX_VALUE;
        int minSwaps, maxSwaps, totalSwaps;
        maxSwaps = totalSwaps = 0;
        minSwaps = Integer.MAX_VALUE;
        int minComparisons, maxComparisons, totalComparisons;
        maxComparisons = totalComparisons = 0;
        minComparisons = Integer.MAX_VALUE;

        for (int i = 0; i < 12; i++) {
            int[] testArray = testDataGenerator.getTestData();
            System.out.println("Initial Array: " + Arrays.toString(testArray));

            Instant start = Instant.now();  // time capture -- start
            genericSort.sort(testArray);
            Instant end = Instant.now();    // time capture -- end

            Duration timeElapsed = Duration.between(start, end);

            minTime = Math.min(minTime, timeElapsed.getNano());
            maxTime = Math.max(timeElapsed.getNano(), maxTime);
            totalTime += timeElapsed.getNano();

            minSwaps = Math.min(minSwaps, genericSort.getSwaps());
            maxSwaps = Math.max(genericSort.getSwaps(), maxSwaps);
            totalSwaps += genericSort.getSwaps();

            minComparisons = Math.min(minComparisons, genericSort.getComparisons());
            maxComparisons = Math.max(genericSort.getComparisons(), maxComparisons);
            totalComparisons += genericSort.getComparisons();

            System.out.println("Sorted Array: " + Arrays.toString(testArray));
            System.out.println("Time: " + timeElapsed);
            System.out.println();
        }
        int averageTime = (totalTime - minTime - maxTime) / 10;
        double averageTimeInSeconds = averageTime / 1_000_000_000.0;
        int averageSwaps = (totalSwaps - minSwaps - maxSwaps)/10;
        int averageComparisons = (totalComparisons - minComparisons - maxComparisons)/10;
        System.out.println("Average Time (in seconds): " + averageTimeInSeconds);
        System.out.println("Average Number of Swaps: " + averageSwaps);
        System.out.println("Average Number of Comparisons: " + averageComparisons);
    }

    public void queueTester(ITemplateSort genericSort) {
        TestDataGenerator testDataGenerator = new TestDataGenerator(5000);
        int minTime, maxTime, totalTime;
        maxTime = totalTime = 0;
        minTime = Integer.MAX_VALUE;
        int minSwaps, maxSwaps, totalSwaps;
        maxSwaps = totalSwaps = 0;
        minSwaps = Integer.MAX_VALUE;
        int minComparisons, maxComparisons, totalComparisons;
        maxComparisons = totalComparisons = 0;
        minComparisons = Integer.MAX_VALUE;

        for (int i = 0; i < 12; i++) {
            Queue<Integer> testQueue = testDataGenerator.createQueueTestData();
            System.out.print("Initial Queue ");
            printQueue(testQueue);

            Instant start = Instant.now();  // time capture -- start
            genericSort.sort(testQueue);
            Instant end = Instant.now();    // time capture -- end
            Duration timeElapsed = Duration.between(start, end);

            minTime = Math.min(minTime, timeElapsed.getNano());
            maxTime = Math.max(timeElapsed.getNano(), maxTime);
            totalTime += timeElapsed.getNano();

            minSwaps = Math.min(minSwaps, genericSort.getSwaps());
            maxSwaps = Math.max(genericSort.getSwaps(), maxSwaps);
            totalSwaps += genericSort.getSwaps();

            minComparisons = Math.min(minComparisons, genericSort.getComparisons());
            maxComparisons = Math.max(genericSort.getComparisons(), maxComparisons);
            totalComparisons += genericSort.getComparisons();

            System.out.print("Sorted Queue ");
            printQueue(testQueue);

            System.out.println("Time: " + timeElapsed);
            System.out.println();
        }
        int averageTime = (totalTime - minTime - maxTime) / 10;
        double averageTimeInSeconds = averageTime / 1_000_000_000.0;
        int averageSwaps = (totalSwaps - minSwaps - maxSwaps)/10;
        int averageComparisons = (totalComparisons - minComparisons - maxComparisons)/10;
        System.out.println("Average Time (in seconds): " + averageTimeInSeconds);
        System.out.println("Average Number of Swaps: " + averageSwaps);
        System.out.println("Average Number of Comparisons: " + averageComparisons);
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
