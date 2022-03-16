package com.csap2;

import java.util.Scanner;

public class BestSongHackathon extends Option {

    public BestSongHackathon() {
        optionName = "Best Song Hackathon";
    }

    public String getOptionName() {
        return optionName;
    }

    public void process(Scanner scanObj) {
        Song a = new Song("Something wonderful", "Dr. Seuss", 128.45, 3022);
        Song b = new Song("Something wonderful", "Dr. Seuss", 128.45, 3022);
        Song c = new Song("Something wonderful", "Dr. Seuss", 128.45, 3022);
        Song d = new Song("Something wonderful", "Dr. Seuss", 128.45, 3022);
        Song e = new Song("Something wonderful", "Dr. Seuss", 128.45, 3022);
        Song[] songArray = {a, b, c, d, e};

        for (int j = 0; j < songArray.length - 1; j++) {
            System.out.println(songArray[j].getSongName());
            System.out.println(songArray[j].getArtist());
            System.out.println(songArray[j].getDuration());
            System.out.println(songArray[j].getYear());
        }

        for (int i = 0; i < songArray.length - 1; i++) {
            System.out.println("What's the name of your " + i + "st favorite song?");
            String name = scanObj.nextLine();
            System.out.println("Artist's name (First name or Band name)?");
            String artist = scanObj.nextLine();
            System.out.println("How long is the song (double)?");
            double duration = Double.parseDouble(scanObj.nextLine());
            System.out.println("What year did the song come out?");
            int year = Integer.parseInt(scanObj.nextLine());

            songArray[i].setSongName(name);
            songArray[i].setArtist(artist);
            songArray[i].setDuration(duration);
            songArray[i].setYear(year);
        }

        for (int k = 0; k < songArray.length - 1; k++) {
            System.out.println(songArray[k].getSongName());
            System.out.println(songArray[k].getArtist());
            System.out.println(songArray[k].getDuration());
            System.out.println(songArray[k].getYear());
        }
    }
}
