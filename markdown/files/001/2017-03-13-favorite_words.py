words = []

word = input('What is one of your favorite words? ')
while word != '':
    words.append(word)
    word = input('What is another one of your favorite words? ')

words = words.sort()
print('Your favorite words were:', words)
