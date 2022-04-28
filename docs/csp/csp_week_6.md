---
layout: default
---

# CSP

{% include csp_nav.html %}

## Week 6 - [Ticket](https://github.com/Archkitten/CS-AP-2/issues/19)

### MCQ 1

Score: 48/50

Flagged Question 34: For which of the following situations would it be best to use a heuristic in order to find a solution that runs in a reasonable amount of time?
* What is a heuristic?
  * A) Appending a value to a list of  n  elements, which requires no list elements be examined.
  * B) Finding the fastest route that visits every location among  n  locations, which requires  n!  possible routes be examined.
  * C) Performing a binary search for a score in a sorted list of  n  scores, which requires that fewer than  n  scores be examined.
  * D) Performing a linear search for a name in an unsorted database of  n  people, which requires that up to  n  entries be examined.
* Luckily, I guessed the right answer of B. This is because A wasn't searching anything, and C and D are already using a search algorithm.
* So, what is a heuristic?
  * Google:
    * enabling someone to discover or learn something for themselves.
    * a heuristic process or method.
  * B is correct because the method for finding the fastest route is different per route, so an evolving algorithm or AI is required for this type of problem.

Question 6: Which of the following algorithms display all integers between 1 and 20, inclusive, that are not divisible by 3?
* I chose: A and C
  * C)
    * Step 1: Set x to 1.
    * Step 2: If x is divisible by 3, then do nothing; otherwise display x. 
    * Step 3: Increment x by 1.
    * Step 4: Repeat steps 2 and 3 until x is 20.
* Correct answer: A and D
  * D)
    * Step 1: Set x to 1.
    * Step 2: If x is divisible by 3, then do nothing; otherwise display x.
    * Step 3: Increment x by 1.
    * Step 4: Repeat steps 2 and 3 until x is greater than 20.
* The difference between the two answers is that C) says to repeat until x == 20, and D) says to repeat until x > 20. While C) still prints the correct result, it only looks at values from 1-19 because the loop terminates after setting x = 20 and checking it. D) will look at values from 1-20 because it will set x = 20, see that x !> 20, and run the loop one last time to detect the value of 20 before terminating once x == 21.

Question 11: The variable age is to be used to represent a person’s age, in years. Which of the following is the most appropriate data type for age?
* I chose: D
  * D) list
* Correct answer: B
  * B) number
* I accidentally saw 'list' as 'int' and picked it without a second thought. Whoops.