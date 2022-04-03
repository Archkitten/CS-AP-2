package csa.util;
import java.util.Random;

public class TestDataGenerator {
    int size;
    public TestDataGenerator(int size) {
        this.size = size;
    }

    public int[] getTestData() {
        int[] intArray = new int[size];
        Random rand = new Random();
        for (int i = 0; i < size; i++) {
            intArray[i] = rand.nextInt();
        }
        return intArray;
    }
}
