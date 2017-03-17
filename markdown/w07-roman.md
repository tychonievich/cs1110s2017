---
title: roman.py
...

# Task

Write a file named `roman.py` that converts integers into roman numerals.


Given an integer larger than 0 and less than 4000, convert it to roman numerals.
You can find the rules for this at
[http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm](http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm),
or simply search for it online.

There are many ways to do this, some more efficient than others. If it
works and you wrote it yourself that's good enough.

If the integer they provide is not in the right range, print "Input must
be between 1 and 3999"


# Example Invocations


An example run of the program might look like:

    Enter an integer: 1997
    In roman numerals, 1997 is MCMXCVII

Another run might look like:

    Enter an integer: 5820
    Input must be between 1 and 3999


# Thought Question

There exist many solutions to this task.
Our reference solution is ten lines of code and uses lists.
How brief can you make your code?

Could you generalize your code to work with other values than 1, 5, 10, 50, 100, 500, and 1000?
For example, if the numbers were A:1, B:4, and C:16 then 30 would be CBCAA.
If you stick with the rule "at most one small value before a big value",
what is the set of numbers that results in the most compact representation?
(Obviously, don't submit code that uses different values)

# Troubleshooting

Most solutions involve building up the solution a letter or two at a time, using the `+` operator,
and keeping track of how far along you are by subtracting from the input as each new letter is added to the answer.

Most solutions we've seen use `while`{.python}, though some use `if`{.python} or `list`{.python}s instead or in addition to `while`{.python}.

