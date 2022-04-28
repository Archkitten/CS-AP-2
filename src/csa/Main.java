package csa;
import csa.util.Menu;
import csa.util.Option;
import csa.week0.WeekZero;
import csa.week1.WeekOne;
import csa.week2.WeekTwo;
import csa.week3.WeekThree;
import csa.week5.WeekFive;
import csa.week6.WeekSix;

public class Main {

    public static void main(String[] args) {
        Option one = new WeekZero();
        Option two = new WeekOne();
        Option three = new WeekTwo();
        Option four = new WeekThree();
        Option five = new WeekFive();
        Option six = new WeekSix();

        Option[] options = new Option[] {one, two, three, four, five};

        Menu menu = new Menu();
        menu.run("\n----- MAIN MENU -----", options);
    }
}
