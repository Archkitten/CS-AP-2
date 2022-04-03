package csa.util;

public class InsertionSort implements ITemplateSort {

    @Override
    public void sort(int[] intArray) {
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
}
