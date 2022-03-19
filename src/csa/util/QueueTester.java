package csa.util;

/**
 * Driver Class
 * Tests queue with string, integers, and mixes of Classes and types
 */
public class QueueTester {
    public static void main(String[] args) {
        // Create iterable Queue of Words
        Object[] words = new String[]{"seven", "slimy", "snakes", "sallying", "slowly", "slithered", "southward"};
        QueueManager qWords = new QueueManager("Words", words);
        qWords.printQueue();

        // Create iterable Queue of Integers
        Object[] numbers = new Integer[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        QueueManager qNums = new QueueManager("Integers", numbers);
        qNums.printQueue();

        /*
        // Create iterable Queue of NCS Generics
        Animal.setOrder(Animal.KeyType.name);
        Alphabet.setOrder(Alphabet.KeyType.letter);
        Cupcakes.setOrder(Cupcakes.KeyType.flavor);
        // Illustrates use of a series of repeating arguments
        QueueManager qGenerics = new QueueManager("My Generics",
                Alphabet.alphabetData(),
                Animal.animalData(),
                Cupcakes.cupCakeData()
        );
        qGenerics.printQueue();

        // Create iterable Queue of Mixed types of data
        QueueManager qMix = new QueueManager("Mixed");
        qMix.queue.add("Start");
        qMix.addList(
                words,
                numbers,
                Alphabet.alphabetData(),
                Animal.animalData(),
                Cupcakes.cupCakeData()
        );
        qMix.queue.add("End");
        qMix.printQueue();
         */
    }
}
