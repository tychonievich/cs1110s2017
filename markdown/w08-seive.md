---
title: seive.py
...

# Task

Write a function `primes` with a single argument `x`
that returns a list of all prime numbers less than `x`.
You may assume that `x` is an integer greater than 2.

2 is the smallest prime.
All larger primes are integers *x* such that for all prime numbers *y* smaller than *x*,
the remainder of *x* ÷ *y* is non-zero.

We recommend implementing some version of the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).
In particular,

1.  Have a list of primes, initially containing 2
1.  For each odd number (except 1), check if it is prime by finding the remainder of each number in the list of primes
    -   If *any* remainder was 0, the number is *not* prime
    -   If *all* remainders were non-0, add the number to the list of primes


# Example Runs

When you run `seive.py`, nothing should happen.
It defines a function, it does not run it.

If in another file (which you do not submit) you write the following:

````python
import seive
print(seive.primes(50))
many = seive.primes(12345)
print(many[-1])
````

you should get the following output quickly (in not more than a second or two):

````
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
12343
````


# Thought Questions

Once I know that 17 is not divisible by 2, 3, or 5
I don't have to check other numbers; if 17 was divisible by something larger than 5, it would also have to be divisible by something smaller than 17 ÷ 5 and thus something smaller than 5.
Generalizing this observation can dramatically speed up your code, allowing you to return 7-digit primes in reasonable time.

There are also many other [primality tests](https://en.wikipedia.org/wiki/Primality_test) which are more efficient than the above for checking single large numbers, though some are less efficient for creating lists of small prime numbers.


# Troubleshooting

You'll probably want a loop within a loop: the outer loop to consider possible primes, the inner loop to check possible factors of the currently-being-considered possible prime.

Many successful solutions have a variable named `prime_so_far` that is `True`{.python} until a factor is found, then it becomes `False`.

Don't add a prime to the list of primes until after you've checked *all* of its possible prime factors!
