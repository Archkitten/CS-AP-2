package csa.util;

/**
 * Queue Manager
 * 1. "has a" Queue
 * 2. support management of Queue tasks (aka: titling, adding a list, printing)
 */
public class QueueManager<T> {
    // queue data
    private final String name; // name of queue
    public final Queue<T> queue = new Queue<>(); // queue object

    /**
     *  Queue constructor
     *  Title with empty queue
     */
    public QueueManager(String name) {
        this.name = name;
    }

    /**
     *  Queue constructor
     *  Title with series of Arrays of Objects
     */
    public QueueManager(String name, T[]... seriesOfObjects) {
        this.name = name;
        this.addList(seriesOfObjects);
    }

    /**
     * Add a list of objects to queue
     */
    public void addList(T[]... seriesOfObjects) {
        for (T[] objects: seriesOfObjects)
            for (T data : objects) {
                this.queue.add(data);
            }
    }

    // Made for Challenge #2, the Merge Queue after one of the queues has run out of data.
    public void appendQueue(Queue<T> q) {
        this.queue.getTail().setNextNode(q.getHead());
        queue.size += q.size;
    }

    /**
     * Print any array objects from queue
     */
    public void printQueue() {
        System.out.print(this.name + " count: " + queue.size + ", ");
        System.out.print("data: ");
        for (T data : queue) {
            System.out.print(data + " ");
        }
        if (queue.getHead() == null) {
            System.out.print("null");
        }
        System.out.println();
    }
}
