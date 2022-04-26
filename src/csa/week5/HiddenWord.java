package csa.week5;

public class HiddenWord {

    private String hiddenWord;

    public HiddenWord(String hiddenWord) {
        this.hiddenWord = hiddenWord;
    }

    public String getHint(String guess) {
        String s = "";
        Boolean found = false;
        for (int g = 0; g < guess.length(); g++) {
            // Stupid
            // System.out.println("G: " + g);
            for (int h = 0; h < hiddenWord.length(); h++) {
                // Stupid
                // System.out.println("H: " + h + guess.charAt(g) + hiddenWord.charAt(h));
                if (guess.charAt(g) == hiddenWord.charAt(h)) {
                    if (g == h) {
                        s += guess.charAt(g);
                        // Stupid
                        // System.out.println("S1: " + s);
                    }
                    else {
                        s += "+";
                        // Stupid
                        // System.out.println("S2: " + s);
                    }
                    found = true;
                    // Stupid
                    // System.out.println("Found1: " + found);
                    break;
                }
                else {
                    found = false;
                    // Stupid
                    // System.out.println("Found2: " + found);
                }
            }
            if (!found) {
                s += "*";
                // Stupid
                // System.out.println("S5: " + s);
            }
        }
        return s;
    }

    public static void main(String[] args) {
        HiddenWord test = new HiddenWord("APPLE");
        System.out.println("APPLE");

        System.out.println("Guessing: APPLE");
        System.out.println(test.getHint("APPLE"));


//        System.out.println("Guessing: AUDIO");
//        System.out.println(test.getHint("AUDIO"));

//        System.out.println("Guessing: APPLY");
//        System.out.println(test.getHint("APPLY"));
//
//        System.out.println("Guessing: LOSER");
//        System.out.println(test.getHint("LOSER"));
    }
}
