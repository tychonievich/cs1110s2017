age = input('How old are you? ')

# int(str)
# float(str)
# str(anything)

numeric_age = int(age)

fake_age = numeric_age - 5
print("You don't even look", fake_age, "!")

# the following is confusing
print("You don't even look", str(int(age) - 5) + "!")

# the following is so confusing you should never do it
print("You don't even look", str(int(input('How old are you? ')) - 5) + "!")
