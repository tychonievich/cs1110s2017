# Write program to find phone numbers of people from Simpsons TV series
# assuming no area code included
#
# http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/simpsons_phone_book.txt
#
# findall() returns the occurrences of the pattern in the target string
#    - create a list of occurrences of a pattern in a string
#    - group(), start(), end() not applicable
# search() gives more information than just the actual patterns
#    - tell where the pattern occurs in the target string
#    - returns a match object for the first occurrence
#    - returns None if pattern is not found
# match() checks if the pattern exists at the very *start* of a string
#    - returns None if pattern not found
#      note: Python processes None as False
# finditer() creates a list (or an iterator) of match objects for where
#      the pattern occurs in a string
#    - thus, can iterate a list of match objects and use group(), start(), end()


import re


# use search() to find a pattern in a string
# and display the match objects on the screen
def search_phone_numbers(filename, reg_ex):
    infile = open(filename, "r")
    for line in infile:
        obj = reg_ex.search(line)
        if obj != None:
            print("use search :", obj, obj.group(), obj.start(), obj.end())
    infile.close()


# use search() to find a pattern in a string
# and display the match objects on the screen, print each group
# note: group() is equivalent to group(0)
def search_phone_numbers_group(filename, reg_ex):
    infile = open(filename, "r")
    for line in infile:
        obj = reg_ex.search(line)
        if obj != None:
            print("use search and group :", obj.group(0), obj.group(1), obj.group(2))
    infile.close()



# use match() to find a pattern at the start of a string
# and display the match objects on the screen
def match_phone_numbers(filename, reg_ex):
    infile = open(filename, "r")
    for line in infile:
        obj = reg_ex.match(line)
        if obj != None:
            print("use match : ", obj, obj.group(), obj.start(), obj.end())
    infile.close()


# use match() to find a pattern at the start of a string
# and display the match objects on the screen, print each group
def match_phone_numbers_group(filename, reg_ex):
    infile = open(filename, "r")
    for line in infile:
        obj = reg_ex.match(line)
        if obj != None:
            print("use match and group : ", obj.group(0), obj.group(1), obj.group(2))
    infile.close()



# use findall() to find all occurrences of a pattern in a string
# and display the occurrences
def findall_phone_numbers(filename, reg_ex):
    infile = open(filename, "r")
    for line in infile:
        objs = reg_ex.findall(line)
        for obj in objs:
            print("use findall : ", obj)
    infile.close()



# use finditer() to find all occurrences of a pattern in a string
# and display the occurrences
def finditer_phone_numbers(filename, reg_ex):
    infile = open(filename, "r")
    for line in infile:
        objs = reg_ex.finditer(line)
        for obj in objs:
            print("use finditer : ", obj, obj.group(), obj.start(), obj.end())
    infile.close()


# use finditer() to find all occurrences of a pattern in a string
# and display the occurrences, print each group
def finditer_phone_numbers_group(filename, reg_ex):
    infile = open(filename, "r")
    for line in infile:
        objs = reg_ex.finditer(line)
        for obj in objs:
            print("use finditer and group : ", obj.group(0), obj.group(1), obj.group(2))
    infile.close()



print("============= look for phone numbers")

# regex = re.compile(r"[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]")
# regex = re.compile(r"[0-9]?[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]")
# regex = re.compile(r"[0-9]?[0-9]{3}-[0-9]{4}")
regex = re.compile(r"[0-9]{3,4}-[0-9]{4}")

search_phone_numbers("simpsons_phone_book.txt", regex)
match_phone_numbers("simpsons_phone_book.txt", regex)
findall_phone_numbers("simpsons_phone_book.txt", regex)
finditer_phone_numbers("simpsons_phone_book.txt", regex)


print("============= look for names of people whose first names start with 'J' and last names start with 'Neu'")

regex = re.compile(r"J.*Neu")
# regex = re.compile(r"Neu")
search_phone_numbers("simpsons_phone_book.txt", regex)
match_phone_numbers("simpsons_phone_book.txt", regex)
findall_phone_numbers("simpsons_phone_book.txt", regex)
finditer_phone_numbers("simpsons_phone_book.txt", regex)


print("============= look for phone numbers using grouping")

# # this expression contains 2 groups, each group represents a sequence of digits
regex = re.compile(r"(\d{3,4})-(\d{4})")    # group -- use parentheses
search_phone_numbers("simpsons_phone_book.txt", regex)
match_phone_numbers("simpsons_phone_book.txt", regex)
findall_phone_numbers("simpsons_phone_book.txt", regex)
finditer_phone_numbers("simpsons_phone_book.txt", regex)


print("============= look for phone numbers using grouping, print each group")

# # this expression contains 2 groups, each group represents a sequence of digits
regex = re.compile(r"(\d{3,4})-(\d{4})")    # group -- use parentheses
search_phone_numbers_group("simpsons_phone_book.txt", regex)
match_phone_numbers_group("simpsons_phone_book.txt", regex)
findall_phone_numbers("simpsons_phone_book.txt", regex)   # notice the output
finditer_phone_numbers_group("simpsons_phone_book.txt", regex)