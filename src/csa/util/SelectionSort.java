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
        LinkedList<Integer> dummyHead = new LinkedList<>(0, null);
        dummyHead.setNextNode(intQueue.head);
        LinkedList<Integer> node1=dummyHead, node2, minTempNode;

        for (int i = 0; i < intQueue.size; i++) {
            // "i" controls what has already been sorted.
            node1 = node1.getNext();
            int min = node1.getData();
            int minIndex = i;
            minTempNode = node1;
            // "j = i" prevents the algorithm from sorting what has already been sorted.
            // The "+ 1" is because we don't need to compare the minimum with the minimum again.
            node2 = node1;
            for (int j = i + 1; j < intQueue.size; j++) {
                // If the value we get to is less than j, set it as the new minimum.
                node2 = node2.getNext();
                if (node2.getData() < min) {
                    min = node2.getData();
                    minTempNode = node2;
                }
            }
            // Once we've found the minimum, swap the two values.
            minTempNode.setData(node1.getData());
            node1.setData(min);
            // Learning algorithmic strategies from Insertion Sort! Reduce swapping as much as possible!
        }
    }


}
