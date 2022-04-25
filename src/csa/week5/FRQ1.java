package csa.week5;
import csa.util.Option;

import java.util.Arrays;
import java.util.Scanner;

public class FRQ1 extends Option {

    public FRQ1() {
        optionName = "FRQ1";
    }

    public void tester() {
        System.out.println("{1, 2, 3, 4, 5}");
        int[] testArray = {1, 2, 3, 4, 5};
        System.out.println(arraySum(testArray));

        System.out.println("{1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}");
        int[][] testArray2 = {{1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}};
        System.out.println(Arrays.toString(rowSums(testArray2)));
    }

    // Question 1
    public static int arraySum(int[] arr) {
        int total = 0;
        for (int i : arr) {
            total += i;
        }
        return total;
    }

    // Question 2
    public static int[] rowSums(int[][] arr2D) {
        int[] total = new int[arr2D.length];
        for (int i = 0; i < arr2D.length; i++) {
            total[i] = arraySum(arr2D[i]);
        }
        return total;
    }

    // Question 3
    public static boolean isDiverse(int[][] arr2D) {
        int[] arr = rowSums(arr2D);
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    return false;
                }
            }
        }
        return true;
    }

}
