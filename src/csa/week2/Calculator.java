package csa.week2;
import csa.util.Stack;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Calculator {

    // Key instance variables
    private final String expression;
    private ArrayList<String> tokens;
    private ArrayList<String> reverse_polish;
    private Double result;

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

    // Helper definition for supported operators
    private final Map<String, Integer> SEPARATORS = new HashMap<>();
    {
        // Map<"separator", not_used>
        SEPARATORS.put(" ", 0);
        SEPARATORS.put("(", 0);
        SEPARATORS.put(")", 0);
    }

    // Test if token is an operator
    private boolean isOperator(String token) {
        // find the token in the hash map
        return OPERATORS.containsKey(token);
    }

    // Test if token is an separator
    private boolean isSeperator(String token) {
        // find the token in the hash map
        return SEPARATORS.containsKey(token);
    }

    // Compare precedence of operators.
    private Boolean isPrecedent(String token1, String token2) {
        // token 1 is precedent if it is greater than token 2
        return (OPERATORS.get(token1) - OPERATORS.get(token2) >= 0) ;
    }

    // Create a 1 argument constructor expecting a mathematical expression
    public Calculator(String expression) {
        // original input
        this.expression = expression;

        // parse expression into terms
        this.termTokenizer();

        // are there variables? - Arch
        this.variableDetector();

        // place terms into reverse polish notation
        this.tokensToReversePolishNotation();

        // calculate reverse polish notation
        this.rpnToResult();
    }

    // Term Tokenizer takes original expression and converts it to ArrayList of tokens
    private void termTokenizer() {
        // contains final list of tokens
        this.tokens = new ArrayList<>();

        int start = 0;  // term split starting index
        StringBuilder multiCharTerm = new StringBuilder();    // term holder
        for (int i = 0; i < this.expression.length(); i++) {
            Character c = this.expression.charAt(i);
            if ( isOperator(c.toString() ) || isSeperator(c.toString())  ) {
                // 1st check for working term and add if it exists
                if (multiCharTerm.length() > 0) {
                    tokens.add(this.expression.substring(start, i));
                }
                // Add operator or parenthesis term to list
                if (c != ' ') {
                    tokens.add(c.toString());
                }
                // Get ready for next term
                start = i + 1;
                multiCharTerm = new StringBuilder();
            } else {
                // multi character terms: numbers, functions, perhaps non-supported elements
                // Add next character to working term
                multiCharTerm.append(c);
            }

        }
        // Add last term
        if (multiCharTerm.length() > 0) {
            tokens.add(this.expression.substring(start));
        }
    }

    // Detect variables, equals, and semicolons - Arch
    // Java String to Char Array: https://stackoverflow.com/questions/10006165/converting-string-to-character-array-in-java
    // ^ you probably don't need that because Tokenization already does it for you ^
    // Java Char to Int: https://beginnersbook.com/2019/04/java-char-to-int-conversion/
    private void variableDetector() {
        // If you see equals, calculate the terms afterwards? until the semicolon at least
        // Then somehow set the expression equal to the variable, store that somewhere
        // and if the variable comes up again, replace it with the expression
    }

    // Takes tokens and converts to Reverse Polish Notation (RPN), this is one where the operator follows its operands.
    private void tokensToReversePolishNotation () {
        // contains final list of tokens in RPN
        this.reverse_polish = new ArrayList<>();

        // stack is used to reorder for appropriate grouping and precedence
        Stack<String> tokenStack = new Stack<>();
        for (String token : tokens) {
            switch (token) {
                // If left bracket push token on to stack
                case "(":
                    tokenStack.push(token);
                    break;
                case ")":
                    while (tokenStack.peek() != null && !tokenStack.peek().equals("("))
                    {
                        reverse_polish.add( (String)tokenStack.pop() );
                    }
                    tokenStack.pop();
                    break;
                case "+":
                case "-":
                case "*":
                case "/":
                case "%":
                case "^":
                case "√":
                    // While stack
                    // not empty AND stack top element
                    // and is an operator
                    while (tokenStack.peek() != null && isOperator((String) tokenStack.peek()))
                    {
                        if ( isPrecedent(token, (String) tokenStack.peek() )) {
                            reverse_polish.add((String)tokenStack.pop());
                            continue;
                        }
                        break;
                    }
                    // Push the new operator on the stack
                    tokenStack.push(token);
                    break;
                default:    // Default should be a number, there could be test here
                    this.reverse_polish.add(token);
            }
        }
        // Empty remaining tokens
        while (tokenStack.peek() != null) {
            reverse_polish.add((String)tokenStack.pop());
        }

    }

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
                double c = 0;
                // IDE is trying to suggest: 'if' statement can be replaced with 'switch' statement
                if (i.equals("+")) {
                    c = a + b;
                }
                else if (i.equals("-")) {
                    c = a - b;
                }
                else if (i.equals("*")) {
                    c = a * b;
                }
                else if (i.equals("/")) {
                    c = a / b;
                }
                else if (i.equals("%")) {
                    c = a % b;
                }
                else if (i.equals("^")) {
                    c = Math.pow(b, a);
                }
                else {
                    c = 0;
                }
                // enhanced switch statement (suggested by IDE) doesn't work with Replit
                /*
                double c = switch (i) {
                    case "+" -> a + b;
                    case "-" -> a - b;
                    case "*" -> a * b;
                    case "/" -> a / b;
                    case "%" -> a % b;
                    case "^" -> Math.pow(b, a);
                    default -> 0;
                };
                */
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

    // Print the expression, terms, and result
    public String toString() {
        return ("Original expression: " + this.expression + "\n" +
                "Tokenized expression: " + this.tokens.toString() + "\n" +
                "Reverse Polish Notation: " +this.reverse_polish.toString() + "\n" +
                "Final result: " + String.format("%.2f", this.result));
    }
}
