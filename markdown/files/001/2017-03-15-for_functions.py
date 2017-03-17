def harmonic_mean(values):
    '''n / (1/a + 1/b + 1/c + 1/d + ... )'''
    total = 0
    number = 0
    for value in values:
        total += 1/value
        number += 1
    return number / total


def mean(values):
    total = 0
    number = 0
    for value in values:
        total += value
        number += 1
    return total / number

def mean2(values):
    return sum(values) / len(values)

print(mean([2]))
print(mean([1,2,3]))
print(mean([1,2,3,4,-1,13,0]))