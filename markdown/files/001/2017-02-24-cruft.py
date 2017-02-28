def is_even(number):
    remainder = number % 2
    if remainder == 0:
        return True
    else:
        return False

def is_even(number):
    remainder = number % 2
    return remainder == 0



# if ...: return True  -> get rid of the if
# == True -> delete it

even = is_even(13)
if even:
    print('even:', even)
else:
    print('odd:', even)


e1 = is_even(13)
e2 = is_even(12)
if e1 == e2:
    print('math broke')

# change any     x == False    into    not x

# use else
x = 5

if x > 10:
    print(x, 'is big')
if x <= 10:
    print(x, 'is small')

if x > 10:
    print(x, 'is big')
else:
    print(x, 'is small')