package csa.util;

public class BubbleSort implements ITemplateSort {

    @Override
    public void sort(int[] intArray) {
        // The amount of iterations is equal to the elements in the array, to account for the worst case scenario.
        for (int j = 1; j < intArray.length; j++) {
            // The sort itself will check each consecutive element and swap them if they are out of order.
            // This results in the largest value being bubbled to the top.
            // the "- j" prevents the bubble sort from resorting bubbled values.
            for (int i = 0; i < intArray.length - j; i++) {
                if (intArray[i] > intArray[i + 1]) {
                    // Swap the two values
                    int temp = intArray[i];
                    intArray[i] = intArray[i + 1];
                    intArray[i + 1] = temp;
                }
            }
        }
    }

    @Override
    public void sort(Queue<Integer> intQueue) {
        QueueIterator<Integer> it = (QueueIterator<Integer>) intQueue.iterator();
        // System.out.println(it.next());
        // Example being node 2
        while (it.hasNext()) {
            if (it.current.getData() > it.current.getNext().getData()) {
                // it.current.getPrevious() is node 1, it.current.getNext() is node 3
                // it.current.getPrevious().setNextNode(it.current.getNext());
                // it.current.setNextNode(it.current.getPrevious());
                int temp = it.current.getData();
                it.current.setData(it.current.getNext().getData());
                it.current.getNext().setData(temp);
            }
            // it.next() moves the pointer forward
            System.out.println(it.next());
        }

        /*
        // System.out.println(it.next());
            int temp = it.next();
            // Example being node 2
            while (it.hasNext()) {
                if (temp > it.next()) {
                    // it.current.getPrevious() is node 1, it.current.getNext() is node 3
                    // it.current.getPrevious().setNextNode(it.current.getNext());
                    // it.current.setNextNode(it.current.getPrevious());
                    it.current.getPrevious().setData(it.current.getData());
                    it.current.setData(temp);
                }
            }
         */

        // Direct Translation, doesn't work.
        /*
        for (int j = 1; j < intQueue.size; j++) {
            for (int i = 0; i < intQueue.size - j; i++) {
                if (intQueue.getHead().getData() > intQueue.getHead().getNext().getData()) {
                    int temp = intQueue.getHead().getData();
                    intQueue.getHead().setData(intQueue.getHead().getNext().getData());
                    intQueue.getHead().getNext().setData(temp);
                }
            }
        }
        */
    }
}
