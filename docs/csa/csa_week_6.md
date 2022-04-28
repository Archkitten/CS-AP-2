---
layout: default
---

# CSA

{% include csa_nav.html %}

## Week 6 - [Ticket](https://github.com/Archkitten/CS-AP-2/issues/18)

### 2020 Practice Exam 1 MCQ

Question 6: Which of the following expressions evaluate to 3.5 ?
1. (double) 2 / 4 + 3
2. (double) (2 / 4) + 3
3. (double) (2 / 4 + 3)

* I chose: E
  * I, II, and III
* Correct answer: A
  * Only I
* For I:
  * (double) 2 / 4 + 3
  * 2.0 / 4 + 3
  * 0.5 + 3
  * 3.5
* For II:
  * (double) (2 / 4) + 3
  * (double) (0) + 3
  * 0.0 + 3
  * 3.0
* For III:
  * (double) (2 / 4 + 3)
  * (double) (0 + 3)
  * (double) (3)
  * 3.0
* I had a fundamental misunderstanding of when the values got cast to double.

Question 7: Consider the following code segment.
```
int num = /* initial value not shown */;
boolean b1 = true;
if (num > 0) {
    if (num >= 100) {
        b1 = false;
    }
}
else {
    if (num >= -100) {
        b1 = false;
    }
}
```
Which of the following statements assigns the same value to b2 as the code segment assigns to b1 for all values of num?
* I chose: A
  * boolean b2 = (num > -100) && (num < 100);
* Correct answer: E
  * boolean b2 = (num < -100) || (num > 0 && num < 100);
* Test cases:
  * -200 evaluates to true (bypass 1st if, 3rd else: b1 not set to false)
  * -50 evaluates to false (bypass 1st if, 3rd else: b1 set to false)
  * 50 evaluates to true (1st if, 2nd if: b1 not set to false)
  * 200 evaluates to false (1st if, 2nd if: b1 set to false)
* I just didn't have enough time to read and 'test case' this problem carefully. Time pressure.

Question 9: Consider the following code segment.
```
ArrayList<Integer> numList = new ArrayList<Integer>();
numList.add(3);
numList.add(2);
numList.add(1);
numList.add(1, 0);
numList.set(0, 2);
System.out.print(numList);
```
What is printed by the code segment?
* I chose: A
  * [1, 3, 0, 1]
* Correct answer: B
  * [2, 0, 2, 1]
* Logic:
  * [3]
  * [3, 2]
  * [3, 2, 1]
  * [3, 0, 2, 1]
  * [2, 0, 2, 1]
* I misunderstood .add() and .set(). numList.add(1, 0) will add a "0" before index 1, instead of adding a "1" before index 0.

Question 10: Consider the following method.
```
public static void printSome(int num1, int num2) {
    for (int i = 0; i < num1; i++) {
        if (i % num2 == 0 && i % 2 == 0) {
            System.out.print(i + " ");
        }
    }
}
```
Which of the following method calls will cause "0 10 " to be printed?
* I chose: C
  * printSome(10, 5)
* Correct answer: D
  * printSome(20, 5)
* printSome() will print all even numbers that are a multiple of num2 AND less than num1.
* My incorrect answer printSome(10, 5) will only print "0 " because 10 (desired result) is not less than 10 (num1).

Question 12: Which of the following can replace /* missing condition */ so that the printDetails method CANNOT cause a run-time error?
```
borrower is a variable of Book Class
data type of borrower is Person (custom class)
```
1. !borrower.equals(null)
2. borrower != null
3. borrower.getName() != null

* I chose: A
  * I only
* Correct answer: B
  * II only
* If borrower hasn't been defined yet, using .equals() will return an error despite being a Person data type. Use != instead.

Question 13: Assume that a, b, and c are boolean variables that have been properly declared and initialized. Which of the following boolean expressions is equivalent to !(a && b) || c?
* I chose: B
  * a \|\| b \|\| c
* Correct answer: E
  * !a \|\| !b \|\| c
* De Morgan's Law. !(a && b) is equivalent to !a \|\| !b.
* Ugh. I blame this on time constraints. I used to be so good at these types of problems!

