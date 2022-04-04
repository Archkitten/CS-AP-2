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
        }
        // Learning algorithmic strategies from Insertion Sort! Reduce swapping as much as possible!
    }
}
