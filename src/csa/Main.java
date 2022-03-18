package csa;
import csa.util.Menu;
import csa.util.Option;
import csa.week0.WeekZero;

public class Main {

    public static void main(String[] args) {
        Option one = new WeekZero();
        Option two = new WeekZero();

        Option[] options = new Option[] {one, two};

        Menu menu = new Menu();
        menu.run("\n----- MAIN MENU -----", options);
    }
}
