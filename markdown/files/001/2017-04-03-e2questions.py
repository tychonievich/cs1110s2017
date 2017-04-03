q = '''
is the list comprehensive? - yes (within its scope)
set in exam? - no
exam structure
example of hand-written code difficulty vs homework difficulty


and, or, not
    and - True if and only if both operands are true
    or - True if either (or both) operand is true
    not - turns true into false and vice-versa

string indexing
    start at 0
    at other end, we start at -1
    "hi there"[2] == ' '
    "hi there"[-6] == ' '
slice
    has two indices
    subsequence, includes the left index and not the right
    "hi there"[2:5] == ' th'
    missing left index is assumed to be 0
    missing right index assumed to be len(sequence)
    "hi there"[:2] == 'hi'
    "hi there"[2:] == ' there'

strip split order
url - open, read, when to do what
    readline -> next line as one str

    read -> whole thing as one str
    readlines -> whole thing as a list of str, one per line
    for -> whole thing, one line at a time, as a str
decode utf-8 -- when do you do it?
    decode from url, not from a file
    do it on a string

substring in string
    "hi" in "white" == True
    "Hi" in "white" == False
    [1,2] in [1, [1,2], 1, 2] == True
    [1,2] in [1, 1, 2, 1, 2] == False

find's arguments
    string.find(substring) -> first index of the substring
    "hi there".find('e') == 5
index works like find but for lists not strings
    [0,2,5,7].index(2) == 1

what is mapping
    other languages call what python calls "dict" a "map"
        "mapping" key:value relationship
    …or maybe you meant lab last week, in which case it is cartography

dict vs list
how to use dict when writing code
    use it when we ask you to do so
methods of dict
    keys()
    values()
    items()

why do list methods modify not return?

random, randrange -- structure, chosing to use
    random.randrange(0, 10)

while vs for -- when to use which
    if you describe in English using words like
        "until", "as long as", ... → while
        "once for each", "for", "X times" → for
use with lists
    for element in list:
        ...
    for index in range(len(list)):
        ...

finding index in string in list
    for string in list:
        find the index in this string

using bool flags in a loop
'''

# count, accumulate
count = 0
for thing in collection:
    count += do_stuff(thing)

# check a condition
# for all things:
guess = True
for thing in collection:
    if not condition_holds(thing):
        guess = False

# for some thing:
guess = False
for thing in collection:
    if condition_holds(thing):
        guess = True

