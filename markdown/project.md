---
title: game.py
...

# Overview

Your task is to use PyGame and gamebox to create in interesting game with a partner.
Unlike other assignments,

-   You should work with one (1) partner for the entirety of this assignment
-   This assignment is worth more points (see [the syllabus](syllabus.html) for details)
-   You are free to define the details of this assignment yourselves
-   We'll check your progress (based on current archimedes submissions) *every Thursday*; lack of progress will result reduced final grades.

# Partnering

## Recording a partner.

Create a "new file" in PyCharm named `partner.txt`.  In it put *only* the computing ID and name of your partner, like so:

````
lat7h
Luther Tychonievich
````

Submit it as one of your files for this assignment on [Archimedes](https://archimedes.cs.virginia.edu/cs1110/).
This assignment lets you submit several files; this is one of them.

The due date for `partner.txt` is Thursday 13 April 2017 (lab that day will help you if you don't have one before then).
You and your partner *must* both have each other's IDs in your submitted `partner.txt`s by Friday morning.

You can see if your partner submission worked by visiting [the partner summary page](https://archimedes.cs.virginia.edu/cs1110/partners.php).

If you want to work alone or need a group of three, your lab TA (or Professor Dill for 1111) can help you understand how to submit that.  Groups of three will only be approved in the event of an odd number of unmatched people.

Preferably, you'll pick a partner within your same lab section, but that is not strictly required.

## Working together

To the degree possible, please plan to work together, rather than each working independently and combining code later.
Working together can result in fewer bugs and better code.

If you have problems with your partner, first bring them up to your partner and then to your instructor.
We'll do our best to help things run smoothly.

We will also ask for each student to submit a partner evaluation near the end of your time together.

# Designing your game

Each game is expected to be unique; we do not tell you what to implement.
However, we do provide some guidelines to keep the scope appropriate:

## Required Features

Your game should look like a game someone might want to play (i.e., probably not just a lot of colored boxes).
You must include all of the following:

User Input
:   Either through the keyboard or mouse, you should have appropriate and working user controls.

Graphics/Images
:   You should use some appropriate images in your game.

Start Screen
:   Game has a start screen with game name, student names (and IDs), and basic game instructions.

## Optional Features

You must include at least four of the following:

Animation
:   Use a sprite sheet to have an animated character.

Enemies
:   Have characters that can hinder the player character from accomplishing the goal.

Collectables
:   Add collectables (i.e. coins) to the level that can be picked up by the character with a counter that appears on the screen.

Scrolling level
:   Make it so you can keep going off the screen! (You may need to add a background image to make this more obvious.)

Timer
:   Have a countdown (or count up) timer for your game.

Health meter
:   Have a health meter that changes as you hit enemies/obstacles.

Music/Sound effects
:   Have some good sound design.

Two players simultaneously
:   Two players who are able to interact with one another within the game.

## Other Constraints

It is *not* sufficient to base your game on our examples.
The example code is designed to teach concepts and give code snippets you can use,
but since we did an infinite jumper, you should not do one.

# Game Ideas

Don't have a good game idea in mind?
See [Wikipedia's list of golden-age arcade games](https://en.wikipedia.org/wiki/Golden_age_of_arcade_video_games#List_of_popular_arcade_games) for many ideas.

# FAQ

Many questions of the form "how do I do *X*" are answered in [The PyGame Docs](http://cs1110.cs.virginia.edu/code/gamebox/gamebox.pdf).
Others are added here as they come to our attention.

Why do my fast-moving objects pass through walls?
:   Because in a single frame they make it past the center of the wall, so `move_to_stop_overlapping` moves them out the wrong side.

    The simplest solution is making fatter obstacles (or fatter objects; if an object cannot move more than `min(obj.width, obj.height) / 2` pixels per frame, it cannot have this problem)
    
    A fancier three-part solution is to (a) increase the ticks per frame by a factor of $n$, (b) reduce the speeds by a factor of $n$, and (c) only draw and display once every $n$ frames.  Parts (a) and (b) solve the problem, part (c) keeps the solution from over-taxing your computer.
    
    The most robust solution is to track which side of each obstacle you were last frame and which side this frame and if that changes, do something about it; doing this correctly is not simple, but the `overlap` method of boxes can help if you want to try.

How do I make a grid-movement-based game?
:   Pick a grid size $g$ and then only change $x$ and $y$ in increments of $g$.


# Submission

You'll need to submit your code and any support files to Archimedes.
In addition to the final submission date of midnight, 2 May 2017
we will also check your submissions **each Thursday** between now and then (i.e., 20 April and 27 April).
**Making steady progress every week** is a requirement for full credit on this assignment.

We accept all kinds of files in the submission, but note:

-   You **must** submit `partner.txt` as part of the first submission
-   The game must be run by using `game.py`; it may use other `.py` files too if you want
-   If you make your own graphics, level files, etc., upload those; but media you download should be accessed by URL not file so we can save space on the submission server
-   Don't upload copyrighted material which you do have rights to give us

At least one partner will need to submit your files each time you submit.
If more than one submit the same file name, the last submission of the group will be used.

