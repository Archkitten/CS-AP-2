package csa.week5;

public class Wordle {

    public static void main(String[] args) {
        String hidden = "APPLE";
        String input = "PEARL";
        System.out.println(guess(hidden, input));
    }

    static String guess(String hidden, String input) {
        int len = hidden.length();
        char[] s = new char[len];
        char[] hc = hidden.toCharArray();
        char[] ic = input.toCharArray();
        int index = 0;
        for (int i = 0; i < len; i++) {
            if (hc[i] == ic[i]) {
                s[i] = hc[i];
            } else {
                s[i] = '*';
            }
        }

        for (int i = 0; i < len; i++) {
            System.out.println("i/s[i]=" + i + "/" + s[i]);
            if (s[i] == '*') {
                System.out.println("hi1");
                if (hidden.contains(Character.toString(ic[i]))) {
                    System.out.println("hi");
                    s[i] = '+';
                }

            }
        }

        return new String(s);
    }
}