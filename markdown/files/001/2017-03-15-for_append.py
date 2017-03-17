los = '''
write code that, given a list of strings,
creates a list of the lengths of the strings

e.g. ['hi', 'there'] should become [2, 5]
'''.split()

lol = []

for word in los:
    lol.append(len(word))
    print(lol)
print(los)
print(lol)