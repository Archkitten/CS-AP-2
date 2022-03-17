package com.week0;

import com.Option;

import java.util.Scanner;

public class NumberSwap extends Option {

    public NumberSwap() {
        optionName = "Number Swap";
    }

    public String getOptionName() {
        return optionName;
    }

    private void swap() {
        Scanner scanObj = new Scanner(System.in);

        System.out.println("Input first integer:");
        int a = scanObj.nextInt();
        System.out.println("Input second integer:");
        int b = scanObj.nextInt();

        if (a > b) {
            int temp = a;
            a = b;
            b = temp;
        }
        System.out.println(a + " " + b);
    }


    public void process(Scanner scanObj) {
        // super.process() will just run the process() method from Option.java
        super.process(scanObj);
        // Then run swap()
        NumberSwap testObj = new NumberSwap();
        testObj.swap();
    }
}
