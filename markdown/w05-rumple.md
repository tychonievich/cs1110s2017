---
title: rumple.py
...

# Task

Various folk tales (namely those of Aarne-Thompson type 500) hinge on the difficulty of guessing strange names
(e.g. Rumpelstiltskin, Tom Tit Tot, Whuppity Stoorie, Gilitrutt, جعيدان, Хламушка, Rumplcimprcampr, Martinko Klingáč, Ruidoquedito, Pancimanci, Cvilidreta, Tremotino, עוּץ-לי גוּץ-ל, 大工と鬼六, Myrmidon, etc.).
This assignment has you implement such a system.

Write a program named `rumple.py` that repeatedly asks the user to guess a name until it guesses the right one.
So that we can test your program, open with a version of the rhyme the Brothers Grimm added to their variant of the story:

````
You will never win the game, for Rumpelstiltskin is my name.
````

... replacing `Rumpelstiltskin` with whichever name you picked.  Please pick a name that neither begins nor ends with spaces.

Then repeatedly ask the user to `Guess my name:`;
If they enter the correct name, give some kind of frustrated reply (e.g., `No! How did you guess?`)
and end the program.
If they enter the wrong name, give some kind of triumphant reply (e.g., `Ha! You'll never guess!`)
and then ask them to guess again.

# Example Invocations

Each implementation of `rumple.py` might have a different target name.
If yours used `Rumpelstiltskin`, one run might be

````
You will never win the game, for Rumpelstiltskin is my name.
Guess my name: Rumpelstiltskin
No! How did you guess?
````

Another run might be

````
You will never win the game, for Rumpelstiltskin is my name.
Guess my name: rumple
Ha! You'll never guess!
Guess my name: Rumple
Ha! You'll never guess!
Guess my name: Whuppity Stoorie
Ha! You'll never guess!
Guess my name: Cvilidreta
Ha! You'll never guess!
Guess my name: Tom Tit Tot
Ha! You'll never guess!
Guess my name: 
Ha! You'll never guess!
Guess my name: I give up
Ha! You'll never guess!
Guess my name: Just tell me your name!
Ha! You'll never guess!
Guess my name: rumpelstiltskin
Ha! You'll never guess!
Guess my name: My advisor the midget
Ha! You'll never guess!
Guess my name: Rumpelstiltskin
No! How did you guess?
````

# Thought Question

Some variants of Aarne-Thompson type 500 have a limit on the number of guesses or the amount of time in which guesses can be made.
How would you add those to your implementation?

If the user types nothing, it might be nicer not to gloat:

````
Guess my name: Tom Tit Tot
Ha! You'll never guess!
Guess my name: 
Guess my name: I give up
Ha! You'll never guess!
````
The code you submit should *not* include any of these extensions.

# Troubleshooting

You'll probably either need an `if`{.python} statement or two different `input` invocations.