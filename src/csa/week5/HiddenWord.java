package csa.week5;

public class HiddenWord {

    private String hiddenWord;

    public HiddenWord(String hiddenWord) {
        this.hiddenWord = hiddenWord;
    }

    public String getHint(String guess) {
        String s = "";
        for (int g = 0; g < guess.length(); g++) {
            for (int h = 0; h < hiddenWord.length(); h++) {
                if (guess.charAt(g) == hiddenWord.charAt(h) && g == h) {
                    s += guess.charAt(g);
                }
                else if (guess.charAt(g) == hiddenWord.charAt(h)) {
                    s += "+";
                }
            }
            s += "*";
        }
        return s;
    }
}
