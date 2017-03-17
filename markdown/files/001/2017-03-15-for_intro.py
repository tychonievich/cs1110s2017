sentence = 'This is a longer piece of text'
words = sentence.split()

'''

word = words[0]
do_stuff(word)
word = words[1]
do_stuff(word)
...

'''
for word in words:
    print(word)

print(words)



count_dracula = 0
for poodle in count_dracula:
    print('poodle =', poodle)
    count_dracula += 1
print(count_dracula)
# error
# 0
# 1
# 2
# 7
# 8