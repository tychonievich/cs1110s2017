# to read file:
# open(filename)
# read()

post_box = open('file_intro_1.py')
print(post_box)
contents = post_box.read()
print(contents)
print('characters:', len(contents))
lines = contents.split('\n')
print('lines:', len(lines))
words = contents.split()
print('words:', len(words))
