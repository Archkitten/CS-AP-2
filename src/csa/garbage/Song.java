package csa.garbage;

public class Song {

    private String songName;
    private String artist;
    private double duration;
    private int year;

    public Song(String songName, String artist, double duration, int year) {
        this.songName = songName;
        this.artist = artist;
        this.duration = duration;
        this.year = year;
    }

    public String getSongName() {
        return songName;
    }

    public String getArtist() {
        return artist;
    }

    public double getDuration() {
        return duration;
    }

    public int getYear() {
        return year;
    }

    public void setSongName(String songName) {
        this.songName = songName;
    }

    public void setArtist(String artist) {
        this.artist = artist;
    }

    public void setDuration(double duration) {
        this.duration = duration;
    }

    public void setYear(int year) {
        this.year = year;
    }

}
