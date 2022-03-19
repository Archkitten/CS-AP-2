package csa.week1;
import csa.util.Option;
import csa.util.QueueManager;

public class ChallengeOne extends Option {

    public ChallengeOne() {
        optionName = "Challenge #1";
    }

    public void tester() {
        QueueManager myQueue = new QueueManager("Words");

        myQueue.queue.add("blob");
        myQueue.printQueue();
        myQueue.queue.add("drip");
        myQueue.printQueue();
        myQueue.queue.add("ro");
        myQueue.printQueue();
    }

}
