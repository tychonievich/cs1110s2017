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

<div style="display:table; font-size:200%; margin: 1em auto; padding:1ex; box-shadow: 0 1px 10px rgba(0,0,0,.1); border: thin solid #eee; border-radius:1ex; background-image: linear-gradient(to bottom, #ffffff, #f2f2f2);">[Submit assignments here](https://archimedes.cs.virginia.edu/cs1110/)</div>

<style type="text/css">
dl dd {
  display: inline;
  margin: 0;
}
dl dd:after{
  display: block;
  content: '';
}
dl dt{
  display: inline-block;
  min-width: 100px;
}
</style>

''')

for asgn in data['assignments']:
    due = asgn['due']
    links = asgn['links']
    if len(links) == 0:
        print(due,'\n:    TBA')
        break
    else:
        #print(due,'\n:    ')
        for link in links:
            try:
                if ' (' in link:
                    link, extra = link.split(' (',1)
                    extra = ' ('+extra
                else: extra = ''
                with open(link+'.md') as f:
                    for line in f:
                        if line.startswith('title: '): break
                print(due,'\n:    ['+line[7:].strip()+']('+link.strip()+'.html)', extra)
                #print('    1.  ['+line[7:].strip()+']('+link.strip()+'.html)')
            except:
                print(due,'\n:    assignment not yet released')
                #print('    1.  assignment not yet released')
print('''

# 1110 Labs

''')

for asgn in data['1110-lab']:
    print('-   '+asgn)
