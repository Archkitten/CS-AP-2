---
layout: default
---

# CSP

{% include csp_nav.html %}

## Week 5 - [Ticket](https://github.com/Archkitten/CS-AP-2/issues/17)

### Study Plan

MCQ1:
* Flagged Questions 23 and 24
* Flagged Question 39 (Parallel Processing)
* Flagged Question 46 (Open Protocols)

Review Topics:
* Parallel Processing

Plans:
* I think I'm ready for the AP Test, but any questions I guess on or get wrong on these MCQs, I'll record the overall topic.
* This week, the only topic I missed questions on was parallel processing, so I plan to go back to the CollegeBoard videos on specifically parallel processing.
* Other than that, I think I'm ready.

### Copy of MCQ 1

Score: 49/50

Question 39: A certain computer has two identical processors that are able to run in parallel. Each processor can run only one process at a time, and each process must be executed on a single processor. The following table indicates the amount of time it takes to execute each of three processes on a single processor. Assume that none of the processes are dependent on any of the other processes.

```
|---------|------------------------------------|
| Process | Execution Time on Either Processor |
|---------|------------------------------------|
| X       | 60 seconds                         |
| Y       | 30 seconds                         |
| Z       | 50 seconds                         |
|---------|------------------------------------|
```

Which of the following best approximates the minimum possible time to execute all three processes when the two processors are run in parallel?

* First processor handles X. 60 seconds.
* Seconds processor handles Y and Z. 30 + 50 = 80 seconds.
* Max time is 80 seconds.

### MCQ 2

Score: 49/50

Question 1: Which of the following best describes the ability of parallel computing solutions to improve efficiency?
* I chose: B
  * B) Any solution can be broken down into smaller and smaller parallel portions, making the improvement in efficiency theoretically limitless as long as there are enough processors available.
* Correct answer: D
  * D) The efficiency of a solution that can be broken down into parallel portions is still limited by a sequential portion.
* Technically B is correct, but D is the better answer because it applies to reality. Assuming one processor uses 6 seconds, two processors would take 3 seconds each. However, realistically you wouldn't use 1000 processors just to reduce that time down to 0.006 seconds.
