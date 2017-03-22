---
title: "Lab 9: Debugging - TA Guide"
...

# Running the Lab

Encourage them to work in teams.  More than 2 is OK for this lab.

Review the debugging guide on the student site.

Tell them they actually need to read the entire student page.  There is information there they will not be able to do the lab without.

Remind them that they should *either* fix all bugs *or* work until the end of lab; doing both is not required.

# The Bugs

The `etext =` is missing in the following lines of `phrases(etext)`.
This results in some words appearing with sentence-trailing punctuation.


incorrect                             fix
------------------------------------  ------------------------------------
````python                            ````python
etext = etext.replace('\n', '.')      etext = etext.replace('\n', '.')
etext = etext.replace('!', '.')       etext = etext.replace('!', '.')
etext = etext.replace('?', '.')       etext = etext.replace('?', '.')
````                                  ````

----

The `len(word) == 1` is missing in the following line of `words(phrase)`.
This results in `i` not being found.



````python
if len(word) == 1 or word != word.upper():
````


----

These lines have been added to `populate_list(etext)`.
This results in the contents of `snark.txt` not being in the dicts

````python
master_list = {}
frequencies = {}
````


----

The parentheses of the following line of `most_commonly_with`'s `bycount` function have been removed.
This results in the wrong frequencies being found.

````python
return counts[e]/(frequencies[e] + frequencies[target])
````

