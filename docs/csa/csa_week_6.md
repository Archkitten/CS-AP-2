---
layout: default
---

# CSA

{% include csa_nav.html %}

## Week 6 - [Ticket]

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
* [Logic]

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
