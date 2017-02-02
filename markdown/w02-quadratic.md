---
title: quadratic.py
...

# Task

Write a file named `quadratic.py` with a function named `big_root` which, if given (a, b, c), returns the more positive root of the quadratic equation 

> a *x*^2^ + b *x* + c = 0

Use the [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula) to solve this problem.

Also write a second function, `small_root`, which gives the other root of the equation.

You may assume we only give coefficients for which the answer is a real number.

Neither function should `print`{.python} anything nor ask for any `input`{.python}.
You should not have any code outside of these two functions.

# Example Invocations

When you run `quadratic.py`, nothing should happen.
It defines a function, it does not run it.

If in another file (which you do not submit) you write the following:

````python
import quadratic

print(quadratic.big_root(1, -1, -1))
print(quadratic.small_root(1, -1, -1))
````

you should get the following output:

````
1.618033988749895
-0.6180339887498949
````

(don't worry if your answer differs in the last few digits)

# Thought Question

We won't grade this, but what does your code do when you try to solve an equation with no real solutions?

````python
print(quadratic.big_root(1, 1, 1))
````

If you want, feel free to also add [the cubic formula](https://math.vanderbilt.edu/schectex/courses/cubic/) or even (if you feel really ambitious) [the quartic formula](https://en.wikipedia.org/wiki/Quartic_function#General_formula_for_roots),
but [there isn't a quintic formula](https://en.wikipedia.org/wiki/Abel%E2%80%93Ruffini_theorem).

# Troubleshooting

Recall that <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ceaad50b7a0ae8ad64014319f138887ec5147f6c" title="square root means one-half power"/>.

Don't remember the operators you need?  See &sect;3.3.1.  Also, remember that in Python `^`{.python} is *not* the exponentiation operator (we won't cover what `^`{.python} is; if you are curious, see &sect;19.2.5).

Did you get the order of operations right?  You could look them up, but adding parentheses never hurts.

There are two roots (because of the &plusmn; in the quadratic formula), but one of them is always the biggest&hellip; no need for an `if`{.python}

Have you tried other coefficients besides `(1, -1, -1)`{.python}?

