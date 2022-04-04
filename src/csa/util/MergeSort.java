package csa.util;

public class MergeSort implements ITemplateSort {

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
        while (i >= intArrayMidpoint && i < intArrayLength) {
            arrayTwo[j++] = intArray[i++];
        }

        // Start RECURSION
        sort(arrayOne);
        sort(arrayTwo);

        // After RECURSION
        merge(intArray, arrayOne, arrayTwo);
    }

    public void merge(int[] arrayMerged, int[] arrayOne, int[] arrayTwo) {
        int i = 0, j = 0, k = 0;

        // If both arrays still have elements...
        while (i < arrayOne.length && j < arrayTwo.length) {
            // If arrayOne is less than arrayTwo, add the element of arrayOne.
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
}
