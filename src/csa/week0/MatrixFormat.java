package csa.week0;
import csa.util.Menu;
import csa.util.Option;

public class MatrixFormat extends Option {

    public MatrixFormat() {
        optionName = "Matrix Format";
    }

    public void tester() {
        Option one = new Numpad();
        Option two = new Keyboard();

        Option[] options = new Option[] {one, two};

        Menu menu = new Menu();
        menu.run("\nNumpad or Keyboard?", options);
    }
}
