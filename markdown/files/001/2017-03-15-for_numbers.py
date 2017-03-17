numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    number = number**2
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i]**2

print(numbers)


los = '''
write code that, given a list of strings,
creates a list of the lengths of the strings

e.g. ['hi', 'there'] should become [2, 5]
'''.split()

for i in range(len(los)):
    los[i] = len(los[i])
print(los)