package csa.week5;

public class Range implements NumberGroup {

    private int minimum;
    private int maximum;

    public Range(int minimum, int maximum) {
        this.minimum = minimum;
        this.maximum = maximum;
    }

    public boolean contains(int n) {
        return n >= minimum && n <= maximum;
    }
}
