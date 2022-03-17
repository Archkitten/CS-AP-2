package com;

import java.util.Scanner;

public class Option {

    protected String optionName = "Option";

    public String getOptionName() {
        return optionName;
    }

    public void process(Scanner scanObj) {
        System.out.println(optionName);
    }

    public void tester() {
        System.out.println("Test\n");
    }
}
