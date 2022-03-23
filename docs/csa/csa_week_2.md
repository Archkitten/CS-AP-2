{% include navigation.html %}

# CSA

{% include csa_nav.html %}

## Week 2 - [Ticket](https://github.com/Archkitten/CS-AP-2/issues/5)

### (TPT) Study Group Challenge 2

Assignment:
1. Build a calculator to process expressions and ultimately change RPN to a calculation.
2. Build in Power of operator ^: 2 ^ 1 = 2, 2 ^ 2 = 4, 2 ^ 3 = 8
3. Extra credit. Build variable assignment and evaluation into your expressions (a = 2; a + 1).
4. Extra credit. Investigate Wikipedia article and pseudo code and try adding a SQRT(). Try building Pythagoras expression.

### [Tri 3: Tech Talk 2: Calculator](https://github.com/nighthawkcoders/nighthawk_csa/wiki/Tri-3:-Tech-Talk-2:-Calculator)

Math Symbols:
* PEMDAS, each operator has its own precedence (priority)
* Add exponent ^ operator with priority 5
```
// Helper definition for supported operators
    private final Map<String, Integer> OPERATORS = new HashMap<>();
    {
        // Map<"token", precedence>
        OPERATORS.put("*", 3);
        OPERATORS.put("/", 3);
        OPERATORS.put("%", 3);
        OPERATORS.put("+", 4);
        OPERATORS.put("-", 4);
    }
```

Math Original Expression (String):
```
2 + 2
4 * 6 + 3
5 + 1 * 8
(7 + 5) * 9
```

Tokenization (Array):
```
[2, +, 2]
[4, *, 6, +, 3]
[5, +, 1, *, 8]
[(, 7, +, 5, ), *, 9]
```

Reverse Polish Notation (Array, works well with Stack):
```
[2, 2, +]
[4, 6, *, 3, +]
[5, 1, 8, *, +]
[7, 5, +, 9, *]
```

[Youtube Video](https://www.youtube.com/watch?v=Wz85Hiwi5MY) - 3:00
* Sorting the values within the Reverse Polish Notation arrayList
  * Is it an operator (+ - * / %)?
    * Is the existing operator of greater precedence?
      * Do/Don't put in Stack?
      * Pop something?
    * Else?
      * Do/Don't put in Stack?
      * Pop something?
  * Is it a seperator (" ")?
    * Skip it
  * Is it a number (1 2 3 4 5)?
    * Put it in a Queue

Result (Double):
```

```


### Challenge #1: RPN To Result
Calculator.java
```
# rpnToResult()
# Code Snippet
```
