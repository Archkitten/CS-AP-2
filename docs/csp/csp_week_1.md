{% include navigation.html %}

# CSP

{% include csp_nav.html %}

## Week 1

### 5.3 Notes

Notes

### [Tri 3 TPT 1.0 Computing Bias 5.3](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3-TPT-1.0-Computing-Bias-5.3)

GitHub Actions

### 5.4 Notes

Notes

### [Tri 3 TPT 1.1 Crowdsourcing 5.4](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3-TPT-1.1-Crowdsourcing--5.4)

GitHub Actions

### [Tri 3 TT1 Data Structures](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3-TT1---Data-Structures)

Categories of Data:
* Primitive Data Type - int, Boolean, String, etc.
* Collection Data Structure - Lists, Dictionary, etc.

List:
```
my_list = []
my_list.append("Hello!")

print(len(my_list))
# Result: 1

my_list.remove(0)
```

InfoDB Lists:
```
InfoDB = []

InfoDB.append({"P1": "Blob", 
               "P2": "Drip", 
               "P3": "Ro"})
```

Assignment (InfoDB Loops):
* Iterate through a python list in three different ways:
* For Loop
* While Loop
* Recursion
```
# for loop iterates on length of InfoDB
def for_loop():
    for n in range(len(InfoDB)):
        print_data(n)
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDB):
        print_data(n)
        n += 1
    return
```

Fibonacci:
* Fibonacci is a process that requires iteration, as the following value requires the two previous values to appear.
* Therefore, getting the next value in a Fibonacci sequence requires constant iteration.
