package csa.week0;
import csa.util.Option;

public class NumberSwap extends Option {

    public NumberSwap() {
        optionName = "Number Swap";
    }

    public void tester() {
        System.out.println(swap(1, 2));
        System.out.println(swap(60, 30));
        System.out.println(swap(9, -11));
    }

    private String swap(int a, int b) {
        if (a > b) {
            int temp = a;
            a = b;
            b = temp;
        }
        return (a + " " + b);
    }

}
