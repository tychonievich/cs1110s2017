s = 'this\'s a "string"'
d = "this's also a string"
tripple_single = '''we can put text
        and new lines


        and 'quotes' and "quotes"
'''

def absolute(x):
    '''Computes the absolute value of x
    example: absolute(-3) should be 3
    '''
    b = x < 0
    if b:
        return -x
    else:
        return x

print(absolute(-3))

def working_age(age):
    if age >= 14 and age < 70:
        return True
    else:
        return False

def working_age2(age):
    if 14 <= age < 70:
        return True
    else:
        return False

def working_age3(age):
    return 14 <= age < 70


b1 = True
b2 = 2 < 3
answer = b1 and b2
print(answer)

w1 = working_age(20)
w2 = working_age(103)
print(w1, w2)

# print(1 < 2 > 3 < 5 > 2) # do not do this
