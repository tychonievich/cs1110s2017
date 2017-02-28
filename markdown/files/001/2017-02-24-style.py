# Aesthetics:

print('hi') # good
print( 'hi' ) # what the textbook does
print ('hi') # bad

# an even number = 1110
an_even_number = 1110 # Python suggests
anEvenNumber = 1110 # Java, C++ suggest

# understandability

# rule 1: use descriptive variable names
user_age = input('How old are you? ')
# rule 1.a: don't change what a variable means
user_age = int(user_age)
user_age += 5 # bad: changed meaning of variable to not match name

# rule 2: user descriptive function names
def fraction(numerator, denominator):
    return numerator / denominator

# rule 2.a: if a function returns True/False, name it is_something or the like
def is_even(x):
    return x % 2 == 0
# see 8.2.10 in textbook

# rule 3: use a variable for each idea
import math
r = 10
#      density   * volume of a sphere
mass = 1000 * (4/3) * math.pi * r**3

density = 1000
volume_sphere = (4/3) * math.pi * r**3
mass = density * volume_sphere


density = 1000
c = (4/3) * math.pi
volume_sphere = c * r**3
mass = density * volume_sphere



# rule 4: use docstrings
def is_even(x):
    '''determines if the argument was an even integer

    is_even(13) -> False
    is_even(12.03) -> False
    is_even(12.0) -> True
    '''
    return x % 2 == 0


help(len)