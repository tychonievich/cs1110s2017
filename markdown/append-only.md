---
title: Append-only files
...

# Intro

There are several ways to keep information on a disk drive so you can store information between runs of a program.  For example, you can

-   Have a "save" action that writes the values of all important variables to a file in disk and a "load" action that reads those same values from disk.
-   Use a database, which is a program optimized for reading and writing small parts of large amounts of information to a disk.
-   Use an action log.
-   Re-write the entire file every time anything changes.

The [required assignment](w12-write.html) had you implement a re-write file; this writeup discusses the action log approach.


# Action-log files

The idea of an action log is that every time you change a value, you also write down that that change occured in a file.
When restarting the program you read the log and "replay" the actions, ending up with the same set of values you had when last you stopped running the program.
Action logs can use a bit more disk space than other ways of writing files, and they can take a bit longer to load, but they have various advantages too, including:

-   You can't forget to save: changing a variable changes the log.
-   They include an edit history and "un-do" information: every previous state of the program is represented by a prefix of the log.
-   Various accounting, sequentiality, and robustness properties we won't go into here.

You'll implement an action log in this assignment.

## Task

Have a set of functions that interact with a `dict` and a file.
Those that update the `dict` also write a history of that update to the file.
Those that read the file re-play those updates and return the resulting `dict`.

Your file should be a CSV file with three columns: action, key, and value.
Valid **action**s are `put` (corresponding to `d[key] = value`{.python})
and `del` (corresponding to `del d[key]`{.python}).
Valid **key**s are strings, but they should not contain commas `,` or newlines `\n` or `\r`.
Valid **values**s are strings, but they should not contain commas `,` or newlines `\n` or `\r`;
the **value** should be omitted for a `del` action.

An example action log CSV file might be

````
put,3,three
put,three,3
put,fvie,5
put,5,five
del,fvie
````

Replaying this log would give the `dict` `{'3': 'three', 'three': '3', '5': 'five'}`{.python}.

## Functions

Write the following functions.

-   `load(filename)` should
    
    1.  if the filename corresponds to a file on disk, read and replay the contents of the file to generate a `dict`; otherwise the `dict` should be `{}`.
    2.  open the given file in append-only mode.
    3.  return the `dict` and the opened file in a tuple.

-   `put(pair, key, value)`, where `pair` is a (dict, opened_file) tuple, should
    
    1.  check that `key` and `value` are legal (no commas or new-lines) and return `False` if they are not.
    2.  update the `dict` in `pair` to contain the given key:value pair.
    3.  write a `put` action line to the file in `pair`.  Use `print` with the option `flush=True` to ensure the write is committed to disk immediately.
    4.  return `True` if all actions succeeded.

-   `remove(pair, key)`, where `pair` is a (dict, opened_file) tuple, should

    1.  check that `key` is a key in the `dict` in `pair`
    2.  update the `dict` in `pair` to contain the given key:value mapping; and
    3.  write a `del` action line to the file in `pair`.  Use `print` with the option `flush=True` to ensure the write is committed to disk immediately.
    4.  return `True` if all actions succeeded.

-   `save(dict, filename)` should open the file, write a single `put` line for each key:value pair in the dict, then close the file.
    It should only print the keys and values that follow the rules (strings, no commas or newlines)
    and should return a list of the keys it was not able to write.

