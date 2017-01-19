---
title: Frequently Asked Questions
...

<style>h1 { font-size:1em; border: none; }</style>


# How do I get off the waitlist?

In order to come off the wait list, there has to be an open seat in BOTH the lecture and lab you are signed up for. If one or the other is not true, then SIS moves on to the next student who has the right combination.

Our main cap is the lab. The lab sessions CANNOT go over 46 due to fire code limits. A few seats in each lab are held back for a week or so to accommodate very special cases.

Some examples of special cases include:

-   Current SEAS 2nd year or higher that has not taken a CS 1 class yet
-   Incoming SEAS transfer 2nd year or higher
-   Early graduation

All SEAS Students will be given a seat, once each, provided they fill out the above form.  If you lose it by dropping and re-adding the course, we cannot re-accommodate you.

<!--
If you feel you warrant special consideration and are currently on the waitlist, please fill out the form here: [https://goo.gl/forms/rL5Mx4c6cjYVP1t53](https://goo.gl/forms/rL5Mx4c6cjYVP1t53)
-->

Earlier there was a link here to a form to submit a waiting list appeal. We have already handled all those appeals and have relinquished control over our extra seats. We no longer have resources to honor additional appeals.

*CLAS (and other schools) Students:*

- If you are a first year, we're sorry, but you probably won't get the course this semester. You are welcome to stay on the wait list to see what happens.
- If you are thinking about the BA major in CS, you need to take 1110 by your third semester. You still have plenty of time. If this is your third semester or later, fill out the form above.
- If you are in a major that requires CS 1110 (Math, Cog Sci -- note *NOT* Commerce!) and are either a third or fourth year, use the form above.

*Consider the other CS1 courses:*

We are offering two other CS1 courses this semester: CS 1112 with Prof. Cohoon (for students with no programming experience) and CS 1113 with Prof. Ibrahim (for future engineers). These are both good options to consider and all count the same for prerequisites and major requirements!

We wish we could take everyone that wanted CS 1110 or CS 1111, but it’s simply not feasible with the room sizes and resources we have. Please do try again next semester if you can’t get in this time.

We cannot control how many students leave the course, opening up room on the waiting lists, but historically we have had waiting lists shrink by as many as 5--10 students per lab section prior to the add deadline.

Let us know if you have any questions.


# What can I do while on the waiting list?

You are welcome to come to 1110 lectures, but not to physically come to labs (the first week's lab being an exception: you may come to that), though attempting the lab activities on your own is encouraged.
1111 lectures sometimes fill the room, so you might be asked to leave the room to make space for those enrolled if you are on the 1111 waiting list.

We hope to also give you the ability to submit assignments while on the waiting list so that when/if you get off you are in no way behind on your work.
No promises, though.


# My computer died. What do I do?

As this is a programming class, we do expect you to have access to a computer for the duration of the semester.
If you are temporarily without a working machine, Python and PyCharm should be installed on publicly available machines in Alderman Library and other locations.

We expect you to make regular backups of your code so in the event of a failure you still have access to your assignments.
We will not accept a computer failure as a reason to waive a late penalty for an assignment.

We highly suggest you look into using a cloud-based solution to make constant backups of particular directories on your computer, such as UVaBox found at [http://its.virginia.edu/box/](http://its.virginia.edu/box/) or Dropbox found at [http://dropbox.com](http://dropbox.com).
You can also do some basic assignments in an in-browser Python environment such as 
[https://repl.it/](https://repl.it/), [http://c9.io](http://c9.io), [http://pythontutor.com](http://pythontutor.com), etc.


# Can I permanently swap labs?

You can, assuming you find someone to swap with.
You can [post on Piazza](https://piazza.com/class/iwxt2sk0gjf72b?cid=6) if you are interested in doing this.
If BOTH people agree to the swap, email Prof. Tychonievich and he'll take care of it.
DOUBLE CHECK that you both can actually take the other lab before agreeing! Check Piazza for more information.


# Can I go to different lab section this week?

Due to fire code limits, you cannot attend another lab session, even for just one week.
We're also doing group work, so you need to be there for your team.

If this is a class/test session, your other professor should provide you with an alternate time since you have a university class at the same time.

Missing one week in general will not affect your grade. Every student can miss one lab with no penalty (and you do not need to make up the work).


# I'm in the *X* lecture, can I go to the *Y* lecture instead?

1111 students can attend an 1110 section on occasion if they like, though doing so will not excuse any missed attendance or participation activities.
1110 students should not attend 1111 lectures due to the size of the classroom.
1110 students can attend the other 1110 section on occasion as well, though again each section may have its own attendance and participation activities.


# Can I take my test in a different lecture section?

Absolutely not.

# I have another final exam at the same time as our final exam. What do I do?

When we get closer to the end of the semester, we'll have a form you'll fill out to get a separate time. We will accommodate most all cases here with no issue. Please do not email us about this before the end of the semester as we will have no other information to tell you.


# I have travel and will miss the final exam. What do I do?

University policy does not require us to provide any accommodations for travel.
We might make exceptions for special cases, but "I already paid for tickets" is *not* a special case.


# My program handled all the example inputs correctly but still got a 0.  Why?

This could be a grading error, but could also be because you hard-coded those specific cases instead of solving the general problem (see [the syllabus](syllabus.html#generality-of-solutions)).

# What is "hard-coding"?

[Wikipedia](https://en.wikipedia.org/wiki/Hard_coding) defines it as "embedding [...] an input or configuration data directly into the source code of a program."
In this course, it most commonly appears when students solve the examples but not the general problem.

For example, suppose we ask for "a function called `sum` that computes the sum of two numbers.  For example, `sum(2, 3)`{.python} should give `5` and `sum(-1.1, 1.0)`{.python} should give `-0.1`."
A correct solution would solve the general problem, like this:

````python
def sum(x, y):
    '''returns the mathematical sum of its arguments'''
    return x + y
````

Conversely, a solution with the example inputs hard-coded might look like this:

````python
def sum(x, y):
    '''a hard-coded solution that returns the mathematical sum 
        of (2, 3) and (-1.1, 1.0), but not most other values'''
    if x < 0: 
        return -0.1
    else:
        return 5
````


# Can I make an announcement in CS 1110 or CS 1111?

We get so many of these requests that we cannot grant them all, and to avoid being unfair we generally do not grant any of them.
If the announcement is purely academic in nature and there is a compelling reason why Introduction to Programming lecture is the right place to make it, email the professors; but we still make no guarantee we'll accommodate you.

Raising your hand in class to make an announcement (rather than to ask or answer a question) is [unprofessional behavior](syllabus.html#professionalism) and will be treated as such.
