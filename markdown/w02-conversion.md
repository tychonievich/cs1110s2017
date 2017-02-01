---
title: conversion.py
...

# Task

Write a file with two functions: `c2f` and `f2c`.
`c2f` should accept as a parameter a temperature in Fahrenheit and return the corresponding temperature in Celsius.
`f2c` should accept as a parameter a temperature in Celsius and return the corresponding temperature in Fahrenheit.

Neither function should `print`{.python} anything nor ask for any `input`{.python}.
You should not have any code outside of these two functions.

# Example Invocations

When you run `conversion.py`, nothing should happen.
It defines functions, it does not run them.

If in another file (which you do not submit) you write the following:

````python
import conversion

print(conversion.c2f(31))
print(conversion.c2f(100))
print(conversion.f2c(-40))
print(conversion.f2c(72))
````

you should get the following output:

````
87.8
212.0
-40.0
22.22222222222222
````

Don't worry if you are off in the last few decimal places
