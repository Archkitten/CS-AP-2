package csa.week1;
import csa.util.Option;
import csa.util.QueueManager;

public class ChallengeTwo extends Option {

    private Integer[] numbers1 = new Integer[] {1, 4, 5, 8, 9, 10, 11};
    private Integer[] numbers2 = new Integer[] {2, 3, 6, 7};
    private QueueManager<Integer> q1 = new QueueManager("Q1", numbers1);
    private QueueManager<Integer> q2 = new QueueManager("Q2", numbers2);
    private QueueManager<Integer> q3 = new QueueManager("Q3");

    public ChallengeTwo() {
        optionName = "Challenge #2";
    }

    public void tester() {
        mergeQueues();
        q3.printQueue();
    }

    public void mergeQueues() {

        while (q1.queue.getHead() != null && q2.queue.getHead() != null) {
            // If q1 is less than (or equal to) q2, add the value from q1 into q3.
            // Then delete the head of q1.
            if (q1.queue.getHead().getData() <= q2.queue.getHead().getData()) {
                q3.queue.add(q1.queue.getHead().getData());
                q1.queue.delete();
            }
            // Otherwise, add the value from q2 into q3.
            else {
                q3.queue.add(q2.queue.getHead().getData());
                q2.queue.delete();
            }
        }

        // If q1 has finished its course, add the remaining values from q2 into q3.
        if (q1.queue.getHead() == null) {
            // You know, I could've also just linked q3's tail to q2's head.
            // It would've been much more efficient.
            // But I cannot for the life of me find out how to do so through code, so...
            // This idiot solution stays.
            while (q2.queue.getHead() != null) {
                q3.queue.add(q2.queue.getHead().getData());
                q2.queue.delete();
            }
        }
        // Else if q2 has finished its course, add the remaining values from q1 into q3.
        else if (q2.queue.getHead() == null) {
            while (q1.queue.getHead() != null) {
                q3.queue.add(q1.queue.getHead().getData());
                q1.queue.delete();
            }
        }
    }

    // Tester
    public static void main(String[] args) {
        ChallengeTwo t = new ChallengeTwo();
        t.tester();
    }
}
