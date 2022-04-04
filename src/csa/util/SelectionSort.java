package csa.util;

public class SelectionSort implements ITemplateSort {

    @Override
    public void sort(int[] intArray) {
        for (int i = 0; i < intArray.length; i++) {
            // "i" controls what has already been sorted.
            int min = intArray[i];
            int minIndex = i;
            // "j = i" prevents the algorithm from sorting what has already been sorted.
            // The "+ 1" is because we don't need to compare the minimum with the minimum again.
            for (int j = i + 1; j < intArray.length; j++) {
                // If the value we get to is less than j, set it as the new minimum.
                if (intArray[j] < min) {
                    min = intArray[j];
                    minIndex = j;
                }
            }
            // Once we've found the minimum, swap the two values.
            intArray[minIndex] = intArray[i];
            intArray[i] = min;
            // Learning algorithmic strategies from Insertion Sort! Reduce swapping as much as possible!
        }

        // I tried getting rid of "min" and replace it with "temp", but...
        // Line 36 is slower since I need to find the element of the index again.
        /*
        for (int i = 0; i < intArray.length; i++) {
            // "i" controls what has already been sorted.
            int minIndex = i;
            // "j = i" prevents the algorithm from sorting what has already been sorted.
            // The "+ 1" is because we don't need to compare the minimum with the minimum again.
            for (int j = i + 1; j < intArray.length; j++) {
                // If the value we get to is less than j, set it as the new minimum.
                if (intArray[j] < intArray[minIndex]) {
                    minIndex = j;
                }
            }
            // Once we've found the minimum, swap the two values.
            if (minIndex != i) {
                int temp = intArray[minIndex];
                intArray[minIndex] = intArray[i];
                intArray[i] = temp;
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
