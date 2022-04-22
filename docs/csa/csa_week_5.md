---
layout: default
---

# CSA

{% include csa_nav.html %}

## Week 5 - [Ticket](https://github.com/Archkitten/CS-AP-2/issues/15)

### Plan

<table>
    <tr>
        <th>Day</th>
        <td>Things to Review</td>
    </tr>
    <tr>
        <td>Monday</td>
        <td>
            1. Study Java syntax for for-loops.
            <br>
            2. Review Array and ArrayList syntax differences.
            <br>
            3. Increase speed for MCQs on conditional, looping, and recursive problems.
            <br>
            4. Practice writing code on paper (No IDE or W3 schools syntax help).
            <br>
            5. Watch out for super() class calls.
            <br>
            6. Unit 9 MCQ Question 3 is tricky. Review it over and over again, so I don't get tricked in the future.
        </td>
    </tr>
    <tr>
        <td>Tuesday</td>
        <td>
            7. Review Truth Tables and De Morgan's Law.
            <br>
            8. Memorize how java default libraries like substring() work.
            <br>
            9. Study how java for-each loops work with arrays (2015 MCQ Question 22).
            <br>
            10. Be careful when the inner nested for loop sets it's starting/stopping point based on the value of the outer for loop.
        </td>
    </tr>
    <tr>
        <td>Wednesday</td>
        <td>
            Questions Missed: None!
            <br>
            Questions Unanswered: 23, 26 and onwards.
            <p>
                Question 26: E
                <br>
                The changeIt() method isn't doing anything because there is no return type. Therefore, the start() method will print out 1 2 3 4 5 6 blackboard.
            </p>
            <p>
                Question 27: B
                <br>
                The sort is a selection sort. 1st pass: 6 and 1 get swapped. 2nd pass: 3 and 2 get swapped. 3rd pass: 3 and 5 don't get swapped. End result is 1 2 3 5 4 6.
            </p>
            <p>
                Question 28: B
                <br>
                The sort is a selection sort. It'll compare 15 times because 5 + 4 + 3 + 2 + 1. It'll swap 5 times because there are 5 pairs available to swap (5 iterations happen).
            </p>
            <p>
                Question 29: A
                <br>
                3 returns 1, 40 returns 1+1=2, 100 returns 1+1+1=3, 564 returns 1+1+1=3. It's just the number of digits.
            </p>
            <p>
                Question 30: B
                <br>
                (II) only. (I) and (III) always runs the code for 0-4 boxes.
            </p>
            <p>
                Question 31: E
                <br>
                The two starting points for X's are (1, 0) and (3, 0). Then keep creating X's one row down and one column over. So from (1, 0) the next X's would be (0, 1), and from (3, 0) the next X's would be (2, 1), (1, 2), and (0, 3).
            </p>
            <p>
                Question 32: B
                <br>
                B is the only one that correctly uses getters, treats k as an element and not as an index number, and doesn't have syntax errors.
            </p>
        </td>
    </tr>
    <tr>
        <td>Thursday</td>
        <td>
            <img src="../assets/images/Week_5_FRQ1.JPG" alt="Image Preview" width="425" height="550">
            <img src="../assets/images/Week_5_FRQ2.JPG" alt="Image Preview" width="425" height="550">
        </td>
    </tr>
    <tr>
        <td>Friday</td>
        <td>
            <p>
                Question 33: E
                <br>
                All three functions work. (I)'s Integer.MIN_VALUE sets the max to the lowest possible value beforehand, and (II) and (III) both set their max to the first index of the array.
            </p>
            <p>
                Question 34: D
                <br>
                A and C's expression use the array length minus one, which is incorrect because the for loop stopping condition is <, not <=. D is correct because the condition is when k is at the end of the array, this makes sense because we don't want to add a comma to the last word.
            </p>
            <p>
                Question 35: C
                <br>
                Binary search will get 5 as the index value of the first "8" found.
            </p>
            <p>
                Question 36: D
                <br>
                Binary search 2000 values is 2^11.
            </p>
            <p>
                Question 37: E
                <br>
                (II) is correct, prints out from the end of the array to 2. (III) reverses the array first, then prints out from front to 2, so it is also correct.
            </p>
            <p>
                Question 38: C
                <br>
                k is the counter counting the number of times v == nums[numVals - 1].
            </p>
            <p>
                Question 39: C
                <br>
                Apparently ArrayList's .set() function will return the value that it was trying to replace. So Alice Bob Carl will print out in the first for loop while everything gets set to Alex, so the second for loop prints out Alex Alex Alex.
            </p>
            <p>
                Question 23: C
                <br>
                j = 1
                <br>
                k j _ _ _
                <br>
                Input: 5 4 3 2 1
                <br>
                Output: 5 5 3 2 1
                <br>
                (k = -1 so while loop breaks out)
                <br>
                Final Result of (j = 1): 4 5 3 2 1
                <br>
                j = 2
                <br>
                _ k j _ _
                <br>
                Input: 4 5 3 2 1
                <br>
                Output: 4 5 5 2 1
                <br>
                k _ j _ _
                <br>
                Input: 4 5 5 2 1
                <br>
                Output: 4 4 5 2 1
                <br>
                (k = -1 so while loop breaks out)
                <br>
                Final Result of (j = 2): 3 4 5 2 1
            </p>
        </td>
    </tr>
</table>

### Self Study Guide

<a href="https://archkitten.github.io/CS-AP-2/csa/csa_study_guide" class="btn">Study Guide</a>
