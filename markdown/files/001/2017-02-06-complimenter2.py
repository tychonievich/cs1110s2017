age = input('How old are you? ')
print('line 2: age =', age, 'which is a', type(age))

non_integer_age = float(age)
print('line 5: non_integer_age =', non_integer_age, 'which is a', type(non_integer_age))
print('line 6: age =', age, 'which is a', type(age))

integer_age = int(non_integer_age)

fake_age = integer_age - 5
print('You don\'t even look \"' +  str(fake_age) + '"!')


age = int(float(input('How old are you? ')))
