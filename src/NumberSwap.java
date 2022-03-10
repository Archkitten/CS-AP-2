public class NumberSwap extends Option {

    String optionName = "NumberSwap";

    public String getOptionName() {
        return optionName;
    }

    public static void swap() {
        System.out.println("NumberSwap.swap");
    }


    public void process() {
        System.out.println("NumberSwap");
    }

    public static void main(String[] args) {
        Option testerObj = new NumberSwap();
        testerObj.process();
    }
}
