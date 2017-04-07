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

# Programming Assignments

To streamline the twice-a-week 1111 and thrice-a-week 1110 schedules,
programming assignments are due in batches once a week.
When several are due the same day, we strongly encourage working on and submitting one each day or two,
in the order listed here.

[Submit assignments here](https://archimedes.cs.virginia.edu/cs1110/)

''')

for asgn in data['assignments']:
    due = asgn['due']
    links = asgn['links']
    if len(links) == 0:
        print(due,'\n:    TBA')
        break
    else:
        print(due,'\n:    ')
        for link in links:
            try:
                with open(link+'.md') as f:
                    for line in f:
                        if line.startswith('title: '): break
                print('    1.  ['+line[7:].strip()+']('+link.strip()+'.html)')
            except:
                print('    1.  assignment not yet released')
print('''

# 1110 Labs

''')

for asgn in data['1110-lab']:
    print('-   '+asgn)
