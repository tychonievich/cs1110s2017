---
title: "Lab 7: Nim"
...

# Attendance

We will be taking roll in lab each week! Please come to your assigned lab to be counted present!

Each lab TAs are empowered to select their own method of taking roll.
Please follow your lab TA's instructions.  
They may dock points if you  are excessively late or leave unusually early.

# Pairing

For this and all subsequent labs, you will work in pairs.

# Recitation

The TAs will do a quick review of `while`{.python} before the in-lab activity.

# Single-Pile Nim

In this lab you will write a program that lets two players play Nim.
You will also optionally be able to add an optimal computer player.

The Game of Nim is a well-known game with a number of variants. One particularly interesting version plays like this:

> Assume you have a large pile of marbles. Two players alternate taking marbles from the pile. In each move, a player is allowed to take between 1 and half of the total marbles. So, for instance, if there are 64 marbles in the pile, any number between and including 1 and 32 is a legal move. Whichever player takes the last marble loses.

For the main part of this lab, you'll make a program that manages the pile and lets users alternate moves.
Optionally, you can add a computerized player.

## Managing the pile

Your program should

1.  ask the user how many marbles should be in the pile initially
2.  repeat the following until the pile is empty:
    1.  print the number of marbles currently in the pile
    1.  ask Player 1 how many marbles to take
    1.  reduce the pile by that number; if it is now empty, Player 2 won
    1.  print the number of marbles currently in the pile
    1.  ask Player 2 how many marbles to take
    1.  reduce the pile by that number; if it is now empty, Player 1 won

There are three basic approaches to making this work.

-   Your `while`{.python} loop can be organized like
    
        while the pile is not empty:
            do player 1's turn
            if the pile is not empty
                do player 2's turn

-   Your `while`{.python} loop can be organized like
    
        set the current player to 1
        while the pile is not empty
            do the current plater's turn
            toggle the current player (e.g., new current player = 3 - old current player)

-   Your `while`{.python} loop can be organized like

        repeat until told to break out of the loop:
            do player 1's turn
            if the pile is empty
                break out of the loop
            do player 2's turn
            if the pile is empty
                break out of the loop

    In Python, "break out of the loop" is spelled `break`{.python}

We encourage you to get the basic gameplay working first.
You should be able to run a game like the following:

    The Game of Nim
    How many marbles should we start with? 100
    The pile has 100 marbles in it.
    Player 1, how many marbles do you want to take? 23
    The pile has 77 marbles in it.
    Player 2, how many marbles do you want to take? 37
    The pile has 40 marbles in it.
    Player 1, how many marbles do you want to take? 20
    The pile has 20 marbles in it.
    Player 2, how many marbles do you want to take? 5
    The pile has 15 marbles in it.
    Player 1, how many marbles do you want to take? 7
    The pile has 8 marbles in it.
    Player 2, how many marbles do you want to take? 4
    The pile has 4 marbles in it.
    Player 1, how many marbles do you want to take? 1
    The pile has 3 marbles in it.
    Player 2, how many marbles do you want to take? 1
    The pile has 2 marbles in it.
    Player 1, how many marbles do you want to take? 1
    The pile has 1 marbles in it.
    Player 2, how many marbles do you want to take? 1
    Player 1 wins!

## Play by the rules

If there are *n* marbles in the pile, the current player should only be able to take between 1 and *n* ÷ 2 marbles.
If they try to take anything else, ask them again.

This requires two parts: computing the correct range and requiring the user to give you a number in that range.
The correct range is almost `1` to `n//2`, except that doesn't handle the case where `n` is 1 correctly.

To require a number in a specific range, we suggest you add a new function, perhaps named `input_between(prompt, min, max)`.
Inside that function, use a `while`{.python} loop to keep asking for `input`{.python} until the user provides a number in the correct range.

You should then be able to replace your `input`{.python} in your main Nim loop with `input_between` and have rules-checking working.

    The Game of Nim
    How many marbles should we start with? 15
    The pile has 15 marbles in it.
    Player 1, how many marbles do you want to take (1-7)? 7
    The pile has 8 marbles in it.
    Player 2, how many marbles do you want to take (1-4)? 7
    Player 2, how many marbles do you want to take (1-4)? 0
    Player 2, how many marbles do you want to take (1-4)? 4
    The pile has 4 marbles in it.
    Player 1, how many marbles do you want to take (1-2)? 1
    The pile has 3 marbles in it.
    Player 2, how many marbles do you want to take (1-1)? 1
    The pile has 2 marbles in it.
    Player 1, how many marbles do you want to take (1-1)? 1
    The pile has 1 marbles in it.
    Player 2, how many marbles do you want to take (1-1)? 1
    Player 1 wins!

You are welcome to stop here, but if you want more practice, continue with the optional part.

## (Optional) Computer Player

Adjust your game to have player 2 be controlled by the computer.
The computer should play by an optimal winning strategy, which means

-   If possible, it wants the remaining number of marbles after its move to be one less than a power of 2.
-   If the above is not possible, it takes a single marble.

Create a function `optimal_move(n)` that returns the optimal number of marbles to take, given a pile of size `n`.
This will likely need the help of an additional function `power_of_two_below(n)` which returns the largest a power of 2 that is &le; *n*.

`power_of_two_below(n)`
:   Start with 1, repeatedly double it until it is > *n*, then divide it by 2 and return

`optimal_move(n)`
:   Return *x* such that `x + (power_of_two(n) - 1)` = *n*; but if that is < 1, return 1.

Then use `optimal_move` instead of `input_between` for Player 2.

    The Game of Nim
    How many marbles should we start with? 15
    The pile has 15 marbles in it.
    Player 1, how many marbles do you want to take (1-7)? 7
    The pile has 8 marbles in it.
    Player 2 takes 1 marble.
    The pile has 7 marbles in it.
    Player 1, how many marbles do you want to take (1-3)? 1
    The pile has 6 marbles in it.
    Player 2 takes 3 marbles.
    The pile has 3 marbles in it.
    Player 1, how many marbles do you want to take (1-1)? 1
    The pile has 2 marbles in it.
    Player 2 takes 1 marble.
    The pile has 1 marbles in it.
    Player 1, how many marbles do you want to take (1-1)? 1
    Player 2 wins!



## Submission

**At least one partner** should submit one .py file named `nim.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **both partners' ids** in comments at the top of the file.

