import re

# Python "" string, including "I use the word \"hi\" in many examples"
text = r'''
"xyz"
"x\"y\"z"
'''

#                          __  __
string = re.compile(r'"([^"\\]|\\.)*"')
for match in string.finditer(text):
    print("match:", match.group())


# addition problem: one or more numbers, separated by + or - (and maybe spaces)

text = r'''
3
3 + 4
303+4 -5 + 6
'''

addition = re.compile(r'[0-9]+(( ?[\-\+] ?[0-9]+)*)')
# addition = re.compile(r'[0-9\+\- ]+')
for match in addition.finditer(text):
    print('addition:', match.group(), match.groups(), match.group(1))



# ... and also perform the addition
# instructors on an actual Lou's List page
