---
title: "Lab 8: WahooSpoon"
...

# Attendance

We will be taking roll in lab each week! Please come to your assigned lab to be counted present!

Each lab TAs are empowered to select their own method of taking roll.
Please follow your lab TA's instructions.  
They may dock points if you  are excessively late or leave unusually early.

# Pairing

For this and all subsequent labs, you will work in pairs.

# Recitation

The TAs will do a quick review of lists before the in-lab activity.

# Setup

If you've never used UrbanSpoon, it's an app that helps you choose a restaurant to go to based on some choices and a whole lot of randomness.
We're going to build a simplified version of this app using lists.

Create a file called `wahoospoon.py`.
Start off by setting up some variables to store restaurant names, styles, and costs.
Our suggestion is to use three lists in which the indexes of each restaurant lines up with its style and cost.

````python
import random

restaurants = ["Sticks", "Yuan Ho", "Melting Pot", "East Garden"]
styles = ["Casual", "Chinese", "Fancy", "Chinese"]
costs = ["$", "$", "$$$", "$$"]
````

Of course, add your own entries here!

# Prompt The User and Get Lunch!

Write code to choose between three options: get a random restaurant, get
a random restaurant based on style, and get a random restaurant based on
cost.

It should look something like this:

    Welcome to WahooSpoon! 
      1. Get a random restaurant 
      2. Get a random restaurant based on style 
      3. Get a random restaurant based on cost 
    Choice?

If the user chooses 1, you should call a function called `get_random_restaurant()` to get a random restaurant.
The function should return a tuple of three strings: the name of the restaurant, the style, and the cost.

If the user chooses 2, you should print the list of available styles, removing any duplicates from this printed list.
Prompt the user for which style the user wants.
Then call a function called `get_restaurant_style(chosen_style)` to get a random restaurant.
The function should only take the style the user types as a parameter.
The function should return a tuple of three strings: the name of the restaurant, the style, and the cost.

If the user chooses 3, you should print the list of available costs, removing any duplicates from this printed list.
Prompt the user for which cost the user wants.
Then call a function called `get_restaurant_cost(chosen_cost)` to get a random restaurant.
The function should only take the cost the user types as a parameter.
The function should return a tuple of three strings: the name of the restaurant, the style, and the cost.

An example run could look like this:

    Welcome to WahooSpoon! 
      1. Get a random restaurant 
      2. Get a random restaurant based on style 
      3. Get a random restaurant based on cost 
    Choice? 2
    {'Fancy', 'Chinese', 'Casual'}
    What style would you like?: Chinese
    We're going to East Garden today! (Style: Chinese / Cost: $$ )
    
## Starter code

To help you out, here is some code to start with, including the headers for the functions you need to write.
At no time should you [hardcode](faq.html#what-is-hard-coding) anything from the list of restaurants, styles, or costs!
Imagine how the program should run if we added all the places in Charlottesville.

````python
import random

restaurants = ["Sticks", "Yuan Ho", "Melting Pot", "East Garden"]
styles = ["Casual", "Chinese", "Fancy", "Chinese"]
costs = ["$", "$", "$$$", "$$"]

def get_random_restaurant():
    ...

def get_restaurant_style(chosen_style):
    ...

def get_restaurant_cost(chosen_cost):
    ...


print("Welcome to WahooSpoon!")
print("  1. Get a random restaurant")
print("  2. Get a random restaurant based on style")
print("  3. Get a random restaurant based on cost")
choice = int(input("Choice? "))
if choice == 1:
    r, s, c = get_random_restaurant()
elif choice == 2:
    print(set(styles))
    style = input("What style would you like?: ")
    r, s, c = get_restaurant_style(style)
else:
    print(set(costs))
    cost = input("What cost would you like?: ")
    r, s, c = get_restaurant_cost(cost)

print("We're going to", r, "today! (Style:", s, "/ Cost:", c, ")")
````

Note: the `set`{.python} function used above changes a sequence into a set (a collection that contains no duplicates and has no oder).
We won't spend a lot of time on `set`{.python} in this course.

## Suggestions

On thing you'll need to do repeatedly is make a smaller list out of a bigger list.
For example, once they pick `Chinese` you'll need to figure out what the set of Chinese restaurants is so you can pick one of them randomly.

There are several ways to go about this, but one of the simplest is to make a list of indices.
Loop over all indices and if `styles[index] == chosen_style`{.python} add the index to a list of correctly-styled indices.

Once you have a list of possible options, the function [`random.choice(list)`{.python}](https://docs.python.org/3.5/library/random.html#random.choice) may come in handy.


## Submission

**At least one partner** should submit one .py file named `wahoospoon.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **both partners' ids** in comments at the top of the file.
