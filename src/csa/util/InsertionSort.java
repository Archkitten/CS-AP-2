package csa.util;

public class InsertionSort implements ITemplateSort {

    @Override
    public void sort(int[] intArray) {
        // Woah! Much faster than the code I copied from, after a few modifications! No more swappers too!
        for (int i = 1; i < intArray.length; i++) {
            int j = i;
            // "value" holds the current value, we'll hold this value in memory in case we need to move it back.
            int value = intArray[j];
            while (j > 0 && value < intArray[j - 1]) {
                // Move all values up one until we find the place to insert "value".
                intArray[j] = intArray[j - 1];
                j--;
            }
            intArray[j] = value;
        }

        // Someone else's slightly more efficient code?
        /*
        for(int i = 1; i < intArray.length; i++) {
            int cur = intArray[i];
            int j = i - 1;
            while(j >= 0 && intArray[j] > cur) {
                intArray[j + 1] = intArray[j];
                j--;
            }
            intArray[j + 1] = cur;
        }
        */

        // My actual Insertion Sort, but using swappers
        /*
        for (int i = 1; i < intArray.length; i++) {
            int j = i;
            while (j > 0 && intArray[j] < intArray[j - 1]) {
                // If the current is less than the value before it, swap 'em.
                int temp = intArray[j];
                intArray[j] = intArray[j - 1];
                intArray[j - 1] = temp;
                j--;
            }
        }
        */

        // My old garbage reverse bubble sort:
        /*
        for (int i = 1; i < intArray.length; i++) {
            int j = i;
            while (j > 0) {
                if (intArray[j] < intArray[j - 1]) {
                    // If the current is less than the value before it, swap 'em.
                    int temp = intArray[j];
                    intArray[j] = intArray[j - 1];
                    intArray[j - 1] = temp;
                }
                j--;
            }
        }
        */
    }

    @Override
    public void sort(Queue<Integer> intQueue) {

    }

    // Swap if needed
    public void swapIfNeeded(Queue<Integer> queue, int index1, int index2) {
        // As long as they don't throw a QueueOutOfBoundsException...
        if (index1 < queue.size && index2 < queue.size) {

            LinkedList<Integer> node1 = queue.head;
            LinkedList<Integer> node2 = queue.head;

            // Finding node in the right position?
            for (int i = 0; i < index1; i++) {
                node1 = node1.getNext();
            }
            for (int i = 0; i < index2; i++) {
                node2 = node2.getNext();
            }

            // The actual swap!
            if (node1.getData() > node2.getData()) {
                Integer temp = node1.getData();
                node1.setData(node2.getData());
                node2.setData(temp);
            }
        }
    }
}