Question 14: The following categories are used by some researchers to categorize zip codes as urban, suburban, or rural based on population density.
* An urban zip code is a zip code with more than 3,000 people per square mile. 
* A suburban zip code is a zip code with between 1,000 and 3,000 people, inclusive, per square mile. 
* A rural zip code is a zip code with fewer than 1,000 people per square mile.

I.
```
String cat;
if (density > 3000) {
    cat = "urban";
}
else if (density > 999) {
    cat = "suburban";
}
else {
    cat = "rural";
}
return cat;
```

II.
```
String cat;
if (density > 3000) {
    cat = "urban";
}
if (density > 999) {
    cat = "suburban";
}
cat = "rural"; 
return cat;
```

III.
```
if (density > 3000) {
   return "urban";
}
if (density > 999) {
   return "suburban";
}
return "rural";
```

* I chose: A
  * I only
* Correct answer: D
  * I and III only
* III is the most direct answer to the question, returning urban above 3000 density, then returns suburban above 1000 density, and returns rural otherwise.
* I didn't see the return statements inside III, and thought a variable was being set to urban and suburban. So I concluded it would return rural each time, and dismissed III as a possible correct answer. Oops.

Question 27: Consider the following statement. Assume that a and b are properly declared and initialized boolean variables.
```
boolean c = (a && b) || (!a && b);
```
Under which of the following conditions will c be assigned the value false?
* I chose: B
  * Never
* Correct answer: E
  * When b has the value false
* CollegeBoard response: When b has the value false, both of the expressions (a && b) and (!a && b) evaluate to false, regardless of the value of a. The entire expression evaluates to false \|\| false, or false. When b has the value true, one of the expressions (a && b) or (!a && b) evaluates to true. The entire expression, in this case, is either true \|\| false or false \|\| true, or true. A truth table can be used to summarize these results.
* Next time I'll use a truth table to use test cases. I blame time pressure part 2.

Question 28: Consider the following method.
```
public static String abMethod(String a, String b) {
    int x = a.indexOf(b);
    while (x >= 0) {
        a = a.substring(0, x) + a.substring(x + b.length());
        x = a.indexOf(b);
    }
    return a;
}
```
What, if anything, is returned by the method call abMethod("sing the song", "ng")?
* I chose: C
  * "si the song"
* Correct answer: B
  * "si the so"
* The method will take the first parameter as a string and remove any instances of the second parameter from the string.
* I was originally going to pick B, and I can't remember the reason why I switched to C.

Question 31: Consider an integer array nums, which has been properly declared and initialized with one or more values. Which of the following code segments counts the number of negative values found in nums and stores the count in counter?

I.
```
int counter = 0;
int i = -1;
while (i <= nums.length - 2)
{
   i++;
   if (nums[i] < 0)
   {
      counter++;
   }
}
```

II.
```
int counter = 0;
for (int i = 1; i < nums.length; i++)
{
   if (nums[i] < 0)
   {
      counter++;
   }
}
```

III.
```
int counter = 0;
for (int i : nums)
{
   if (nums[i] < 0)
   {
      counter++;
   }
}
```

* I chose: E
  * I, II, and III
* Correct answer: A
  * I only
* II is wrong because the for loop starts at i = 1, causing the 0th element of the array (nums[0]) to be skipped.
* III is wrong because a for each loop measures the element itself, not the index number. No need to call the array again.
* I'm such an idiot! I even knew about III's critical concept, reviewed it the night prior, AND put it in the study guide! I must have chosen E out of time pressure, or I didn't read the code carefully enough.

Question 33: Consider the following code segment.
```
String[][] letters = /* array implementation not shown */;
// A B C D
// E F G H
// I J K L

for (int col = 1; col < letters[0].length; col++) {
    for (int row = 1; row < letters.length; row++) {
        System.out.print(letters[row][col] + " ");
    }
    System.out.println();
}
```
What is printed as a result of executing this code segment?
* I chose: D
  * F G H
  * J K L
* Correct answer: E
  * F J
  * G K
  * H L
* They switched up the normal row-column nested for loop for a column-row one! \>:(

Question 38 - 40:
* Out of time, guessed B on all of them and got none right.
