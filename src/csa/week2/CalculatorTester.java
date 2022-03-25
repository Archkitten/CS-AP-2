package csa.week2;
import csa.util.Option;
import java.util.Scanner;

public class CalculatorTester extends Option {

    public CalculatorTester() {
        optionName = "Calculator";
    }

    public void tester() {
        Calculator simpleMath = new Calculator("100 + 200  * 3");
        System.out.println("\nSimple Math\n" + simpleMath);

        Calculator parenthesisMath = new Calculator("(100 + 200)  * 3");
        System.out.println("\nParenthesis Math\n" + parenthesisMath);

        Calculator allMath = new Calculator("200 % 300 + 5 + 300 / 200 + 1 * 100");
        System.out.println("\nAll Math\n" + allMath);

        Calculator allMath2 = new Calculator("200 % (300 + 5 + 300) / 200 + 1 * 100");
        System.out.println("\nAll Math2\n" + allMath2);

        Calculator expMath = new Calculator("2 * 5 ^ 2 * 2");
        System.out.println("\nExponent Math\n" + expMath);

        Calculator sqrtMath = new Calculator("√(60 + 4) * √4 ^ 2");
        System.out.println("\nSquare Root Math\n" + sqrtMath);

        Scanner scanObj = new Scanner(System.in);
        System.out.println("\nEnter your own math equation to calculate:");
        String customString = scanObj.nextLine();
        Calculator customMath = new Calculator(customString);
        System.out.println("\nCustom Math\n" + customMath);
    }
}
