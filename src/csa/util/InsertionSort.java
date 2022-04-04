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
//        for (int i = 1; i < intQueue.size; i++) {
//            int j = i;
//            // "value" holds the current value, we'll hold this value in memory in case we need to move it back.
//            int value = intQueue[j];
//            while (j > 0 && value < intQueue[j - 1]) {
//                // Move all values up one until we find the place to insert "value".
//                intQueue[j] = intArray[j - 1];
//                j--;
//            }
//            intArray[j] = value;
//        }
        LinkedList<Integer> dummyHead = new LinkedList<>(0, null);
        dummyHead.setNextNode(intQueue.head);
        intQueue.head.setPrevNode(dummyHead);
        LinkedList<Integer> node1 = intQueue.head;
        LinkedList<Integer> node2;
        for (int i = 1; i < intQueue.size; i++) {
            int j = i;
            node1 = node1.getNext();
            // "value" holds the current value, we'll hold this value in memory in case we need to move it back.
            int value = node1.getData();
            node2 = node1.getPrevious();
            while (j > 0 && value < node2.getData()) {
                // Move all values up one until we find the place to insert "value".
                node2.getNext().setData(node2.getData());
                node2 = node2.getPrevious();
                j--;
            }
            node2.getNext().setData(value);
        }
    }

}
