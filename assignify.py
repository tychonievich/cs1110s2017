import datetime
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

with open('cal-shared.yaml') as stream:
    data = load(stream, Loader=Loader)

day = datetime.timedelta(days=1)

now = data['Special Dates']['Courses begin']
end = data['Special Dates']['Courses end']
lab = data['1110-lab']

print('''---
title: Assignments
...

# 1110/1111 Programming Assignments

''')

for asgn in data['assignments']:
    due = asgn['due']
    links = asgn['links']
    if len(links) == 0:
        print(due,'\n:    TBA')
    else:
        for link in links:
            with open(link+'.md') as f:
                for line in f:
                    if line.startswith('title: '): break
            print(due,'\n:    ['+line[7:]+']('+link+'.md)')

print('''

# 1110 Labs

''')

for asgn in data['1110-lab']:
    print('-   '+asgn)
