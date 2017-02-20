def ordinal(n):
    '''1 -> 1st, 2 -> 2nd, 3 -> 3rd, 4 -> 4th, 5 -> 5th, ..., 12 -> 12th, 321 -> 321st, ...'''
    # int -> str
    # str + suffix
    # determine the suffix (usually th, unless it isn't)
    suffix = 'th'
    if (n % 10) == 2:
        suffix = 'nd'
    s = str(n)
    answer = s + suffix
    return answer

print(ordinal(1))
print(ordinal(2))
print(ordinal(12))
print(ordinal(22))
print(ordinal(202))
print(ordinal(10))
print(ordinal(13))