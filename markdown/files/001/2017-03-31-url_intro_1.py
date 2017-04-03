# to read url:
# open(filename)
# read()
# decode('utf-8')

import urllib.request


post_box = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/snark.txt')
print(post_box)
contents = post_box.read()
print(contents)
text = contents.decode('utf-8')
print(text)

print('characters:', len(text))
lines = text.split('\n')
print('lines:', len(lines))
words = text.split()
print('words:', len(words))
