# import the regular expression (re) module to handle regular expression
import re

# findall() returns the occurrences of the pattern in the target string
#    - create a list of occurrences of a pattern in a string
# search() gives more information than just the actual patterns
#    - tell where the pattern occurs in the target string
#    - returns a match object for the first occurrence
#    - returns None if pattern is not found
# match() checks if the pattern exists at the very start of a string
#    - returns Non if pattern not found --> Python process it as False
# finditer() creates a list (or an iterator) of match objects for where
#      the pattern occurs in a string --> thus, can use for obj in ...

def find_all_phone_numbers_of(filename, reg_ex):
    results = ""      # can we return a list of results?
    infile = open(filename, "r")

    for line in infile:
        # if reg_ex.search(line):   # search() return the first match object
        #     results = results + line.rstrip() + '\n'

        obj = reg_ex.search(line)
        if obj != None:  # why do we need to take care of None value
            # print(reg_ex.search(line))
            print(obj, obj.group(), obj.start(), obj.end())

        # obj = reg_ex.match(line)
        # if obj != None:
        #     # print(reg_ex.match(line))
        #     print(obj, obj.group(), obj.start(), obj.end())
    infile.close()
    return results




def find_all_phone_numbers(filename, reg_ex):
    results = ""      # can we return a list of results?
    infile = open(filename, "r")

    for line in infile:
        # temp_result = reg_ex.findall(line)
        # if len(temp_result) > 0:
        #     for info in temp_result:
        #         results += info + '\n'

        obj_list = reg_ex.finditer(line)
        for obj in obj_list:
            print(obj, obj.group(), obj.start(), obj.end())
    infile.close()
    return results




# Find all possible phone numbers of people from Simsons TV series
# whose first names start with "J" and last names start with "Neu"
regex = re.compile(r"J.*Neu")   # create a regular expression object that match the pattern
simpsons_phones = find_all_phone_numbers_of("simpsons_phone_book.txt", regex)
print(simpsons_phones)


# Find all possible phone number from Simsons TV series
# assuming no area code included
regex = re.compile(r"[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]")
simpsons_all_phones = find_all_phone_numbers("simpsons_phone_book.txt", regex)
print(simpsons_all_phones)

# http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/simpsons_phone_book.txt
