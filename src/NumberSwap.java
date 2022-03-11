public class NumberSwap extends Option {

    public NumberSwap() {
        optionName = "NumberSwap";
    }

    public String getOptionName() {
        return optionName;
    }

    private void swap() {
        System.out.println("NumberSwap.swap");
    }


    public void process() {
        // super.process() will just run the process() method from Option.java
        super.process();
        // Then run swap()
    }
}
