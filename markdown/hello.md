---
title: PyCharm vs IDLE
...

# Of Languages and Editors

Human speak various languages (English, Swahili, Mandarin, etc) and can compose documents in these languages using various programs (TextEdit, Word, Google Docs, etc).
Some programs are able to help people write in some languages, having spell check, grammar check, thesauri, etc., but even the nicest program does not remove the need to know the language you are writing.

The same holds true with languages computers speak (Python, C, LISP, etc)
and the programs (called "editors") we use to compose documents in these languages (PyCharm, Idle, Eclipse, etc).
Our primary text uses the **Python 3** language and the **IDLE** editor.
We will use the same language (**Python 3**) but a different editor (**PyCharm**).
This page describes how to translate from one to the other.

PyCharm has a lot of spell-check-like features for the Python language, but to make all of those work properly requires both some one-time set-up and you to use it the way it works best.

# Using PyCharm Well

On most computers, PyCharm can be used to open files: you double-click on a `.py` file and PyCharm opens it.  But this is **not** the way PyCharm is designed to be used.

PyCharm works best if you

- Run the Pycharm application.
- Create a "Project", which is a collection of Python files.  We suggest having just one project during this entire course, probably named something like "CS 1110" or "Introduction to Programming" (though you can name it "yesterday's anticipation" or anything else you like).
- From inside PyCharm with that project opened, open the files you want to edit. 

This may seem counter-intuitive at first, but it will help streamline your work later on.

# Setting Up PyCharm

There's a little work you need to do up front to make PyCharm work optimally all semester.

## Tell Pycharm how to run programs

1. In the *File* (or *PyCharm*) menu, select "Default Settings"
2. In the left-hand pane, select "Project Interpreter"
3. At the top of the right-hand pane, in the drop-down menu pick the largest "3.*something*" number available (likely 3.6.0, but anything beginning 3 will work).
4. Click "OK" to close the default settings window

## Install Pillow

1. In the very bottom-right corner of the PyCharm window is  a little grey box-shaped icon.  Clicking it will toggle the visibility of some extra options.  Right above it should be several small icons with text adjacent to them.  Make sure both "Python Console" and "Terminal" are visible.
1. Press the "Python Console" icon; a window containing a few lines of text and a line with `>>>` in it will show up.
    1.  Verify that the second line says "Python 3.*something*"; if not, ask a TA for help.
    1.  The first line should begin with a directory path, something like `/usr/bin/python3.6` or `/Volumes/HD5/Python/bin/python3.5` or `C:\Users\student\AppData\Local\Python36\lib\bin\python3.exe`; this will be followed by a space and another path.
        Copy the first path up to and including the last slash; for example, if it is `/usr/bin/python3.4` copy `/usr/bin/`.
1.  Press the "Terminal" icon; a window containing a single line of text and a blinking cursor should show up.
    1. paste what you copied in the last step; then, without a space in between, add `pip3` (and, if you are on Windows, `.exe`) to get something like, e.g., `/usr/bin/pip3` or `C:\Python36\bin\pip3.exe`
    2. after `pip3` (or `pip3.exe`) enter a space, the word `install`, another space, and the word `pillow`, like
    
        ````bash
        /usr/bin/pip3 install pillow`
        ````
        
        then press enter.  Several lines should be displayed, ending with a message like `Successfully installed pillow`


# Understanding the Book

When the book talks about

IDLE
:   We'll use PyCharm instead

"Python Shell"
:   We'll use PyCharm's "Python Console" instead; see [the pevious section](#install-pillow) for how to access the Python Console.



