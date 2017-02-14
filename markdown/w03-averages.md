---
title: averages.py
...

# Task

Write a file named `averages.py` with several functions in it for computing averages of three values:

- `mean(a, b, c)`{.python} should compute the [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) of `a`, `b`, and `c`.
- `median(a, b, c)`{.python} should compute the [median](https://en.wikipedia.org/wiki/Median) of `a`, `b`, and `c`.
- `rms(a, b, c)`{.python} should compute the [root-mean-square](https://en.wikipedia.org/wiki/Root_mean_square) of `a`, `b`, and `c`.
- `middle_average(a, b, c)`{.python} should compute the mean, median, and rms of `a`, `b`, `c`; and then return the median of those three averages.

Additionally, you should implement your solution such that

- `rms` invokes `mean` once.
- `middle_average` invokes `mean` and `rms` once each and `median` twice.


# Example Invocations

(will be added soon)

# Thought Question

How often is each of the three averages the middle average?  Are any of them always larger or always smaller than the others?

Can you use default values to allow your functions to work if only two arguments are supplied?  To get you started, consider writing `def mean(a, b, c=None):`{.python}.  If you get those working, what about allowing four or five values?

(Note: there [is a way](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists) to have arbitrarily-long argument lists, but we won't discuss the `tuple`{.python} construct is uses for a few weeks yet.)

There are [many other averages](https://en.wikipedia.org/wiki/Average); if you want additional practice, see how many of them you can get working.


# Troubleshooting

Your `mean` function can be a single line, as all it is doing is math.

Your `median` function will probably need several `if`{.python} statements.

Did you test out your `median` when all three argument values are the same?

For `rms`, recall that <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ceaad50b7a0ae8ad64014319f138887ec5147f6c" title="square root means one-half power"/> and that the exponentiation operator in Python is `**`{.python}.

Find yourself tempted to copy the contents of one function into another one? Your should probably *invoke* the copied function instead of copying it.