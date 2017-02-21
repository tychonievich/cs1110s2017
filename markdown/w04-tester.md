---
title: tester.py
...

# Task

Write a file named `tester.py` that contains a function named `is_median`
that tests another function to see if it correctly implements the `median` task defined in [last week's `averages` assignment](w03-averages.html).

As a reminder, the general structure of such a function is

````python
def is_median(func):
    if func(0, 0, 0) != 0:
        return False
    
    if func(1, 2, 3) != 2:
        return False
    
    # ...
    
    return True
````

# Example Invocations

When you run `tester.py`, nothing should happen.
It defines a function, it does not run it.

If in another file (which you do not submit) you write the following:

````python
import tester
import statistics

def second(a, b, c):
    return b

def correct(a, b, c):
    return statistics.median([a, b, c])

print(tester.is_median(second))
print(tester.is_median(correct))
````

you should get the following output:

````
False
True
````

# Grading

We have a lot of incorrect implementations of `median`;
for full credit, your function should be able to identify all of them as incorrect
(while still noting that correct ones are correct).

We won't create nasty cases, such as "it only fails if the second argument is 31284";
all the functions we'll run your code against will have the kinds of issues student-submitted code actually had.


# Thought Question

It is nice to know what test cases failed,
but we still want the main behavior of the program to be a True/False answer.

Try using `global`{.python} to have `is_median` accumulate a list of failed test cases in another variable,
maybe called `median_report` or the like.
For example, you might be able to get it so that

````python
print(tester.is_median(second))
print('-----------------------')
print(median_report)
````

prints something like

````
False
-----------------------
Failed 9 / 17 test cases; for example, 
    the median of (3, 1, 2) should be 2, not 1
````

There is a lot of room for making this report as pretty as you want.

Also, don't forget to re-set the report each time you invoke `is_median`.
We wouldn't want 

````python
print(tester.is_median(second))
print(tester.is_median(correct))
print(median_report)
````

to print the report of `second`'s failures after running `correct`.


# Troubleshooting

Consider *corner cases*: what as special arguments that have to be treated differently than others?
For example, "all arguments are the same" was a corner case.

Consider *equivalence classes*: what sets of arguments are likely to all have the same correctness?
For example, if `(2, 8, 9)` works then it is unlikely `(2, 9, 10)` will fail.

Consider such factors as

-   relationship between median and mean
-   which argument had the median value
-   negative numbers
-   repeated arguments


