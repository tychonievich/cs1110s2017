---
title: "Lab 11: Installing Gamebox - TA Guide"
...

# Running the Lab

This lab is optional.  They do not need to sign in.

# Windows specific troubleshooting

In step 5, if they have a problem with the substeps `a.`--`c.`, try the second step `a.` first.
In theory this will work for most students, but it is a new feature and we haven't tried it with very many students yet.

If they get an error message on substep `c.`, they might have any of the following problems:

-   They might not have downloaded the `.whl` file to the correct directory.  It should be in the same directory as their `.py` files.
-   They have the wrong version of Python selected as their project interpreter.  To check for this, and change it if it is the problem, 
    -   File → Settings (opens a new window)
    -   On the left menu, under **Project: *project-name***, select Project Interpreter
    -   In the drop-down, it should say "3.6.1".  If not,
        -   Select 3.6.1 if present
        -   If not present, go to <http://python.org>, re-download and re-install Python.
            Download the 64-bit version.
-   They might have a 32-bit version of Windows.
    The chance of this is very low, but if they do you can get the appropriate `.whl` file from <http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame>

# OS X specific troubleshooting

It takes some time to do all the steps.  This is expected.

Some students have several versions of Python on their computer, with the command line using one and PyCharm using another.
This will result in every installation step working without an error, but PyCharm being unable to run `gamebox.py` when they are done.
To fix it,

-   In the terminal type `python3 --version` and note the output
-   In PyCharm,
    -   PyCharm → Settings (opens a new window)
    -   On the left menu, under **Project: *project-name***, select Project Interpreter
    -   In the drop-down, it should say the same version printed by `python3`; if not, select that version from the drop-down. If it is not there,
        -   in the terminal type `python -c 'import os,sys;print(os.path.realpath(sys.argv[1]))' $(which python3)`^[I haven't tried this particular script-foo since OS X 10.5, but I suspect it still works]; it should print a path, like `/System/Library/Frameworks/Python.framework/Versions/3.6.1/lib/python3`
        -   in PyCharm's settings, there is a gear icon next to the drop-down; use the "add local" option there to select the path printed above

