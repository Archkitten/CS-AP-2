package csa.week6;

public class GameSpinner {
    private int sectors;
    private static int run = 0;
    private int previousResult = 0;

    public GameSpinner(int sectors) {
        this.sectors = sectors;
    }

    public int currentRun() {
        return run;
    }

    public int spin() {
        int result = (int)(Math.random() * sectors + 1);
        if (previousResult == 0 || result == previousResult) {
            run += 1;
        }
        else {
            run = 0;
        }
        previousResult = result;
        return result;
    }
}
