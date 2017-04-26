---
title: Python functions and methods you should know
...

This document attempts to list the built-in functions, methods, and types that we expect every student will know well enough to ask about on exams.

Various operators (like `**`{.python} and `[i1:i2]`{.python}) are not included on this list, nor are control constructs like `for`{.python} and `def`{.python}, but students are still expected to know them.

# Exam 1

-   [how to fill in TPEGS footers](http://cs1110.cs.virginia.edu/lab05-paper.html#TPEGS)
-   `len(collection)`{.python}
-   `str(value)`{.python}
-   `int(value)`{.python}
-   `float(value)`{.python}
-   `print(things, to, be, displayed)`{.python}
-   `input(prompt)`{.python}
-   `type(value)`{.python}
-   [other exam 1 topics](http://cs1110.cs.virginia.edu/lab05-paper.html#things-we-expect-you-to-know)

# Exam 2

Since exam 1, we have covered

-   Boolean values (`True`{.python} and `False`{.python}) and operators (`and`{.python}, `or`{.python},  and `not`{.python})
-   Test case selection and debugging strategies
-   Loops (`while`{.python}, `for`{.python})
-   Collection types (`str`{.python}, `list`{.python}, `tuple`{.python}, `range`{.python})
-   The basics of the `dict`{.python} datatype
-   Reading files and web sites
-   Reading tabular data (such as CSV)

In general, we find questions directly about `tuple`{.python}, test case selection, and debugging strategies do not fit well into our exams.  However, the underlying concepts may appear in some way.  We typically intentionally test all other topics.

We expect you to know the following built-in and library functions:

-   `import random`{.python}
    -   `random.randrange(lo, hi)`{.python}
    -   `random.shuffle(list)`{.python}
-   `str`{.python}
    -   `substring in string`{.python}
    -   `string1 + string2`{.python}
    -   `string.lower()`{.python}
    -   `string.upper()`{.python}
    -   `string.strip()`{.python}
    -   `string.split()`{.python}
    -   `string.split(delimiter)`{.python}
    -   `string.find(substring)`{.python}
-   `list`{.python}
    -   `element in lst`{.python}
    -   `lst.append(value)`{.python}
    -   `lst.insert(index, value)`{.python}
    -   `lst.remove(value)`{.python}
    -   `del lst[index]`{.python}
    -   `lst.sort()`{.python}
    -   `lst.reverse()`{.python}
    -   `lst.index(element)`{.python}
-   `list(collection)`{.python}
-   `range(end)`{.python}
-   `range(start, end)`{.python}
-   `range(start, end, step)`{.python}
-   `dict`{.python}
    -   `mapping.keys()`{.python}
    -   `mapping.values()`{.python}
    -   `mapping.items()`{.python}
-   `open(filename)`
    -   `connection.read()`{.python}
    -   `connection.readline()`{.python}
    -   some way of iterating lines (`connection.readlines()`{.python}, or `connection.read().split('\n')`{.python}, or `for line in connection`{.python})
-   `import urllib.request`
    -   `urllib.request.urlopen(url)`{.python}
    -   `stream.read().decode('utf-8')`{.python}

# Exam 3

-   `try:`{.python}/`except:`{.python}
-   `import pygame, gamebox`{.python}
    -   `box1.touches(box2)`{.python}
    -   `box1.move_to_stop_overlapping(box2)`{.python}
    -   `box1.move_both_to_stop_overlapping(box2)`{.python}
    -   `camera.draw(box)`{.python}
    -   `camera.display()`{.python}
    -   `timer_loop(ticks_per_second, ticks)`{.python} and the basics of how to write a `ticks` function, including
        -   `ticks`'s argument is a collection of the keys beign pressed
        -   `ticks` is invoked by gamebox many times ever second
-   `import re`{.python}
    -   `re.compile(r'...')`{.python}, including the use of `[]`, `()`, `+`, `*`, and `?`
    -   `compiled_re.sub(replacement, text)`{.python}, including the use of `\1` and the like
    -   `compiled_re.search(text)`{.python}
    -   `compiled_re.finditer(text)`{.python}
    -   `match.group()`{.python}
    -   `match.group(n)`{.python}
    -   `match.groups()`{.python}
-   `import os.path`{.python}
    -   `os.path.exists(filename)`{.python}
-   `open(filename, 'w'){.python}
-   `with open(...):`{.python}
-   `print(..., file=f)`{.python}
-   debugging strategies
-   everything from listed for exams [1](lab05-paper.html) and 2
