package csa.week6;
import csa.util.Option;

public class FRQ2 extends Option {

    public FRQ2() {
        optionName = "FRQ2";
    }

    public void tester() {
        GameSpinner g = new GameSpinner(4);
        System.out.println("Current Run:" + g.currentRun());
        System.out.println("Spin:" + g.spin());
        System.out.println("Current Run:" + g.currentRun());
        System.out.println("Spin:" + g.spin());
        System.out.println("Current Run:" + g.currentRun());
        System.out.println("Spin:" + g.spin());
        System.out.println("Current Run:" + g.currentRun());
        System.out.println("Spin:" + g.spin());
        System.out.println("Current Run:" + g.currentRun());
        System.out.println("Spin:" + g.spin());
        System.out.println("Spin:" + g.spin());
        System.out.println("Spin:" + g.spin());
        System.out.println("Current Run:" + g.currentRun());
    }
}
