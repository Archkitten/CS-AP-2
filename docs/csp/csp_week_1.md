{% include navigation.html %}

# CSP

{% include csp_nav.html %}

## Week 1 - [Ticket](https://github.com/Archkitten/CS-AP-2/issues/4)

### 5.3 Notes

* Computing Bias occurs when the people that make the machines are biased already.
* Let’s say someone makes a soap dispenser that detects skin color to dispense soap, but forgets about other skin colors. The end result is a biased soap dispenser that only gives soap to the creator, not at the fault of the soap dispenser, but of the person that created it.

### [Tri 3 TPT 1.0 Computing Bias 5.3](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3-TPT-1.0-Computing-Bias-5.3)

1. Does the owner of the computer think this was intentional?
* No.

2. If yes or no, justify you conclusion.
* It probably wasn't intentional, since nobody wants to purposefully develop a racism program.

3. How do you think this happened?
* The company developing the face-tracking software only used white people as a sample size, so once the computer learned to recognize white people, they stopped developing the program. As a result, personal bias and forgetting other races exist is the cause of this error.

4. Is this harmful? Was it intended to be harmful or exclude?
* This is harmful, but it wasn't intended to be.

5. Should it be corrected?
* After the issue was discovered, HP should correct it as soon as possible.

6. What would you or should you do to produce a better outcome?
* Producing a better outcome relies on the individual to keep in mind their own biases and try and prevent them from entering programs they create.

### 5.4 Notes

* Public Data Sets
  * IOC-1.E.1
    * Widespread access to information and public data facilitates the identification of problems, development of solutions, and dissemination of results.
* Distributed Computing
  * Donate spare computing power to help calculations!
* Innovations made possible with crowdsourcing
  * Spotify
    * Collaborative Playlists
    * Algorithm
    * Metadata write-in
  * Crowdfunding
    * Kickstarter
    * IndieGoGo
    * Patreon
  * Blockchain
    * Cryptocurrency
    * Other tokens - Concert tickets
    * N F T s >:(

### [Tri 3 TPT 1.1 Crowdsourcing 5.4](https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-3-TPT-1.1-Crowdsourcing--5.4)

1. CompSci has 150 principles students. Describe a crowdsource idea and how you might initiate it in our environment?
* A crowdsource idea could be something like announcing to a bunch of students, telling them to gather data on something like how much trash is usually left out at lunch.

2. What about Del Norte crowdsourcing? Could your final project be better with crowdsourcing?
* The final project would be better with crowdsourcing, allowing many people to run the program and save their own data on the website.

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
* Create InfoDB List
* Iterate through a python list in three different ways:
  * For Loop
  * While Loop
  * Recursion
* Fibonacci
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
