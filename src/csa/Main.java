package csa;
import csa.util.Menu;
import csa.util.Option;
import csa.week0.WeekZero;
import csa.week1.WeekOne;
import csa.week2.WeekTwo;

public class Main {

    public static void main(String[] args) {
        Option one = new WeekZero();
        Option two = new WeekOne();
        Option three = new WeekTwo();

        Option[] options = new Option[] {one, two, three};

        Menu menu = new Menu();
        menu.run("\n----- MAIN MENU -----", options);
    }
}
