package csa.week1;
import csa.util.Option;
import csa.util.QueueManager;
import csa.util.Stack;

public class ChallengeThree extends Option {

    public ChallengeThree() {
        optionName = "Challenge #3 (Reverse Queue using Stack)";
    }

    public void tester() {
        Integer[] numbers123 = new Integer[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        QueueManager<Integer> integerQueue = new QueueManager<>("IntegerQueue", numbers123);

        // Print initial Queue
        System.out.println("Initial Queue:");
        integerQueue.printQueue();

        // Reverse Queue via Stack (Created a Stack)
        Stack<Integer> integerStack = new Stack<>();

        // Put Queue into Stack
        while (integerQueue.queue.getHead() != null) {
            integerStack.push(integerQueue.queue.getHead().getData());
            integerQueue.queue.delete();
        }

        // Print out Stack
        /*
        while (integerStack.peek() != null) {
            System.out.print(integerStack.peek() + " ");
            integerStack.pop();
        }
        */

        // Put elements from Stack into Queue
        while (integerStack.peek() != null) {
            // System.out.print(integerStack.peek() + " ");
            integerQueue.queue.add(integerStack.pop());
        }

        // Print out the Reversed Queue
        System.out.println("After reversion:");
        integerQueue.printQueue();
    }

    // Tester
    public static void main(String[] args) {
        ChallengeThree t = new ChallengeThree();
        t.tester();
    }
}
