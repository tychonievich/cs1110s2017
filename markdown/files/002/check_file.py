import os.path
# from os.path import *    # using the above system or this syntax


# infile = open('input.txt', 'r')
# line = infile.read().strip()   # read an entire content
# infile.close()
#
# Open a non-existing file with a read mode will result
# in a FileNotFoundError exception.
# To handle this situation, we need to check if the file exists
# prior to opening it.
# Python has a module (os.path) that deals with file system.
# To use methods of this module, import it

# check if the file exists, open and read it
if os.path.exists('input.txt'):
    datafile = open('input.txt', 'r')
    data = datafile.read().strip()    # read an entire file all at once
else:  # otherwise, create a file and write data to it
    with open('input.txt', 'w') as datafile:
        print('let\'s create a file', file=datafile)


## why do we want to read from a file if it exists
## and then create a file only if it doesnt exist?

## why should we check if the file exists?







