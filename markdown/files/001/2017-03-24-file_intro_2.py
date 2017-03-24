# to read file:
# open(filename)
# for line in file:

post_box = open('file_intro_2.py')
print(post_box)
count = 0
words = 0
characters = 0
for line in post_box:
    # count words, lines, and characters somehow
    count += 1
    words += len(line.split())
    characters += len(line)


print('lines, words, and characters:', count, words, characters)
