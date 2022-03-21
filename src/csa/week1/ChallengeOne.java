package csa.week1;
import csa.util.Option;
import csa.util.QueueManager;

public class ChallengeOne extends Option {

    public ChallengeOne() {
        optionName = "Challenge #1 (Add and Delete elements in a Queue)";
    }

    public void tester() {
        // Object[] Words = new String[] {"blob", "drip", "ro"};
        QueueManager myQueue = new QueueManager("Words");
        myQueue.queue.setDebug(true);
        // myQueue.addList(Words);
        // myQueue.printQueue();

        // The commented code above is what's normally supposed to happen, but
        // I wanted to show and print each step of the data being added to the queue.
        myQueue.queue.add("blob");
        myQueue.printQueue();
        myQueue.queue.add("drip");
        myQueue.printQueue();
        myQueue.queue.add("ro");
        myQueue.printQueue();

        myQueue.queue.delete();
        myQueue.printQueue();
        myQueue.queue.delete();
        myQueue.printQueue();
        myQueue.queue.delete();
        myQueue.printQueue();
    }

}
