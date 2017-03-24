# to read file:
# open(filename)
# for line in file:

import urllib.request

post_box = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/snark.txt')
count = 0
words = 0
characters = 0
for line in post_box:
    # count words, lines, and characters somehow
    line = line.decode('utf-8')
    count += 1
    words += len(line.split())
    characters += len(line)


print('lines, words, and characters:', count, words, characters)
