---
title: "Lab 6: Magic 8-Ball"
...

# Attendance

We will be taking roll in lab each week! Please come to your assigned lab to be counted present!

Each lab TAs are empowered to select their own method of taking roll.
Please follow your lab TA's instructions.  
They may dock points if you  are excessively late or leave unusually early.

# Pairing

For this and all subsequent labs, you will work in pairs.

# Recitation

The TAs will do a quick introduction to 

-   `import random`{.python}, `random.randrange(n)`{.python}, and Python's use of \[0, *n*\) intervals
-   The `startswith` method available for strings

... before the in-lab activity.


# Building a Fortune Teller

In this lab you will

1.  Write a function that returns random variations of yes/no answers.
2.  Write another function that takes a question as a parameter and returns a random answer.  It will also do a simple check to detect some kinds of non-yes/no questions and return a different answer for them.
3.  Write a program that uses the functions to answer questions.

As an enrichment activity, we'll also talk about how to make these graphical instead of console-based.

## Return a random string

Write a function that takes no argument and returns a random string that is a grammatically sound answer to a yes/no question.  `Yes` and `No` are obvious possibilities, but so are things like `Definitely`, `Wait and see`, `You won't like the answer`, etc.

There are many ways of doing this, but one of the most uniformly random is as follows.

````
generate a random integer between 0 and n (not including n)
if the random integer was 0,
    return the first answer option

generate a random integer between 0 and n-1 (not including n-1)
if the random integer was 0,
    return the second answer option

...

generate a random integer between 0 and 2 (not including 2)
if the random integer was 0,
    return the next-to-last answer option

return the last answer option
````

## Inspect a question

Write a function that takes as an argument a string representing a question.
Perform some basic checks to see if the string is unlikely to be yes/no; if it is, return some kind of `You were supposed to ask a yes/no question` message; otherwise invoke the function you wrote in the previous step.

Questions that begin with `Who`, `What`, `When`, `Where`, `Why`, or `How` are almost never yes/no questions.
Questions that begin with `Does`, `Is`, `Can`, or `Will` are usually yes/no questions.
You can add as many of these rules of thumb as you wish.

FYI, an educated guess like implemented in software is called a **heuristic**.

## Make it a program

Prompt the user to ask you a question.
Use your functions to get an answer and display it to the user.
If the answer is your `not yes/no question` answer, use an `if`{.python} statement to ask for a second question and get a second answer.

## (Optional) Make it graphical

So far we've only used console programs, but Python also comes with a graphical user inteface (GUI) library pre-installed call `tkinter`.
GUIs require a bit of overhead to use because there are many things we have to tell the computer,
but if you want to here is a way to get started.

````python
def tk_input(prompt):
    '''Python comes with a windowing library called Tk, part of the TCL/Tk system.
    This function uses that to make a popup-window clone of the built-in function
    input.'''
    
    import tkinter
    
    root = tkinter.Tk() # make a window on the screen
    
    # input(prompt) does three things: it displays a prompt, waits for user input, and returns that input
    
    # display a prompt
    prompt = tkinter.Label(root, text=prompt)
    prompt.pack() # tells Tk "place this Label in the window"
    
    # create some place they can type
    entry = tkinter.Entry(root)
    entry.pack(fill=tkinter.X) # the fill part is optional...
    
    def whendone(widget):
        '''We want the window to disappear when the user pressed Return.
        This function is a *callback*, a function called on an event,
        which implements that behavior'''
        root.quit()
    root.bind('<Return>', whendone)
    
    # wait for input
    root.mainloop()
    
    # we only get to this line after input is available
    # the input is inside the Entry, so we get it out to return
    return entry.get()
````

There are *many* ways we could customize this code;
for example, we could make the fonts bigger by

````python
    import tkinter.font
    big_font = tkinter.font.Font(size=40)
    # ...
    prompt = tkinter.Label(root, text=prompt, font=big_font)
    # ...
    entry = tkinter.Entry(root, font=big_font)
````

... and so on.
The official documentation for Tk is not great, but there are many examples you can find online.

### Using windows in submissions

You are welcome to submit a graphical solution to this lab.
For other submissions *don't submit Tk code unless we specifically state it is allowed*.

## Submission

**At least one partner** should submit one .py file named `magic.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **both partners' ids** in comments at the top of the file.

