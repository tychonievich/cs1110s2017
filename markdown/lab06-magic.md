---
title: "Lab 6: Magic 8-Ball"
...

# Attendance

We will be taking roll in lab each week! Please come to your assigned lab to be counted present!

Each lab TAs are empowered to select their own method of taking roll.
Please follow your lab TA's instructions.  
They may dock points if you  are excessively late or leave unusually early.

# Pairing

For this and all subsequent labs, you will work in pairs.

# Recitation

The TAs will do a quick introduction to 

-   `import random`{.python}, `random.randrange(n)`{.python}, and Python's use of \[0, *n*\) intervals
-   The `startswith` method available for strings

... before the in-lab activity.


# Building a Fortune Teller

In this lab you will

1.  Write a function that returns random variations of yes/no answers.
2.  Write another function that takes a question as a parameter and returns a random answer.  It will also do a simple check to detect some kinds of non-yes/no questions and return a different answer for them.
3.  Write a program that uses the functions to answer questions.

As an enrichment activity, we'll also talk about how to make these graphical instead of console-based.

## Return a random string

Write a function that takes no argument and returns a random string that is a grammatically sound answer to a yes/no question.  `Yes` and `No` are obvious possibilities, but so are things like `Definitely`, `Wait and see`, `You won't like the answer`, etc.

There are many ways of doing this, but one of the most uniformly random is as follows.

````
generate a random integer between 0 and n (not including n)
if the random integer was 0,
    return the first answer option

generate a random integer between 0 and n-1 (not including n-1)
if the random integer was 0,
    return the second answer option

...

generate a random integer between 0 and 2 (not including 2)
if the random integer was 0,
    return the next-to-last answer option

return the last answer option
````

## Inspect a question

Write a function that takes as an argument a string representing a question.
Perform some basic checks to see if the string is unlikely to be yes/no; if it is, return some kind of `You were supposed to ask a yes/no question` message; otherwise invoke the function you wrote in the previous step.

Questions that begin with `Who`, `What`, `When`, `Where`, `Why`, or `How` are almost never yes/no questions.
Questions that begin with `Does`, `Is`, `Can`, or `Will` are usually yes/no questions.
You can add as many of these rules of thumb as you wish.

FYI, an educated guess like implemented in software is called a **heuristic**.

## Make it a program

Prompt the user to ask you a question.
Use your functions to get an answer and display it to the user.
If the answer is `not yes/no question`, use an `if`{.python} statement to ask for a second question and get a second answer.

## (Optional) Make it graphical

So far we've only used console programs, but Python also comes with a graphical user inteface (GUI) library pre-installed call `tkinter`.
GUIs require a bit of overhead to use, but if you want to here is a way to get started:





## Submission

**Each partner** should submit one .py file named `madlib.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **both partners' ids** in comments at the top of the file.

