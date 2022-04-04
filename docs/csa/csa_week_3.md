---
layout: default
---

# CSA

{% include csa_nav.html %}

## Week 3 - [Ticket](https://github.com/Archkitten/CS-AP-2/issues/7)

### Table of Contents
* Challenge #0: Time and Sample Size
* Challenge #1: Bubble Sort Objective 1
* Challenge #2: Insertion Sort Objective 1
* Challenge #3: Selection Sort Objective 1
* Challenge #4: Merge Sort Objective 1
* Final Judgement: Objective 1
* Challenge #0: System works with Queues
* Challenge #5: Merge Sort Objective 2
* Challenge #6: Bubble Sort Objective 2
* Challenge #7: Selection Sort Objective 2
* Challenge #8: Insertion Sort Objective 2
* Final Judgement: Objective 2

### (TPT) Study Group Challenge 3

Objective 1: Build all of these into your data structures.
* Here are the Sorts that CB wants you to work with and should work well with Queue that students developed in earlier labs: Bubble Sort, Selection Sort, Insertion Sort
* Consider Quick Sort and Merge Sort and its nature. Build a custom Merge Sort using a data structure that supports binary analysis.

Objective 2: Perform analysis on all of these sorts using 5,000 random pieces of data.
* Build a Wiki that describes your Sort implementations and the Big O complexity of that implementation.
* Establish analytics for comparisons and swaps average to perform each sort, run each at least 10 times and calculate an average
* Additionally, establish a timer and calculate average time for each of the sorts.
* Make a final/judgement on best sort considering Data Structure loading, Comparisons, Swaps, Big O complexity, and Time.

### [Tri 3: Tech Talk 3: Sorts](https://github.com/nighthawkcoders/nighthawk_csa/wiki/Tri-3:-Tech-Talk-3:-Sorts)

Objective 1: Perform analysis on all of these sorts using 5,000 random pieces of data.
* Build custom Bubble Sort, Selection Sort, Insertion Sort and Merge Sort.
* Build a GitHub page that describes Sort implementations and the Big O complexity of these Sorts.
* Establish analytics including: time, comparisons and swaps.
* Average the results for each each Sort, run each at least 12 times and 5000 elements. You should throw out High and Low when doing analysis.
* Make your final/judgement on best sort considering Data Structure loading, Comparisons, Swaps, Big O complexity, and Time.

Objective 2 (optional): Blow me away for auto 100% on all Data Structures work, caveat for calculator.
* Perform sorting and analysis on your own Data Structure and skip but incorporate requirements from Objective #1.
* Defend it in Live Grading with Teacher satisfaction.
* Requirements... Requires GitHub Pages, Analysis. Requires Talk about it.
* Purpose is to build data structure with functionality similar to what was done on ArrayList sort method.
* Must be done on your own data structure. Must contain minimum of 3 different Sorts, merge sort would be amazing.
* Allows you to receive maximum credit on the DS1, DS2 (still need string calculator), and Sorts. Also, maximum credit on Menu if it is of Quality and Organized.
* Allows you option to skip any "mandatory CB study activities" in 4 weeks after Spring Break with automatic A.
* My sample of Insertion Sort on Link List.

### Additional Resources Used

