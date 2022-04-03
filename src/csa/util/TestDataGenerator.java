package csa.util;
import java.util.Random;

public class TestDataGenerator {
    int size;
    public TestDataGenerator(int size) {
        this.size = size;
    }

    public int[] getTestData() {
        int[] intArray = new int[size];
        for (int i = 0; i < size; i++) {
            Random rand = new Random();
            intArray[i] = rand.nextInt();
        }
        return intArray;
    }
}
