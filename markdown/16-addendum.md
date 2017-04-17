---
title: More on File Writing
...

§[16](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.16) gives a useful overview of writing to files,
but we find that a few subjects it discusses could do with additional clarification,
and there are a few useful practices it omits to mention.

# Always use `with` when writing

§[16.2.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.16.2.3) mentions the use of the `with` keyword, but most of the example code in the chapter does not use it.
Using `with` is [safer and more robust](#more-on-buffering) than using `open`/`close`
and should be your default any time you plan to write to a file.

Thus, listing1606.py's file-writing part should be written as

````python
with open('pc_writetext.tmp', 'w') as fp:
    while True:
        text = input('Please enter a line of text: ')
        if text == '':
            break
        fp.write(text)
````

and listing1607.py's file-writing part should be written as

````python
with open(FILENAME, 'a') as fp:
    while True:
        text = input('Please enter a line of text: ')
        if text == '':
            break
        fp.write(text)
````


# `print` is usually better than `write`

It is often more convinient to use the built-in function `print` than the file method `write`.
`print` accepts an optional argument `file` which can be used to print to a file.

````python
with open(FILENAME, 'a') as fp:
    while True:
        text = input('Please enter a line of text: ')
        if text == '':
            break
        print('text =', text, file=fp)
````

Note that

1.  the `file=` argument must come after any arguments to be printed
2.  the `file=` argument must be an opened file, preferably using a `with` construct

`print` behaves the way you expect it would:
accepts multiple arguments of any type, puts spaces between them, and goes to a new line after each invocation.

For completeness, [`print` also has several other optional arguments](https://docs.python.org/3/library/functions.html#print):

-   `print(1, 2, 3, sep='☺')` will print `1☺2☺3\n` instead of the default `1 2 3\n`
-   `print(1, 2, 3, end='☺')` will print `1 2 3☺` instead of the default `1 2 3\n`
-   `flush` [is described below](#more-on-buffering).

# More on buffering

§[16.1.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.16.1.3) mentions buffering and flushing, as does [a footnote](http://www.spronck.net/pythonbook/pythonbook.pdf#Hfootnote.10) in §[16.10](http://www.spronck.net/pythonbook/pythonbook.pdf#section.16.10).
A bit more on this is worth understanding.

It is more efficient for computers to read and write files in large chunks than to read or write them in small chunks.
Because of that, Python will work with your operating system to try to turn all your small reads and writes into large reads and writes.

Conceptually, file writing might proceed something like this:

Code         | Python+OS buffer | Disk
-------------|------------------|------
`print(3, file=f)`{.python} | `"3\n"`{.python} | `""`{.python}
`print(4, file=f)`{.python} | `"3\n4\n"`{.python} | `""`{.python}
`print('some text', file=f)`{.python} | `"3\n4\nsome text\n"`{.python} | `""`{.python}
`print(6, file=f)`{.python} | `""`{.python} | `"3\n4\nsome text\n6\n"`{.python}
`print(7, file=f)`{.python} | `"7\n"`{.python} | `"3\n4\nsome text\n6\n"`{.python}
… | | 

The operating system can chose to flush its buffer to disk at any time, or not to do so.
However, four things force a flush to happen:

-   Invoking `f.close()`.

-   Exiting a `with` block, which implicitly calles `f.close()`.

    Note that `with` blocks are existed if there is an exeption too.
    The following code:

    ````python
    f = open('test.txt', 'w')
    print('did this appear?', file=f)
    x = 3 / 0
    f.close()
    ````
    
    does *not* guarantee that `test.txt` has anything written to it because there was a divide-by-zero exception before the `close` was called.
    However, the following code:

    ````python
    with open('test.txt', 'w') as f:
        print('did this appear?', file=f)
        x = 3 / 0
    ````
    
    *does* guarantee that `test.txt` has `did this appear?` written to it because existing a `with` via a divide-by-zero exception is still existing the `with`, and thus closes the file.

-   Invoking `f.flush()`.
    Unlike `close`, `flush` leaves the file open after ensuring the buffer is written to disk.

-   Using the `flush=True`{.python} optional argument of `print`, like `print(3, '+', 4, '=', 3+4, file=f, flush=True)`{.python}

Buffering also happens on file reads, but we won't see cases where that matters much in this course.
