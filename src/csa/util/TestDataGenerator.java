package csa.util;

public class TestDataGenerator {
    int size;
    public TestDataGenerator(int size) {
        this.size = size;
    }

    public int[] getTestData() {
        int[] intArray = new int[size];
        for (int i = 0; i < size; i++) {
            // If size is 5000, it chooses a number between 0 and 5000
            intArray[i] = (int)(Math.random() * (size + 1));
        }
        return intArray;
    }
}
