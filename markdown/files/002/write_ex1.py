# 1. open file
# 2. write something to file --> data are put in buffer
# 3. close the file --> force data to be written to the file


### BE CAREFULE, don't open your program file with a write mode ###
### The content in your program file will be empty ###

# There are several ways to open, write, and close

####################################
### Open and close explicitly and
### write file with write()
####################################
# be careful with the file's name
# open with "w" mode will empty the file's content
outfile = open('data1.txt', 'w')
outfile.write('take one argument of type string')
# outfile.close()

# Without explicitly close the file, it's up to
# the operating system how it will behave at the moment
# i.e., sometimes our code will work but sometimes it won't.
# This is unpredictable.
# Therefore, we should always close the file.


####################################
### Open and close explicitly and
### write file with print()
####################################
# A flexible way to write to file is use "print" instead of "write"
# print() allows us to print multiple things, multiple types to the file
# -- unlike write() that accepts only one thing and it must be string.
#
outfile = open('data2.txt', 'w')

# optional argument file=name_of_file_object -- telling which file to print to
print('any set of values, any type', outfile, file=outfile)
# can print many times
print('string', 197, 9*8, True, '###', file=outfile)
outfile.close()


# sometimes, there might be a problem while writing to file

outfile = open('data3.txt', 'w')
for i in range(4):
    number = int(input('Enter an integer: '))
    print(number, file=outfile)
outfile.close()


# Suppose when we run this code,
# the user enters an empty space, a letter, or nothing.
# We'll get a runtime error.
# When a runtime error occurs, there is no guarantee
# whether the things we try to write to the file will actually be written.
# This is entirely depending on the operating system.
# Thus, instead of letting the operating system decides what to do,
# we want to take control and make sure data are written to the file.
# To force this writing to the file, we have to make sure
# that the file is always closed.

# One way to handle any potential errors that might occur at runtime
# and make sure the file is close is to use a try/except block

####################################
### Open and close explicitly and
### write file with print()
### Use a try/except block to handle errors
####################################
outfile = open('data3.txt', 'w')
try:
    for i in range(4):
        number = int(input('Enter an integer: '))
        print(number, file=outfile)
    outfile.close()   # close the file after everything's done
except:   # notice we didn't specify the kinds of errors, i.e., handle *any* kinds the same way
    outfile.close()   # if something goes wrong, close the file
    # The "except" clause stops the error and not show error message,
    # and then forces the file to close.


# However, if we want information about the error,
# we wouldn't want to stop the error.
# In fact, we want to let the error occurs and shows
# the error message, and also force closing the file.
# To have this behavior, we'd use a finally keyword.
# Let's modify the above code


####################################
### Open and close explicitly and
### write file with print()
### Use a try/finally block to handle errors
####################################
outfile = open('data3.txt', 'w')
try:
    for i in range(4):
        number = int(input('Enter an integer: '))
        print(number, file=outfile)
    outfile.close()   # close the file after everything's done
finally:   # if anything goes wrong, handle it
    outfile.close()

# The "finally" clause doesn't stop the error from happening.
# The error message will show. Then the code block of the finally
# clause will be executed (in this example, close the file)


# Make use of a Python's "with" statement
# and thus we don't have to explicitly/manually close the file;
# (the best way to work with file)
# also behave the same way as try/finally example above
####################################
### Use the with statement to open and close file
### write file with print()
####################################
with open('output.txt', 'w') as outfile:
    for i in range(4):
        number = int(input('Enter an integer '))
        print(number, file=outfile)
# guarantee to close the file as the code exit the with block