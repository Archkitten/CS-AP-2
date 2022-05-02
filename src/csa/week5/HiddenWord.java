package csa.week5;

import java.util.Arrays;

public class HiddenWord {

    private String answer;
    private char[] answerArray;

    public HiddenWord(String answer) {
        this.answer = answer;
        answerArray = this.answer.toCharArray();
    }

    public String getHint(String guess) {
        // guessArray and hintArray
        char[] guessArray = guess.toCharArray();
        char[] hintArray = new char[guess.length()];

        // Fill everything in hintArray to * by default
        /*
        for (int i = 0; i < hintArray.length; i++) {
            hintArray[i] = '*';
        }
        */
        Arrays.fill(hintArray, '*');

        // Word-le Detection
        for (int i = 0; i < answerArray.length; i++) {
            // Correct, same position
            if (guessArray[i] == answerArray[i]) {
                hintArray[i] = answerArray[i];
//                System.out.println("i / hintArray[i]: " + i + "/" + hintArray[i]);
            }
            // Correct, different position
            else {
                for (int j = 0; j < answerArray.length; j++) {
                    if (guessArray[i] == answerArray[j]) {
                        hintArray[i] = '+';
                        break;
                    }
                }
            }
        }

        // Turn hintArray back into a String and return it
        String hint = new String(hintArray);

        return hint;
    }

    public static void main(String[] args) {
        System.out.println("Answer: TRASH");
        HiddenWord hw = new HiddenWord("TRASH");
        System.out.println("Guess: AUDIO");
        System.out.println(hw.getHint("AUDIO"));
        System.out.println("Guess: TRACK");
        System.out.println(hw.getHint("TRACK"));
        System.out.println("Guess: TRAPS");
        System.out.println(hw.getHint("TRAPS"));
        System.out.println("Guess: TRASH");
        System.out.println(hw.getHint("TRASH"));
    }
}
