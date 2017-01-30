---
title: "Lab 4: Madlibs"
...

# Attendance

We will be taking roll in lab each week! Please come to your assigned lab to be counted present!

Each lab TAs are empowered to select their own method of taking roll.
Please follow your lab TA's instructions.  
They may dock points if you  are excessively late or leave unusually early.

# Pairing

For this and all subsequent labs, you will work in pairs.

# Recitation

The TAs will do a quick review lesson on data types before moving on to
the in-lab activity.

# Building a Madlib

Madlibs work as follows:

1.  Pick a phrase, and replace key words with what kind of word they are.
    For example, you might decide your phrase is
    
    > When I was younger I wanted to be a *profession1*. I pictured myself at a *event1*.  One person says "I'm a *profession2*." Another says "I'm a profession3, just back from *where profession3 works*."  I say "I'm a *profession1!" With a gasp, everyone turns to me.  "You're a *profession1*?  Tell us more!"
    >
    > Then I met you. Now I know that all *profession1*s do is *task1* and no one cares.  Thank you for showing me the true way.
    
    You can pick any phrase you want.
    Often stranger phrases with more key words missing are more interested.
    
1.  Without showing the user the phrase, ask the user for the words you left out.
    For example, you might ask
    
        A profession: phone booth sterilizer
        Something people do: make money
        Another profession: juggler
        A third profession: astronaut
        A place: the Gobi desert
        A kind of event: bluegrass jam session
        
1.  Display the phrase, replacing the key words with the words the user supplied.

    > When I was younger I wanted to be a phone booth sterilizer. I pictured myself at a bluegrass jam session.  One person says "I'm a juggler." Another says "I'm a astronaut, just back from the Gobi desert."  I say "I'm a phone booth sterilizer!" With a gasp, everyone turns to me.  "You're a phone booth sterilizer?  Tell us more!"
    >
    > Then I met you. Now I know that all phone booth sterilizers do is make money and no one cares.  Thank you for showing me the true way.
   
Your goal in this lab is to work with a partner write a program that performs a madlab,
called `madlib.py`.
The program will prompt the user for all the words, then display the phrase.
The phrase should use at least one of the words the user types in more than once place.

For this assignment, we are not auto-grading your results.
So feel free to be creative with the phrase! (Within reason, of course...)

We will, however, look at how you wrote the code.
Specifically, how you solved the problem.
How did you read in what the user typed?
How did you set up your phrase?
How easy would it be to change the phrase?
Did you use functions, good variable names, and comments to help make your code easy to read?

## Submission

**Each partner** should submit one .py file named `madlib.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **both partners' ids** in comments at the top of the file.

