---
layout: default
---

# CSA

{% include csa_nav.html %}

## Self Study Guide

For Loop
```
for (int i = 0; i < 10, i++) {
    System.out.println("This will print out 10 times.")
    System.out.println("i goes from 0 to 9.")
}
```

Array
```
// Array of size 3:
int[] numberArray = new int[3]

// or
int[] numberArray = {0, 1, 2}
```

For Loop + Array
```
for (int i = 0; i < numberArray.length, i++) {
    // Print out each element of the array.
    System.out.println(numberArray[i]);
    // Print out each index of the array.
    System.out.println(i);
}
```

For Each Loop + Array
```
for (int i : array) {
    // Print out each element of the array.
    System.out.println(i);
}
```

Java Default Library: substring()
```
// Ok Imagine a String:
// "College Board"
// And visualize it as an array of characters:
// | C | o | l | l | e | g | e |   | B | o | a | r | d |
//   0   1   2   3   4   5   6   7   8   9   10  11  12

String.substring(1, 4)

// Would return: olle
// Because: | o | l | l | e |
//            1   2   3   4

// Single Parameter starts from 10th value
// and prints out everything after it.
String.substring(10)

// Would return: ard
// Because: | a | r | d |
//            10  11  12
```
