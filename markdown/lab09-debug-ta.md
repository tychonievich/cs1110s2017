---
title: "Lab 9: Debugging - TA Guide"
...

# Running the Lab

Encourage them to work in teams.  More than 2 is OK for this lab.

Review the debugging guide on the student site.

Tell them they actually need to read the entire student page.  There is information there they will not be able to do the lab without.

Remind them that they should *either* fix all bugs *or* work until the end of lab; doing both is not required.

# The Bugs

The bugs I introduced are as follows,
listed in order of where they appear in the code.

## `replace` doesn't modify, it returns

The `etext =`{.python} is missing in the following lines of `phrases(etext)`{.python}.
This results in some words appearing with sentence-trailing punctuation.

incorrect                            fix
------------------------------------ ------------------------------------
`etext.replace('\n', '.')`{.python}  `etext = etext.replace('\n', '.')`{.python}
`etext.replace('!', '.')`{.python}   `etext = etext.replace('!', '.')`{.python}
`etext.replace('?', '.')`{.python}   `etext = etext.replace('?', '.')`{.python}


## Don't skip `"I"`

The `len(word) == 1`{.python} is missing in the following line of `words(phrase)`{.python}.
This results in `i`{.python} not being found.

incorrect                            fix
------------------------------------ -----------------------------------------------------
`if word != word.upper():`{.python}  `if len(word) == 1 or word != word.upper():`{.python}


## Don't re-set dicts

Global dictionary initialization is inside `populate_list(etext)`{.python}.
This results in the contents of `snark.txt` not being in the dicts because it was over-written by `alice.txt`

incorrect                    fix
---------------------------- ---------------------------------------
`master_list = {}`{.python}  *move outside the function*
`frequencies = {}`{.python}  *move outside the function*


## Check for missing words

An `if`{.python} statement has been removed from the beginning of `most_commonly_with(target)`{.python}.
This results in an error message when typing a word that is not in the corpus.


incorrect   fix
----------- ----------------------------------------
*missing*   `if target not in master_list:`{.python}
*missing*   `    return None`{.python}


## Add parentheses

parentheses are missing from the following line of `most_commonly_with`{.python}'s `bycount`{.python} function.
This results in the wrong frequencies being found.

incorrect                                                         fix
----------------------------------------------------------------  -----------------------------------------------------
`return counts[e]/frequencies[e] + frequencies[target]`{.python}  `return counts[e]/(frequencies[e] + frequencies[target])`{.python}


