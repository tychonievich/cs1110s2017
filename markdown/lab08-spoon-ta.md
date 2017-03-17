---
title: "Lab 6: WahooSpoon - TA guide"
...

# Background

This will be students' first required use of `list`{.python}, and first expected use of `for`{.python}.

Encourage students to read the [suggestions section](lab08-spoon.html#suggestions).

# Introduce/Review `list`{.python}

The students should have seen `for`{.python} and `list`{.python} in class.
[List methods](https://docs.python.org/3.3/tutorial/datastructures.html#more-on-lists) they should already know include {`append`, `index`, `insert`, `sort`, `reverse`, `remove`}; list built-in functions they should know include `sum`; list-impacting operators they should know include {`del`, `in`, `+`}.

To help them get started, review the following:

## Iterate by Index

A common pattern, which they may not have seen (depending on their lecture section), is iterating over a list by index instead of by value.

````python
for index in range(len(collection)):
    element = collection[index]
````

The value of such an iteration is it lets us say things about place:

````python
names = 'Luther Upsorn Craig Jim Mark Ahmed Dave'.split()
for index in range(len(names)):
    name = names[index]
    if 'e' in name:
        print('The instructor at index', index, 'has an e in their name')
````


## Filtering lists

Sometimes we want a sub-list of another list.  We can make that by appending to an initially empty list.

````python
squares = []
for n in range(100):
    if n**0.5 == int(n**0.5):
        squares.append(n)
print('the perfect squares are', squares)
````


## Parallel lists

Given

````python
restaurants = ["Sticks", "Yuan Ho", "Melting Pot", "East Garden"]
styles = ["Casual", "Chinese", "Fancy", "Chinese"]
costs = ["$", "$", "$$$", "$$"]
````

how do we find the style of `Melting Pot`?

1.  We find where `Melting Pot` is in its list
    
    ````python
    where = restaurants.index('Melting Pot')
    ````

2.  We find what is in the styles list at that index

    ````python
    style = style[where]
    ````

We suggest you have the students work on this on their own first, then show them the solution.



