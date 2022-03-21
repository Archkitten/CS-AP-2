{% include navigation.html %}

# CSA

{% include csa_nav.html %}

## Week 1 - [Ticket](https://github.com/Archkitten/CS-AP-2/issues/3)

### (TPT) Study Group Challenge 1

Challenges:
0. Sub-menu separates assignments into weeks.
1. Add and delete elements in a queue.
2. Merge 2 queues into an ordered fashion.
3. Reverse a queue using a stack.

### [Tri 3: Tech Talk 1: Linked Lists Part 2](https://github.com/nighthawkcoders/nighthawk_csa/wiki/Tri-3:-Tech-Talk-1:-Linked-Lists-Part-2)

Linked List - Connects Objects to each other
```
import java.util.LinkedList;

LinkedList<String> myLinkedList = new LinkedList<String>();
myLinkedList.add("Above");
myLinkedList.add("Blob");
System.out.println(myLinkedList);
```

Iterable Interface - For each loop through... a Linked List?

Queue - Built on top of a List (FIRST IN FIRST OUT)
* (processes this one ->) above -> blob -> cup -> drip -> john -> leek -> nay -> ro -> wee -> null (<- add stuff here)
* To add elements, add to head (queuing)
* To delete elements, remove from tail (dequeue)

Stack - Also built on top of a List (LAST IN FIRST OUT)
* above (<- processes this one, new elements are also added here, like a stack of plates)
* blob
* cup
* drip
* john
* leek
* nay
* ro
* wee

Challenge 2 Hint: dequeue and requeue

nil - null

Challenge 3 Hint:
* Take a Queue, put it into a Stack, reprint the Stack.
* It works in theory, try it!

implements vs. extends
* 'implements' has no definition? usually from interface
* extends

Generic T - You can put whatever data type you wish into the LinkedList. Once a data type is put in, the entire LinkedList becomes (uses) that data type.
```
public class Queue<T> implements Iterable<T> {
    LinkedList<T> head, tail;
    // Rest of implementation not shown...
}
```

Double sided Linked List
* Previous Node
* and Next Node
* null <- above <-> blob <-> cup -> null

### Challenge #1: Add and Delete elements in a Queue
Queue.java
```
package csa.util;

import java.util.Iterator;

public class Queue<T> implements Iterable<T> {
    LinkedList<T> head, tail;
    int size = 0;

    private boolean debug = false;

    public void setDebug(boolean isDebug) {
        debug = isDebug;
    }

    /**
     *  Add a new object at the end of the Queue,
     *
     * @param  data,  is the data to be inserted in the Queue.
     */
    public void add(T data) {
        if (debug) {
            System.out.println("Enqueued data: " + data);
        }
        // add new object to end of Queue
        LinkedList<T> tail = new LinkedList<>(data, null);
        size++;

        if (head == null)  // initial condition
            this.head = this.tail = tail;
        else {  // nodes in queue
            this.tail.setNextNode(tail); // current tail points to new tail
            this.tail = tail;  // update tail
        }
    }

    public void delete() {
        if (debug) {
            System.out.println("Dequeued data: " + this.head.getData());
        }
        // Technically the data is still there, but the pointer (starting place) has been moved to the next one,
        // meaning it will never be accessed. So mission accomplished?
        this.head = this.head.getNext();
        size--;
    }
   
...
```
QueueManager.java
```
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
    
...

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
```

### Challenge #2: Merge Queues
QueueManager.java
```
    // Made for Challenge #2, the Merge Queue after one of the queues has run out of data.
    public void appendQueue(Queue<T> q) {
        this.queue.getTail().setNextNode(q.getHead());
        queue.size += q.size;
    }
```
ChallengeTwo.java
```
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
            /*
            while (q2.queue.getHead() != null) {
                q3.queue.add(q2.queue.getHead().getData());
                q2.queue.delete();
            }
            */
            q3.appendQueue(q2.queue);
        }
        // Else if q2 has finished its course, add the remaining values from q1 into q3.
        else if (q2.queue.getHead() == null) {
            /*
            while (q1.queue.getHead() != null) {
                q3.queue.add(q1.queue.getHead().getData());
                q1.queue.delete();
            }
            */
            q3.appendQueue(q1.queue);
        }
    }
```

### Challenge #3: Reverse Queue using Stack
ChallengeThree.java
```
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
}
```
