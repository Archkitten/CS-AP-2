package csa.week6;

public class Theatre {
    private Seat[][] theaterSeats;

    // Question 1
    public Theatre(int seatsPerRow, int tier1Rows, int tier2Rows) {
        theaterSeats = new Seat[tier1Rows + tier2Rows][seatsPerRow];
    }

    // Question 2
    public boolean reassignSeat(int fromRow, int fromCol, int toRow, int toCol) {
        // If the seat is available...
        if (theaterSeats[toRow][toCol].isAvailable()) {
            // And if the tier of the desired seat is equal to or higher than their current one...
            if (theaterSeats[toRow][toCol].getTier() >= theaterSeats[fromRow][fromCol].getTier()) {
                // Remove the person from the seat
                theaterSeats[fromRow][fromCol].setAvailability(true);
                // Relocate them to desired area
                theaterSeats[toRow][toCol].setAvailability(false);
                // Return true
                return true;
            }
        }
        // Otherwise, return false
        return false;
    }
}
