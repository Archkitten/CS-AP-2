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
}
