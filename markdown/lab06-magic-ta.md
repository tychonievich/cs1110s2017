---
title: "Lab 6: Magic 8-ball - TA guide"
...

# Background

The students have not had any lecture since the exam.
Part of the goal of this lab is to have fun and unwind, but also to begin exploration of the python standard library.

# Introduce/Review

## `random.randrange`

Students have seen `import random`{.python} before, but it has been a while for some of them.
Review/reteach the following:

-   Some functions are built-in (like `print`{.python} and `str`{.python})
-   Some functions you write yourself
-   Some functions someone else wrote but you need to `import` to get access to.
    -   Reminder: If you wrote a file named `random.py`, `import random`{.python} will import your file, not the one that came with Python.

-   Things you can import are documented online; e.g., [https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)

Focus specifically on [`random.randrange`{.python}](https://docs.python.org/3/library/random.html#random.randrange).

-   `n = random.randrange(4)`{.python} will return a random number `n` such that `0 <= n < 4`
-   Starting at zero and excluding the high endpoint are common in Python and other programming languages
-   Note that `randrange(4)`{.python} returns one of 4 possible values: 0, 1, 2, or 3.

## `str.startswith`

Students have probably not seen the [`startswith`](https://docs.python.org/3/library/stdtypes.html?str.startswith) method of strings.
It isn't complicated; a simple example is to show them

````python
s = 'Example string'
print(s.startswith('E'), s.startsWith('Example st'))
print(s.startswith('e'), s.startsWith('exam'))
````

# Guidance

The lab writeup talks about the functions the students will write.
However, it can be nice to start by showing them what they are shooting for and walking them through a design first.
The following works and can be nice to show them running (but not show them code as it is not the way they should solve the problem since it uses lists and tuples).

````python
def tk_input(prompt):
    '''Python comes with a windowing library called Tk, part of the TCL/Tk system.
    This function uses that to make a popup-window clone of the built-in function
    input.'''
    import tkinter, tkinter.font
    
    root = tkinter.Tk() # make a window on the screen
    big = tkinter.font.Font(size=30)
    
    prompt = tkinter.Label(root, text=prompt, font=big)
    prompt.pack() # tells Tk "place this Label in the window"
    
    entry = tkinter.Entry(root, font=big)
    entry.pack(fill=tkinter.X)
    
    def whendone(widget):
        root.quit()
    root.bind('<Return>', whendone)
    root.mainloop()
    answer = entry.get()
    root.destroy()

    return answer

def tk_print(message):
    '''Python comes with a windowing library called Tk, part of the TCL/Tk system.
    This function uses that to make a popup-window clone of the one-argument
    version of the built-in function print.'''
    import tkinter, tkinter.font
    
    root = tkinter.Tk() # make a window on the screen
    big = tkinter.font.Font(size=30)
    
    # 1. display a message
    prompt = tkinter.Label(root, text=str(message), font=big)
    prompt.pack() # tells Tk "place this Label in the window"
    
    # 2. close if they press enter
    def whendone(widget):
        root.quit()
    root.bind('<Return>', whendone)
    root.mainloop()
    root.destroy()

def random_answer():
    import random
    return random.choice(['Yes', 'No', 'Definitely', 'Not a chance', 'Your guess is as good as mine'])
def answer(question):
    if question.capitalize().startswith(('Who','What','When','Where','Why','How')):
        return 'That was not a yes/no question'
    return random_answer()

q1 = tk_input("Ask me a question and I'll reply")
a1 = answer(q1)
if 'yes/no' in a1:
    q2 = tk_input("I meant a yes/no question; try again:")
    a2 = answer(q2)
    tk_print(a2)
else:
    tk_print(a1)

````

Show them a few yes/no questions to demonstrate the random answers;
also show them a non-yes/no question like `Why should I?` to demonstrate the yes/no detection.

Walk through or have them volunteer the pieces of work needed:

-   selecting a random answer
-   checking for common non-yes/no question formats
-   retrying if wasn't yes/no
-   displaying

Explain that the steps of this lab correspond to those pieces.
Encourage them to do them one at a time, testing each as they go.

Remind them that it is important to test each piece of functionality as it is finished, as well as multiple times along the way.

Remind them that lab is graded on participation, not completion; we want them to be engaged and learn by doing.

# Help

## Supervise pairing

Keep an eye out for pairs dominated by one partner or the other.
Suggest these partnerships switch driver.
You could also do something like announce "Everyone now switch so the person on the left is driving!" periodically, helping you know which person should drive at any given time.

When asked a question by one partner, your first response should always be to turn to the other partner and say something like "What do you think?"

## Remind them to test

When they are stuck, ask them if they wrote any testing code.
If not, show them how to do that.

## Many solutions, not all equal

Some students will try to use `random.choice` or the like to simplify their code.
If you see this, ask both partners to explain something about the code, such as

> TA: "What does `random.choice` do?"
>
> Student 1: "It …"
>
> TA (to student 2): "What do the square brackets mean?"
> 
> …

If one or both student is confused or unclear on the code,
encourage them to both stick to topics they both understand.
We'll come back and teach the more advanced techniques later in the semester.

