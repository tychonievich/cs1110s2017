---
title: maydate.py
...

# Task

Write a file with one function: `creepy`.
`creepy` should have two arguments, the ages of two people.
It should return `False` if the two may date each other without being creepy, `True` otherwise.
See [dating.py](w01-dating.html) for a definition of creepy.

Note: it is possible to solve this problem using `if`, but that is not encouraged.
Consider the following example of how to return `True` or `False` without `if`:

````python
def between(x, y):
    '''returns True if x is bigger than y, False if it is not'''
    return x > y
````

Your function should neither `print`{.python} nor ask for any `input`{.python}.
You should not have any code outside of the function.

You may assume that we only invoke the function with the older age is in the second position.

# Example Invocations

When you run `maydate.py`, nothing should happen.
It defines a function, it does not run it.

If in another file (which you do not submit) you write the following:

````python
import maydate

print(maydate.creepy(18, 80))
print(maydate.creepy(50, 80))
````

you should get the following output:

````
True
False
````

# Question

We won't test it, but what does your code do if you pass in the older age first?

````python
print(maydate.creepy(22, 18))
print(maydate.creepy(31, 18))
````

How hard would it be to make it work for both age orders?