* [Turing Planet Sorting Overview](https://turingplanet.org/2020/02/11/%e6%8e%92%e5%ba%8f%e7%ae%97%e6%b3%95%e3%80%90%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84%e5%92%8c%e7%ae%97%e6%b3%953%e3%80%91/)
* [Java Bubble Sort](https://www.youtube.com/watch?v=F13_wsHDIG4)
* [Bubble Sort in 2 minutes](https://www.youtube.com/watch?v=xli_FI7CuzA)
* [Insertion Sort in 2 minutes](https://www.youtube.com/watch?v=JU767SDMDvA)
* [Selection Sort in 3 minutes](https://www.youtube.com/watch?v=g-PGLbMth_g)
* [Merge Sort in 3 minutes](https://www.youtube.com/watch?v=4VqmGXwpLqc)
* [Merge Sort Algorithm - Full Tutorial](https://www.youtube.com/watch?v=bOk35XmHPKs)

### Challenge #0: Time and Sample Size
SortTester.java
```
public class SortTester {
    public void tester(ITemplateSort genericSort) {
        TestDataGenerator testDataGenerator = new TestDataGenerator(5000);
        int minimum = 0;
        int maximum = 0;
        int totalTime = 0;

        for (int i = 0; i < 12; i++) {
            int[] testArray = testDataGenerator.getTestData();
            System.out.println("Initial Array: " + Arrays.toString(testArray));

            Instant start = Instant.now();  // time capture -- start
            genericSort.sort(testArray);
            Instant end = Instant.now();    // time capture -- end
            Duration timeElapsed = Duration.between(start, end);

            minimum = Math.min(minimum, timeElapsed.getNano());
            maximum = Math.max(timeElapsed.getNano(), maximum);
            totalTime += timeElapsed.getNano();

            System.out.println("Sorted Array: " + Arrays.toString(testArray));
            System.out.println("Time: " + timeElapsed);
            System.out.println();
        }
        int averageTime = (totalTime - minimum - maximum) / 10;
        double averageTimeInSeconds = averageTime / 1_000_000_000.0;
        System.out.println("Average Time (in seconds): " + averageTimeInSeconds);
    }
}
```
Getting the time of the sort (directly):
```
Instant end = Instant.now();
-
Instant start = Instant.now();
=
Duration timeElapsed = Duration.between(start, end);

System.out.println("Time: " + timeElapsed);
```
Getting the average time of all 12 sorts (excluding minimum and maximum):
```
minimum = Math.min(minimum, timeElapsed.getNano());
maximum = Math.max(timeElapsed.getNano(), maximum);
totalTime += timeElapsed.getNano();

int averageTime = (totalTime - minimum - maximum) / 10;
double averageTimeInSeconds = averageTime / 1_000_000_000.0;
System.out.println("Average Time (in seconds): " + averageTimeInSeconds);
```
Sample size of 12 - 2:
```
for (int i = 0; i < 12; i++) {
}
int averageTime = (totalTime - minimum - maximum) / 10;
```
5000 random pieces of data:
```
TestDataGenerator testDataGenerator = new TestDataGenerator(5000);
```
TestDataGenerator.java
```
public class TestDataGenerator {
    int size;
    public TestDataGenerator(int size) {
        this.size = size;
    }

    public int[] getTestData() {
        int[] intArray = new int[size];
        for (int i = 0; i < size; i++) {
            // If size is 5000, it chooses a number between 0 and 5000
            intArray[i] = (int)(Math.random() * (size + 1));
        }
        return intArray;
    }
}
```

### Challenge #1: Bubble Sort Objective 1
BubbleSort.java
* Analysis:
  * Average Speed (in seconds):
    * ~0.0460
  * Yeah, it's pretty slow.
  * Imagine iterating through each element of the array for each element of the array, and swapping every value along the way.
  * At least the "- j" prevents us from checking the values that have already been bubbled to the top. I only noticed that I was missing this after checking my answers, imagine how much slower it would be if I hadn't changed it!
  * Average Speed (without "- j"):
    * ~0.0500
```
// The amount of iterations is equal to the elements in the array, to account for the worst case scenario.
for (int j = 1; j < intArray.length; j++) {
    // The sort itself will check each consecutive element and swap them if they are out of order.
    // This results in the largest value being bubbled to the top.
    // the "- j" prevents the bubble sort from resorting bubbled values.
    for (int i = 0; i < intArray.length - j; i++) {
        if (intArray[i] > intArray[i + 1]) {
            // Swap the two values
            int temp = intArray[i];
            intArray[i] = intArray[i + 1];
            intArray[i + 1] = temp;
        }
    }
}
```

### Challenge #2: Insertion Sort Objective 1
InsertionSort.java - The Prequel
* Analysis:
  * Average Speed:
    * ~0.0150
  * So funny story, at the start of this coding session I was too impatient to learn about Insertion Sort (since I learned it a long time ago), so I decided to just look at a .gif of an Insertion Sort for visualization, and then IMMEDIATELY coded this.
  * Surprisingly, it worked!
  * What didn't work was the fact that I was still checking all the values that had already been sorted, essentially making this version equivalent to a glorified reverse bubble sort. Whoops.
```
// My old garbage reverse bubble sort:
for (int i = 1; i < intArray.length; i++) {
    int j = i;
    while (j > 0) {
        if (intArray[j] < intArray[j - 1]) {
            // If the current is less than the value before it, swap 'em.
            int temp = intArray[j];
            intArray[j] = intArray[j - 1];
            intArray[j - 1] = temp;
        }
        j--;
    }
}
```
InsertionSort.java - The Sequel to the Prequel
* Analysis:
  * Average Speed:
    * ~0.0070 seconds
  * Moving the if statement within the while loop fixed the problem above.
  * The reason why is that in the above example, it'll continue while looping regardless of whether the if-condition has been met or not.
  * By moving the if statement within the while loop, the while loop will stop once the condition has been met, saving precious time.
```
// My actual Insertion Sort, but using swappers
for (int i = 1; i < intArray.length; i++) {
    int j = i;
    while (j > 0 && intArray[j] < intArray[j - 1]) {
        // If the current is less than the value before it, swap 'em.
        int temp = intArray[j];
        intArray[j] = intArray[j - 1];
        intArray[j - 1] = temp;
        j--;
    }
}
```
InsertionSort.java - Turing Planet
* Analysis:
  * Average Speed:
    * ~0.0044
    * (I thought it was ~0.0060 before?)
  * I finally decided to go and take a look at someone else's example, and I found it quite interesting!
  * Instead of swapping each value backwards like in Bubble Sort, they decided to hold the value in a variable called "cur" and then located the right place to insert the value. Doing it this way saves so much time!
```
// Someone else's slightly more efficient code?
for(int i = 1; i < intArray.length; i++) {
    int cur = intArray[i];
    int j = i - 1;
    while(j >= 0 && intArray[j] > cur) {
        intArray[j + 1] = intArray[j];
        j--;
    }
    intArray[j + 1] = cur;
}
```
InsertionSort.java - FINAL VERSION
* Analysis:
  * Average Speed:
    * ~0.0042
  * I implemented the thought behind their code into my own, and it actually surprised me that my code ran faster than theirs!
  * I suspect it has something to do with the fact that I'm doing less operations in the form of those "- 1"s and "+ 1"s, and me having less of them.
```
// Woah! Much faster than the code I copied from, after a few modifications! No more swappers too!
for (int i = 1; i < intArray.length; i++) {
    int j = i;
    // "value" holds the current value, we'll hold this value in memory in case we need to move it back.
    int value = intArray[j];
    while (j > 0 && value < intArray[j - 1]) {
        // Move all values up one until we find the place to insert "value".
        intArray[j] = intArray[j - 1];
        j--;
    }
    intArray[j] = value;
}
```

### Challenge #3: Selection Sort Objective 1
SelectionSort.java - FINAL VERSION
* Analysis:
  * Average Speed:
    * ~0.0058
  * Now THIS is a reverse bubble sort.
  * But... with way less swapping. +Efficiency points
```
for (int i = 0; i < intArray.length; i++) {
    // "i" controls what has already been sorted.
    int min = intArray[i];
    int minIndex = i;
    // "j = i" prevents the algorithm from sorting what has already been sorted.
    // The "+ 1" is because we don't need to compare the minimum with the minimum again.
    for (int j = i + 1; j < intArray.length; j++) {
        // If the value we get to is less than j, set it as the new minimum.
        if (intArray[j] < min) {
            min = intArray[j];
            minIndex = j;
        }
    }
    // Once we've found the minimum, swap the two values.
    intArray[minIndex] = intArray[i];
    intArray[i] = min;
    // Learning algorithmic strategies from Insertion Sort! Reduce swapping as much as possible!
}
```
SelectionSort.java - The Sequel
* Analysis:
  * Average Speed:
    * ~0.0130
  * Not as good as what I coded above... sometimes less is more, y'know?
```
// I tried getting rid of "min" and replace it with "temp", but...
// Line 36 is slower since I need to find the element of the index again.
for (int i = 0; i < intArray.length; i++) {
    // "i" controls what has already been sorted.
    int minIndex = i;
    // "j = i" prevents the algorithm from sorting what has already been sorted.
    // The "+ 1" is because we don't need to compare the minimum with the minimum again.
    for (int j = i + 1; j < intArray.length; j++) {
        // If the value we get to is less than j, set it as the new minimum.
        if (intArray[j] < intArray[minIndex]) {
            minIndex = j;
        }
    }
    // Once we've found the minimum, swap the two values.
    if (minIndex != i) {
        int temp = intArray[minIndex];
        intArray[minIndex] = intArray[i];
        intArray[i] = temp;
    }
}
```

### Challenge #4: Merge Sort Objective 1
MergeSort.java
* Analysis:
  * Average Speed:
    * ~0.0010
  * Very fast.
```
public void sort(int[] intArray) {
    // intArray.length will be called on a lot, so defining it beforehand saves time.
    int intArrayLength = intArray.length;

    // If the length of the array is one... well, start merging. This works because RECURSION.
    if (intArrayLength == 1) {
        return;
    }

    // defining intArrayLength / 2 because that's also used a lot.
    int intArrayMidpoint = intArrayLength / 2;

    // Create the two halves of intArray
    int[] arrayOne = new int[intArrayMidpoint];
    // "intArrayLength -" Deals with odd numbers, since arrayTwo will be larger than arrayOne.
    int[] arrayTwo = new int[intArrayLength - intArrayMidpoint];

    int i = 0, j = 0;
    // For the first half of the array, add to arrayOne.
    while (i < intArrayMidpoint) {
        arrayOne[i] = intArray[i];
        i++;
    }
    // For the second half of the array, add to arrayTwo.
    // Also, reset the pointer for arrayTwo.
    // Keep the pointer for intArray the same.
    while (i < intArrayLength) {
        arrayTwo[j++] = intArray[i++];
    }

    // Start RECURSION
    sort(arrayOne);
    sort(arrayTwo);

    // After RECURSION
    merge(intArray, arrayOne, arrayTwo);
}

private void merge(int[] arrayMerged, int[] arrayOne, int[] arrayTwo) {
    int i = 0, j = 0, k = 0;

    // If both arrays still have elements...
    while (i < arrayOne.length && j < arrayTwo.length) {
        // If arrayOne is less than arrayTwo, add the element of arrayOne.
        if (arrayOne[i] < arrayTwo[j]) {
            arrayMerged[k] = arrayOne[i];
            i++;
        }
        else { // If arrayTwo is less than arrayOne, add the element of arrayTwo.
            arrayMerged[k] = arrayTwo[j];
            j++;
        }
        k++;
    }

    // If arrayOne has run its course...
    if (i == arrayOne.length) {
        // Add the rest of arrayTwo into arrayMerged.
        while (j < arrayTwo.length) {
            arrayMerged[k++] = arrayTwo[j++];
        }
    }
    // If arrayTwo has run its course...
    else {
        // Add the rest of arrayOne into arrayMerged.
        while (i < arrayOne.length) {
            arrayMerged[k++] = arrayOne[i++];
        }
    }
}
```

### Final Judgement: Objective 1
<table>
    <tr>
        <th>Sorting Algorithm</th>
        <th>Time (in seconds)</th>
        <th>Big O Complexity</th>
        <th>Swaps</th>
    </tr>
    <tr>
        <th>Bubble Sort</th>
        <td>~0.0460</td>
        <td>O(n^2)</td>
        <td>n^2</td>
    </tr>
    <tr>
        <th>Selection Sort</th>
        <td>~0.0058</td>
        <td>O(n^2)</td>
        <td>n</td>
    </tr>
    <tr>
        <th>Insertion Sort</th>
        <td>~0.0042</td>
        <td>O(n^2)</td>
        <td>n</td>
    </tr>
    <tr>
        <th>Merge Sort</th>
        <td>~0.0010</td>
        <td>O(log(n))</td>
        <td>0</td>
    </tr>
</table>

### Challenge #0: System works with Queues
SortTester.java

```
public void queueTester(ITemplateSort genericSort) {
    TestDataGenerator testDataGenerator = new TestDataGenerator(5000);
    int minimum = 0;
    int maximum = 0;
    int totalTime = 0;

    for (int i = 0; i < 12; i++) {
        Queue<Integer> testQueue = testDataGenerator.createQueueTestData();
        System.out.print("Initial Queue ");
        printQueue(testQueue);

        Instant start = Instant.now();  // time capture -- start
        genericSort.sort(testQueue);
        Instant end = Instant.now();    // time capture -- end
        Duration timeElapsed = Duration.between(start, end);

        minimum = Math.min(minimum, timeElapsed.getNano());
        maximum = Math.max(timeElapsed.getNano(), maximum);
        totalTime += timeElapsed.getNano();

        System.out.print("Sorted Queue ");
        printQueue(testQueue);

        System.out.println("Time: " + timeElapsed);
        System.out.println();
    }
    int averageTime = (totalTime - minimum - maximum) / 10;
    double averageTimeInSeconds = averageTime / 1_000_000_000.0;
    System.out.println("Average Time (in seconds): " + averageTimeInSeconds);
}

private void printQueue(Queue<Integer> queue) {
    System.out.print("data: ");
    for (Integer data : queue) {
        System.out.print(data + " ");
    }
    if (queue.getHead() == null) {
        System.out.print("null");
    }
    System.out.println();
}
```

TestDataGenerator.java

```
public Queue<Integer> createQueueTestData() {
    Queue<Integer> intQueue = new Queue<>();
    for (int i = 0; i < size; i++) {
        intQueue.add((int)(Math.random() * (size + 1)));
    }
    return intQueue;
}
```

### Challenge #5: Merge Sort Objective 2
MergeSort.java
* Analysis:
  * Average Speed:
    * ~0.0024
  * My mergeQueues method came from the Merge Queues Challenge we did during Week 1. I just had to modify it to work with Queue instead of QueueManager.
  * For sort, I just used the same logic from Objective 1.
  * The only difference is instead of having 3 pointers that add the two Arrays to the larger one, I deleted the elements from the two Queues in order to add it to the larger one.

```
@Override
public void sort(Queue<Integer> intQueue) {
    int intQueueLength = intQueue.size;

    if (intQueueLength == 1) {
        return;
    }

    int intQueueMidpoint = intQueueLength / 2;

    Queue<Integer> q1 = new Queue<>();
    Queue<Integer> q2 = new Queue<>();

    int i = 0;
    while (i < intQueueMidpoint) {
        q1.add(intQueue.getHead().getData());
        intQueue.delete();
        i++;
    }
    while (i < intQueueLength) {
        q2.add(intQueue.getHead().getData());
        intQueue.delete();
        i++;
    }

    sort(q1);
    sort(q2);

    mergeQueues(intQueue, q1, q2);
}

private void mergeQueues(Queue<Integer> qMerged, Queue<Integer> q1, Queue<Integer> q2) {
    while (q1.getHead() != null && q2.getHead() != null) {
        // If q1 is less than (or equal to) q2, add the value from q1 into q3.
        // Then delete the head of q1.
        if (q1.getHead().getData() <= q2.getHead().getData()) {
            qMerged.add(q1.getHead().getData());
            q1.delete();
        }
        // Otherwise, add the value from q2 into q3.
        else {
            qMerged.add(q2.getHead().getData());
            q2.delete();
        }
    }

    // If q1 has finished its course, add the remaining values from q2 into q3.
    if (q1.getHead() == null) {
        /*
        while (q2.queue.getHead() != null) {
            q3.queue.add(q2.queue.getHead().getData());
            q2.queue.delete();
        }
        */
        qMerged.getTail().setNextNode(q2.getHead());
    }
    // Else if q2 has finished its course, add the remaining values from q1 into q3.
    else if (q2.getHead() == null) {
        /*
        while (q1.queue.getHead() != null) {
            q3.queue.add(q1.queue.getHead().getData());
            q1.queue.delete();
        }
        */
        qMerged.getTail().setNextNode(q1.getHead());
    }
}
```

### Challenge #6: Bubble Sort Objective 2
BubbleSort.java
* Analysis:
  * Average Speed:
    * ~0.0840
  * Oh boy. This was difficult to figure out, and took... a long time.
  * I don't quite remember all the struggles and errors that I encountered, it was late and there were way too many.
  * Oh right, one thing I do remember: I was about to give up when I saw that TKperson had completed his version of Bubble Sort that had a runtime of 30 minutes.
  * I looked at how his code worked, and used it for inspiration on how to structure mine. I also noticed that his code ended up doing a triple nested for loop as a result of his swap() function.
  * I also noticed that the third for loop was the same as the second for loop, so it wasn't needed. I integrated his swap() function into mine without calling a new function, but it still didn't work.
  * What ended up fixing everything was learning about the idea of a dummy head, where the dummy head moves but the real head doesn't.

```
LinkedList<Integer> dummyHead = new LinkedList<>(0, null);
dummyHead.setNextNode(intQueue.head);
LinkedList<Integer> node1, node2;

for (int j = 1; j < intQueue.size; j++) {
    node1 = dummyHead;
    for (int i = 0; i < intQueue.size - j; i++) {
        node1 = node1.getNext();
        node2 = node1.getNext();

        if (node1.getData() > node2.getData()) {
            Integer temp = node1.getData();
            node1.setData(node2.getData());
            node2.setData(temp);
        }
    }
}
```

### Challenge #7: Selection Sort Objective 2
SelectionSort.java
* Analysis:
  * Average Speed:
    * ~0.0490
  * After learning about swapping values and the dummy head, this was a breeze.

```
LinkedList<Integer> dummyHead = new LinkedList<>(0, null);
dummyHead.setNextNode(intQueue.head);
LinkedList<Integer> node1=dummyHead, node2, minTempNode;

for (int i = 0; i < intQueue.size; i++) {
    // "i" controls what has already been sorted.
    node1 = node1.getNext();
    int min = node1.getData();
    int minIndex = i;
    minTempNode = node1;
    // "j = i" prevents the algorithm from sorting what has already been sorted.
    // The "+ 1" is because we don't need to compare the minimum with the minimum again.
    node2 = node1;
    for (int j = i + 1; j < intQueue.size; j++) {
        // If the value we get to is less than j, set it as the new minimum.
        node2 = node2.getNext();
        if (node2.getData() < min) {
            min = node2.getData();
            minTempNode = node2;
        }
    }
    // Once we've found the minimum, swap the two values.
    minTempNode.setData(node1.getData());
    node1.setData(min);
    // Learning algorithmic strategies from Insertion Sort! Reduce swapping as much as possible!
}
```

### Challenge #8: Insertion Sort Objective 2
InsertionSort.java
* Analysis:
  * Average Speed:
    * ~0.0320
  * There was a NullPointerExceptionError that happened.
  * I looked at Mr. Mortensen's custom Queue class again and found that I was missing some code about the curr value.
  * Adding the code fixed the error. ¯\_(ツ)_/¯

```
LinkedList<Integer> dummyHead = new LinkedList<>(0, null);
dummyHead.setNextNode(intQueue.head);
intQueue.head.setPrevNode(dummyHead);
LinkedList<Integer> node1 = intQueue.head;
LinkedList<Integer> node2;
for (int i = 1; i < intQueue.size; i++) {
    int j = i;
    node1 = node1.getNext();
    // "value" holds the current value, we'll hold this value in memory in case we need to move it back.
    int value = node1.getData();
    node2 = node1.getPrevious();
    while (j > 0 && value < node2.getData()) {
        // Move all values up one until we find the place to insert "value".
        node2.getNext().setData(node2.getData());
        node2 = node2.getPrevious();
        j--;
    }
    node2.getNext().setData(value);
}
```

### Final Judgement: Objective 2
If the Bubble Sort was still O(n^3) with the triple nested for loop, it may have taken ~20-30 minutes to run through 5000 elements!
<table>
    <tr>
        <th>Sorting Algorithm</th>
        <th>Queue Time (in seconds)</th>
        <th>Array Time (in seconds)</th>
        <th>Big O Complexity</th>
        <th>Swaps</th>
    </tr>
    <tr>
        <th>Bubble Sort</th>
        <td>~0.0840</td>
        <td>~0.0460</td>
        <td>O(n^2)</td>
        <td>n^2</td>
    </tr>
    <tr>
        <th>Selection Sort</th>
        <td>~0.0490</td>
        <td>~0.0058</td>
        <td>O(n^2)</td>
        <td>n</td>
    </tr>
    <tr>
        <th>Insertion Sort</th>
        <td>~0.0320</td>
        <td>~0.0042</td>
        <td>O(n^2)</td>
        <td>n</td>
    </tr>
    <tr>
        <th>Merge Sort</th>
        <td>~0.0024</td>
        <td>~0.0010</td>
        <td>O(log(n))</td>
        <td>0</td>
    </tr>
</table>
