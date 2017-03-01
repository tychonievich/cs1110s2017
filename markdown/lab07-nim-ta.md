---
title: "Lab 6: Magic 8-ball - TA guide"
...

# Background

This will be students' first required use of `while`{.python}.
Significant structure if given on the [student lab writeup](lab07-nim.html).

# Introduce/Review `while`{.python}

`while`{.python}'s semantics
:   check, do, recheck
    
    ````python
    while x:            if x:                  # line X
        y                   y
                            go back to line X
    ````

Top-down loop design
:   In pseudocode, identify
    
    -   something needs to repeat
    -   what that something is
    -   under what condition is needs to repeat
    
    Then put that together into a loop

Bottom-up loop design
:   Start solving the problem without a loop. The moment you find yourself repeating code,
    
    -   indent one copy of the repeated code
    -   add `while ____:`{.python} in front of the indented part
    -   determine how you would know you are done to fill in the blank
    -   delete the other copies, as the `while`{.python} does the repeating for you

# Guidance

The lab writeup gives several pseudo-code loops; any of them will work.

If a student attempts to use recursion instead, compliment them on their ingenuity but also encourage them to use a loop for this lab.

`for`{.python} is problematic for this task and should be discouraged.

# Help

## Supervise pairing

Keep an eye out for pairs dominated by one partner or the other.
Suggest these partnerships switch driver.
You could also do something like announce "Everyone now switch so the person on the left is driving!" periodically, helping you know which person should drive at any given time.

When asked a question by one partner, your first response should always be to turn to the other partner and say something like "What do you think?"

## There's a lot of text

They can't think of how to get "play by the rules" working?
Ask them to read the text there aloud to you.
Likely the answer is there, and is they don't understand it the process of having them read will give you a chance to see what they don't understand.

## Remind them to test

When they are stuck, ask them if they wrote any testing code.
If not, show them how to do that.

## Start small

Encourage them to have runnable programs often along the way.  If the whole thing is too large, encourage them to start with a simpler program, such as one that

-   asks for numbers but ignores them and never stops
-   lets the pile get negatively large
-   has only one player
-   alternates players without a pile
-   always plays three rounds, never more or less

Once they have one of these working, have them pick one more feature to add, then another, etc.
