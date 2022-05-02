package csa.week5;

public class Range implements NumberGroup {

    private int[] range;

    public Range(int a, int b) {
        range = new int[b - a];

        for (int i = 0; i < range.length; i++) {
            range[i] = a + i;
        }
    }

    // Delete this later, used for checking
    public int[] getRange() {
        return range;
    }

    @Override
    public boolean isInGroup() {
        return false;
    }

    public static void main(String[] args) {

    }
}
