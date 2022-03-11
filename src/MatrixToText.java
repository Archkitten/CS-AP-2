public class MatrixToText extends Option {

    public MatrixToText() {
        optionName = "MatrixToText";
    }

    public String getOptionName() {
        return optionName;
    }

    private void numpad() {
        System.out.println("MatrixToText.numpad");
    }

    private void keyboard() {
        System.out.println("MatrixToText.keyboard");
    }


    public void process() {
        // super.process() will just run the process() method from Option.java
        super.process();
        // Ask user to run numpad or keyboard in the future
    }
}
