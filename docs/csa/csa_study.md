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
