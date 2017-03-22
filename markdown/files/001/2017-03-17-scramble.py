import random

text = '''Given some words, scramble the non-start non-end letters of each word'''
text = '''On thing you’ll need to do repeatedly is make a smaller list out of a bigger list. For example, once they pick Chinese you’ll need to figure out what the set of Chinese restaurants is so you can pick one of them randomly.'''

def shuffle_word(word):
    example = list(word)
    random.shuffle(example)

    new_word = ''
    for letter in example:
        new_word += letter

    return new_word

words = text.split()
print(words)

line = ''
for word in words:
    if len(word) == 1:
        line += word + ' '
    else:
        middle = word[1:-1]
        shuffled = shuffle_word(middle)
        line += word[0]+ shuffled + word[-1] + ' '

print(line)

# print(shuffle_word(text))
# print(words)