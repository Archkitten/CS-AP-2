package csa.week2;
import csa.util.Option;

public class CalculatorTester extends Option {

    public CalculatorTester() {
        optionName = "Calculator";
    }

    public void tester() {
        Calculator simpleMath = new Calculator("100 + 200  * 3");
        System.out.println("Simple Math\n" + simpleMath);

        Calculator parenthesisMath = new Calculator("(100 + 200)  * 3");
        System.out.println("Parenthesis Math\n" + parenthesisMath);

        Calculator allMath = new Calculator("200 % 300 + 5 + 300 / 200 + 1 * 100");
        System.out.println("All Math\n" + allMath);

        Calculator allMath2 = new Calculator("200 % (300 + 5 + 300) / 200 + 1 * 100");
        System.out.println("All Math2\n" + allMath2);

        Calculator expMath = new Calculator("5 ^ 2");
        System.out.println("Exponent Math\n" + expMath);
    }
}
