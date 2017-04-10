---
title: flappybird.py
...

# Task

Implement a [FlappyBird](https://flappybird.me/)-like game using pygame.

In particular,

-   There should be one kind if user input, a vertical flap action triggered by either a mouse click or the space bar (your choice) -- you do not need to use an animated sprite sheet for this assignment
-   There should be randomly generated scrolling obstacles (pillars) with openings at random heights
-   Touching the ground or a pillar should end the game
-   Score should be based on how long the player lasts before the game ends
-   When the game ends, the score should be displayed

We won't be able to perform automated testing for this submission (we'll have course staff run it to grade it), but you should be able to tell if it is working on your own by playing the game you've created.

In implementing the game, avoid over-running the computer's resources.
In particular

-   Don't draw() a gamebox for a pilar until it is almost on the screen
-   Remove (or re-use) pilars that go off the screen behind the player

Typically this means having some logic like this in your tick function:

````
if the left-most pillar is off the left side of the screen,
    move it to some distance past the right side of the screen
    re-randomize its opening's vertical location
````

That way you can have a small fixed number of pillar objects in Python
look like an endless stream of pillars when playing the game
