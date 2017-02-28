---
title: On Testing
...


An important part of building software is testing it, ensuring it works and identifying its flaws.
The write-up describes a few basic aspects of testing.


# Test Cases and Suites

A **test case** is an example in which the correct behavior of the software is known,
generally one in which there is some expectation that some software might be incorrect.

The possible set of test cases is usually infinite, so *exhaustive* testing is not generally possible.
Even a simple function like `len` takes in a string, and there are infinitely many strings possible.
Who knows if `len('d&sdf78 Zdfg ')` won't be the one case that fails, even though `len('d&sdf78 Zdff ')` passed?

One option is proof: software has a mathematical basis, and it is possible to create proofs of correctness.
Proofs are little used, in part because they require more mathematical expertise of the programmer,
and will not be taught in this course for that reason as well.
If you are interested, one of the best-known projects to contain such proofs was [seL4](https://sel4.systems/Info/Docs/GD-NICTA-whitepaper.pdf).

More common is the adoption of a **test suite**, a set of test cases that we hope will discover a bug if a bug exists.
Selection of tests for test suites tends to be based on analysis of *equivalence classes* and *corner cases*, along with a few other techniques we won't cover.

To explore this more, we'll look at the `abs` function for finding absolute values.

## Equivalence Classes

If we assume that software was written by a normal non-malicious human,
we can probably assume they did not add extra code for the purpose of making their program break in strange ways.
This in turn generally means that they treat large swaths of inputs the same way.
These probably-the-same swaths are called *equivalence classes*.

For example, if `abs(8)`{.python} works then it is highly unlikely that `abs(9)`{.python} will fail.
This is because "positive integers" is a likely equivalence class for `abs`.

Equivalence classes vary by task.
For example, "positive integers" is probably *not* an equivalence class for `divided_by_2`,
but "even positive integers" might be.

It is good practice to try to split the entire space of inputs or arguments into equivalence classes,
such as

-   `int`{.python} arguments
    -   positive `int`{.python} arguments
    -   `0`{.python}
    -   negative `int`{.python} arguments
-   `float`{.python} arguments
    -   positive `float`{.python} arguments representing integers
    -   positive `float`{.python} arguments representing non-integers
    -   `0.0`{.python}
    -   negative `float`{.python} arguments representing integers
    -   negative `float`{.python} arguments representing non-integers
-   non-numeric arguments

In general, for each equivalence class you should

-   test each boundary of the class (e.g., for positive integers we'd test `1`)
-   test a random value from the middle of the class (e.g., for positive integers we might test `1138`)

## Corner cases

Sometimes there are special cases that might behave differently than others.
Examples include `abs(0)`{.python}, `math.tan(math.pi / 2)`{.python}, `len("")`{.python}, etc.

You should always test all of the corner cases if you can.

Sometimes cases that should break the program are also called corner cases;
for example, what should `abs("hi")` return?


# Function-testing-functions

In Python, function names without their parentheses are just variables,
and can be used to pass functions as arguments to other functions.
This enables us to create functions that test other functions

````python
def is_abs(func):
    # integers
    if func(0) != 0:
        return False
    if func(1) != 1:
        return False
    if func(1138) != 1138:
        return False
    if func(-1) != 1:
        return False
    if func(-3330) != 3330:
        return False
    
    # floating-point numbers
    if func(0.0) != 0.0:
        return False
    if func(-0.0001) != 0.0001:
        return False
    if func(0.0001) != 0.0001:
        return False
    ...
    
    return True

if is_abs(abs):
    print('build-in function abs passed all tests')
else:
    print('build-in function abs failed at least one test')

def my_abs(x):
    if x < 0:
        return -x
    return x

if is_abs(my_abs):
    print('my function my_abs passed all tests')
else:
    print('my function my_abs failed at least one test')


def bad_abs(x):
    if x < 1:
        return -x
    return x

if is_abs(bad_abs):
    print('my function bad_abs passed all tests')
else:
    print('my function bad_abs failed at least one test')
````

Functions that test other functions are just the first step into code that tests code;
Python comes with two more advanced tools ([unittest](https://docs.python.org/3/library/unittest.html) and [doctest](https://docs.python.org/3/library/doctest.html)),
which make use of some parts of the Python language we haven't discussed yet,
and entire companies has grown out of the need to even more advanced tools.


