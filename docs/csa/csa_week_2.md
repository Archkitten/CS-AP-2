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

[Youtube Video](https://www.youtube.com/watch?v=Wz85Hiwi5MY)
* Sorting the values within the Reverse Polish Notation arrayList
  * Is it an operator (+ - * / %)?
    * Is the existing operator of greater precedence?
      * Push to Stack
    * Else
      * Pop out operator underneath
      * Push to Stack
      * Push the popped operator back to Stack
  * Is it a seperator (" ")?
    * Skip it
  * Is it a number (1 2 3 4 5)?
    * Put it in a Queue

Result (Double):
```
4.0
27.0
13.0
108.0
```


### Challenge #1 + #2 + #4: RPN To Result, Power, Square Root
Calculator.java
```
public class Calculator {

    ...

    // Helper definition for supported operators
    private final Map<String, Integer> OPERATORS = new HashMap<>();
    {
        // Map<"token", precedence>
        OPERATORS.put("^", 2);
        OPERATORS.put("√", 2);
        OPERATORS.put("*", 3);
        OPERATORS.put("/", 3);
        OPERATORS.put("%", 3);
        OPERATORS.put("+", 4);
        OPERATORS.put("-", 4);
    }
    
    ...
    
    // Takes RPN and produces a final result
    private void rpnToResult()
    {
        // Stack used to hold calculation while process RPN
        Stack<String> calculation = new Stack<>();

        // for loop to process RPN
        for (String i : this.reverse_polish) {
            // If the token is a number
            if (isANumber(i)) {
                // Push number to stack
                calculation.push(i);
            }
            // else if square root
            else if (i.equals("√")) {
                // Pop the top entry
                double a = Double.parseDouble(calculation.pop());
                // Calculate square root
                double c = Math.sqrt(a);
                // Push result back to stack
                calculation.push(String.valueOf(c));
            }
            // else
            else {
                // Pop the two top entries
                double a = Double.parseDouble(calculation.pop());
                double b = Double.parseDouble(calculation.pop());
                // Based off of Token operator calculate result
                double c = switch (i) {
                    case "+" -> a + b;
                    case "-" -> a - b;
                    case "*" -> a * b;
                    case "/" -> a / b;
                    case "%" -> a % b;
                    case "^" -> Math.pow(b, a);
                    default -> 0;
                };
                // Push result back onto the stack
                calculation.push(String.valueOf(c));
            }
        }
        // Pop final result and set as final result for expression
        result = Double.parseDouble(calculation.pop());
    }

    private Boolean isANumber(String i) {
        try {
            Double.parseDouble(i);
            return true;
        }
        catch (Exception e) {
            return false;
        }
    }
    
    ...
}
```

CalculatorTester.java
```
Calculator expMath = new Calculator("2 * 5 ^ 2 * 2");
System.out.println("\nExponent Math\n" + expMath);

Calculator sqrtMath = new Calculator("√(60 + 4) * √4 ^ 2");
System.out.println("\nSquare Root Math\n" + sqrtMath);
```
