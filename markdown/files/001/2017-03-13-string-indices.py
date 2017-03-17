example = '''
Name: Luther
Occupation: teacher
Age: indeterminate
'''

text = input('Type something: ')

print('the last letter you typed was', text[-1])

the_index = text.find('the')

print('You typed "the" at index', the_index)


occupation_index = example.find('Occupation: ')
occupation_end_index = example.find('\n', occupation_index)
occupation = example[occupation_index:occupation_end_index]

print(occupation)