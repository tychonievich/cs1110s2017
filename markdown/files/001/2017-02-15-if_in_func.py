def absolute_value(x):
    if type(x) == str:
        return x
    if x < 0:
        return -x
    print('still in absolute_value')
    return x

print(absolute_value(-11))
print(absolute_value(12))
print(absolute_value(34.5))
print(absolute_value(-3.45))
print(absolute_value('walnut'))