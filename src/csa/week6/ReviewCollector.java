package csa.week6;
import java.util.ArrayList;

public class ReviewCollector

{
    private ArrayList<ProductReview> reviewList;
    private ArrayList<String> productList;

    /** Constructs a ReviewCollector object and initializes the instance variables. */
    public ReviewCollector() {
        reviewList = new ArrayList<ProductReview>();
        productList = new ArrayList<String>();
    }

    /** Adds a new review to the collection of reviews, as described in part (a). */

    public void addReview(ProductReview prodReview) {
        reviewList.add(prodReview);
        for (String i : productList) {
            if (prodReview.getName().equals(i)) {
                productList.add(prodReview.getName());
            }
        }
    }

    /** Returns the number of good reviews for a given product name, as described in part (b). */

    public int getNumGoodReviews(String prodName) {
        return prodName.indexOf("best");
    }

    // There may be instance variables, constructors, and methods not shown.

}