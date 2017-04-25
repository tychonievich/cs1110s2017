import re

text = '''
In particular,

    There should be one kind if user input, a vertical flap action triggered by either a mouse click or the space bar (your choice) – you do not need to use an animated sprite sheet for this assignment
    There should be randomly generated scrolling obstacles (pillars) with openings at random heights
    Touching the ground or a pillar should end the game
    Score should be based on how long the player lasts before the game ends
    When the game ends, the score should be displayed visually in the game screen

We won’t be able to perform automated testing for this submission (we’ll have course staff run it to grade it), but you should be able to tell if it is working on your own by playing the game you’ve created.
'''

the_word_the = re.compile('[T-Za-t]h[aeiou]')
match = the_word_the.search(text)
# print(match.group(), match.start())

for match in the_word_the.finditer(text):
    print(match.group(), match.start())


list_start = re.compile(r'\[[\-0-9]')

