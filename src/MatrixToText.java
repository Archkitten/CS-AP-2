public class MatrixToText extends Option {

    String optionName = "MatrixToText";

    public String getOptionName() {
        return optionName;
    }

    public static void numpad() {
        System.out.println("MatrixToText.numpad");
    }

    public static void keyboard() {
        System.out.println("MatrixToText.keyboard");
    }


    public void process() {
        System.out.println("MatrixToText");
    }

    public static void main(String[] args) {
        Option testerObj = new MatrixToText();
        testerObj.process();
    }
}
