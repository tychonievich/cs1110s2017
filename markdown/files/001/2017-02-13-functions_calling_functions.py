line_count = 0
def line(m, x, b):
    '''Uses the y = m x + b line formula'''
    global line_count
    y = m * x + b
    line_count += 1
    return y

def x_intercept(m, b):
    '''Solve 0 = m x + b for x'''
    x = -b / m
    return x

def intersect(m1, b1, m2, b2):
    '''Find the intersection of two lines'''
    x = x_intercept(m1-m2, b1-b2)
    y = line(m1, x, b1)
    return x, y



# # code that uses the functions:

# print(line(2, 3, 4), 'should be', 10)
# print(x_intercept(2, 4), 'should be', -2)
#
# m = 3.5
# b = 11.256
# x = x_intercept(b, m)
# y = line(m, x, b)
# print(y, 'should be', 0)

# print(m, 'should be', 2)
# print(y, 'should be', 10)


line1m, line1b = 2, 3
line2m, line2b = -5, 13

print(intersect(line1m, line1b, line2m, line2b))
print(intersect(1, 0,  -1, 3))