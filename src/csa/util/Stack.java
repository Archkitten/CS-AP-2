package csa.util;

/**
 *  Implementation of Stack, using LinkedList (previous only).
 *  December 24, 2019
 * @author     John Mortensen
 *
 */
public class Stack<T>
{
    private LinkedList<T> lifo;  // last in first out Object of stack

    /**
     *  Constructor for the SinglyLinkedList object
     *  Generates an empty list.
     */
    public Stack()
    {
        lifo = null;
    }

    /**
     *  Returns the current (LIFO) objects value.
     *
     * @return  the current objects value in Stack.
     */
    public T peek()
    {
        if (lifo == null)
            return null;
        else
            return lifo.getData();
    }

    /**
     *  Inserts a new object at the top of this Stack,
     *
     * @param  value  is the database to be inserted at the top of the Stack.
     */
    public void push(T value)
    {
        // note the order that things happen:
        // the new object becomes current and gets a value
        // current lifo is parameter, it is assigned as previous node in lifo
        lifo = new LinkedList<T>(value, lifo);
    }

    /**
     *  Removes the top element in the Stack.  Garbage collection should destroy this element when needed.
     *
     */
    public T pop()
    {
        T value = null;

        if (lifo != null) {
            value = lifo.getData();
            lifo = lifo.getPrevious();
        }

        return value;
    }

    /**
     *  Returns a string representation of this Stack,
     *  polymorphic nature of toString overrides of standard System.out.print behavior
     *
     * @return    string representation of this list
     */
    public String toString()
    {
        StringBuilder stackToString = new StringBuilder("[");

        LinkedList<T> node = lifo;  				// start from the back
        while (node != null)
        {
            stackToString.append(node.getData()); 	// append the database to output string
            node = node.getPrevious();    		// go to previous node
            if (node != null)
                stackToString.append(", ");
        }										// loop 'till you reach the beginning
        stackToString.append("]");
        return stackToString.toString();
    }


}
