package csa.util;

public class MergeSort implements ITemplateSort {
    private int swaps = 0;
    private int comparisons = 0;

    @Override
    public void sort(int[] intArray) {
        // intArray.length will be called on a lot, so defining it beforehand saves time.
        int intArrayLength = intArray.length;

        // If the length of the array is one... well, start merging. This works because RECURSION.
        if (intArrayLength == 1) {
            return;
        }

        // defining intArrayLength / 2 because that's also used a lot.
        int intArrayMidpoint = intArrayLength / 2;

        // Create the two halves of intArray
        int[] arrayOne = new int[intArrayMidpoint];
        // "intArrayLength -" Deals with odd numbers, since arrayTwo will be larger than arrayOne.
        int[] arrayTwo = new int[intArrayLength - intArrayMidpoint];

        int i = 0, j = 0;
        // For the first half of the array, add to arrayOne.
        while (i < intArrayMidpoint) {
            arrayOne[i] = intArray[i];
            i++;
        }
        // For the second half of the array, add to arrayTwo.
        // Also, reset the pointer for arrayTwo.
        // Keep the pointer for intArray the same.
        while (i < intArrayLength) {
            arrayTwo[j++] = intArray[i++];
        }

        // Start RECURSION
        sort(arrayOne);
        sort(arrayTwo);

        // After RECURSION
        merge(intArray, arrayOne, arrayTwo);
    }

    private void merge(int[] arrayMerged, int[] arrayOne, int[] arrayTwo) {
        int i = 0, j = 0, k = 0;

        // If both arrays still have elements...
        while (i < arrayOne.length && j < arrayTwo.length) {
            // If arrayOne is less than arrayTwo, add the element of arrayOne.
            comparisons++;
            if (arrayOne[i] < arrayTwo[j]) {
                arrayMerged[k] = arrayOne[i];
                i++;
            }
            else { // If arrayTwo is less than arrayOne, add the element of arrayTwo.
                arrayMerged[k] = arrayTwo[j];
                j++;
            }
            k++;
        }

        // If arrayOne has run its course...
        if (i == arrayOne.length) {
            // Add the rest of arrayTwo into arrayMerged.
            while (j < arrayTwo.length) {
                arrayMerged[k++] = arrayTwo[j++];
            }
        }
        // If arrayTwo has run its course...
        else {
            // Add the rest of arrayOne into arrayMerged.
            while (i < arrayOne.length) {
                arrayMerged[k++] = arrayOne[i++];
            }
        }
    }

    @Override
    public void sort(Queue<Integer> intQueue) {
        int intQueueLength = intQueue.size;

        if (intQueueLength == 1) {
            return;
        }

        int intQueueMidpoint = intQueueLength / 2;

        Queue<Integer> q1 = new Queue<>();
        Queue<Integer> q2 = new Queue<>();

        int i = 0;
        while (i < intQueueMidpoint) {
            q1.add(intQueue.getHead().getData());
            intQueue.delete();
            i++;
        }
        while (i < intQueueLength) {
            q2.add(intQueue.getHead().getData());
            intQueue.delete();
            i++;
        }

        sort(q1);
        sort(q2);

        mergeQueues(intQueue, q1, q2);
    }

    private void mergeQueues(Queue<Integer> qMerged, Queue<Integer> q1, Queue<Integer> q2) {
        while (q1.getHead() != null && q2.getHead() != null) {
            // If q1 is less than (or equal to) q2, add the value from q1 into q3.
            // Then delete the head of q1.
            comparisons++;
            if (q1.getHead().getData() <= q2.getHead().getData()) {
                qMerged.add(q1.getHead().getData());
                q1.delete();
            }
            // Otherwise, add the value from q2 into q3.
            else {
                qMerged.add(q2.getHead().getData());
                q2.delete();
            }
        }

        // If q1 has finished its course, add the remaining values from q2 into q3.
        if (q1.getHead() == null) {
            /*
            while (q2.queue.getHead() != null) {
                q3.queue.add(q2.queue.getHead().getData());
                q2.queue.delete();
            }
            */
            qMerged.getTail().setNextNode(q2.getHead());
        }
        // Else if q2 has finished its course, add the remaining values from q1 into q3.
        else if (q2.getHead() == null) {
            /*
            while (q1.queue.getHead() != null) {
                q3.queue.add(q1.queue.getHead().getData());
                q1.queue.delete();
            }
            */
            qMerged.getTail().setNextNode(q1.getHead());
        }
    }
    @Override
    public int getSwaps() {
        return this.swaps;
    }

    @Override
    public int getComparisons() {
        return this.comparisons;
    }
}
