---
title: "Lab 9: Debugging"
...

# Attendance

We will be taking roll in lab each week! Please come to your assigned lab to be counted present!

Each lab TAs are empowered to select their own method of taking roll.
Please follow your lab TA's instructions.  
They may dock points if you  are excessively late or leave unusually early.

# Pairing or More

For this and all subsequent labs, you will work in pairs.

For this lab, you are also welcome to work alone or in groups of up to four people.

# Setup


## Overview

The goal of this lab is to practice debugging techniques.
It is also a chance to have you work with a larger code-base than the frequency of our assignments has let us have you create yourself thus far.
And it contains a use for the `dict`{.python} data-type we introduced this week.

## Debugging tips

As a reminder, debugging typically works as follows:

1.  Determine that there is a problem, typically by identifying a set of inputs that creates the wrong result.

2.  Discover where in the code the wrong behavior is introduced.  A general guide to doing this is

    -   Add `print`{.python} statements to help determine what is happening

    -   Include enough information to know if what is happening is what should happen, such as

        -   putting a `print`{.python} inside a control construct (`if`{.python}, `while`{.python}, or `for`{.python}) to see if you getting inside the control construct the expected number of times
        -   printing the value of variables to see if they are what you expect
        -   printing part of a subsequent expression to see if its parts are correct.  For example, if `fun[fun.index('keen') + 1] < 'nifty'`{.python} is doing the wrong thing, you might print `fun.index('keen')` to see if it is a sensible value.
    
    -   Narrow in on where the problem happened, using a variant of "binary search":
        
        1.  print before anything goes wrong and after you know something is wrong
        2.  print something about halfway between the other two prints
        3.  if the new print suggests things are working, you only need look after it; or if broken, you only need to look before it; either way, you've cut the region where the problem may have occurred in half)  
        4.  repeat steps 2 and 3, narrowing the region where the problem must have occurred in half again and again until you locate the problem
    
3.  Once you find the source of the problem, fix it.

## The code to debug

The program you are to debug is designed to

1.  Read a few public-domain books
2.  Identify which words appears "with" other words
3.  Ask the user for words of interest
4.  Tell the user which word frequently appears with their word of interest.

There are several nuances to how this is accomplished.

-   "with" is defined as "on the same line and within the same sentence"
-   we don't want super-common words like "a" to be identified for all words, so we take togetherness as `frequency_together / frequency_apart`{.python}
-   to better handle input that contains scripts or the like, we ignore multi-letter all-caps words
-   we strip off all boundary punctuation (i.e., `free,` becomes `free`) but not internal punctuation (i.e., `don't` remains `don't`).

# Task

Download the following files, all into the same folder (which should be your PyCharm project folder)

1.  [debug_task.py](files/debug_task.py) -- this contains broken code to be fixed
2.  [alice.txt](files/alice.txt) -- downloaded and slightly reformatted *Alice in Wonderland* from [Gutenberg.org](http://www.gutenberg.org/ebooks/11)
2.  [snark.txt](files/snark.txt) -- downloaded and slightly reformatted *The Hunting of the Snark* from [Gutenberg.org](http://www.gutenberg.org/ebooks/13)

Then debug and fix `debug_task.py`.
Some of the bugs are intentionally somewhat obscure… reading the comments and docstrings and working with others is encourged!

The code uses some parts of Python we have not taught you,
such as the `sort(key=bycount)`{.python} call on line 76 and the `word.strip(',;:-"[](){}<>/“”‘’_*')`{.python} on line 35.
We did not put bugs in these lines.
We also did lie in comments or docstrings.

## Test Cases

Once fully fixed, the following should be a possible run.

    What word are you interested in? speak
    "speak" often appears with "english"

    What word are you interested in? i
    "i" often appears with "think"

    What word are you interested in? thunk
    "thunk" does not appear in our corpus

    What word are you interested in? from
    "from" often appears with "being"

    What word are you interested in? being
    "being" often appears with "from"

    What word are you interested in? snark
    "snark" often appears with "place"

    What word are you interested in? place
    "place" often appears with "fireplace"

    What word are you interested in? 
     

Symptoms of the bugs may include

-   It crashes
-   It claims not to know a word that it should know
-   It gives an answer it shouldn't be able to give (violating some of the rules in the [The code to debug](#the-code-to-debug) section)
-   It gives a reasonable-seeming but wrong answer

The last kind of bug listed above is the hardest to debug.
You might need to read comments and docstrings and verify that code is doing what is says it is doing…



## Submission

**At least one partner** should submit one .py file named `debug_task.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **all partners' ids** in comments at the top of the file.
