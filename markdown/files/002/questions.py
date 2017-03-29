question = '''
benefits of downloading vs using url
    in memory = can be used by your program
    file - on your computer, but not (until read) in memory
    urllib.request - on someone else's computer


reading a file - what it does, when to do it
    thing = open('somefile.txt')
    text = thing.read() (or readline, readlines, for ... see below)

read a url
    thing = urllib.request.urlopen('somefile.txt')
    data = thing.read()  (or readline, readlines, for ... see below)
    text = data.decode('utf-8')
what is UTF-8

where to decode
    where you first have a string, and only from a URL not a file

what do you strip
    usually white-space (.strip()) but you can strip other stuff (e.g. .strip('ude\n'))


CSV - delimiter-separated, tabular data
    each line is a row
    each row is a list of cells
    cells are separated within a line using a delimiter (often ',', but '|' for louslist.py)
'''

import urllib.request

farm = urllib.request.urlopen('http://www.cs.virginia.edu/~up3f/cs1110/examples/file/studentinfo.txt')
# alltext = thing.read()
# print(type(alltext), len(alltext))
# first_line = thing.readline()
# print(type(first_line), len(first_line), first_line)
# second_line = thing.readline()
# print(type(second_line), len(second_line), second_line)
# alllines = thing.readlines()
# print(type(alllines), len(alllines), alllines)

for potatoe in farm:
    potatoe = potatoe.decode('utf-8').strip()
    print(len(potatoe), potatoe)
