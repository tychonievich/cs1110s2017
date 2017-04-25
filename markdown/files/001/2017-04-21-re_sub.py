import re

text = '''
Note: assignments and their due dates are listed on the assignments page, not on this page.
Monday 	Wednesday 	Thursday 	Friday
Per the registrar, all sections of 1110 and 1111 will have their final exam at 7–10 pm on Thursday, 11 May 2017. Conflicts with that time will be resolved the following day (Friday 12 May) at 10 am. No permission to take the exam earlier than 11 May or from off of UVa grounds will be granted.

You may report conflicts and request accomodations at https://goo.gl/forms/hC5oRY2zJoVfQz023.
Copyright © 2017 Luther Tychonievich, Upsorn Praphamontripong, and Craig Dill.
Last updated 2017-04-19 15:16
'''

two_words = re.compile(r'([a-z]+) ([a-z]+)')

new_text = two_words.sub(r'\1 (not \1) \2', text)

print(new_text)



# change Tychonievich, Luther  →  Luther Tychonievich

text = '''
Tychonievich, Luther and Upsorn Praphamontripong and Dill, Craig
'''

backwards_names = re.compile(r'([A-Z][a-z]+), ([A-Z][a-z]+)')
new_text = backwards_names.sub(r'\2 \1', text)
print(new_text)




# change submission/louslist/lab102/mst3k/louslist.py → mst3k-102/louslist.py

submission = re.compile(r'submission/.*/lab([0-9]+)/([a-z0-9]+)/(.+\.py)')
text = '''
submission/louslist/lab102/mst3k/louslist.py
submission/calculate/lab105/lat7h/calculate.py
'''
new_text = submission.sub(r'\2-\1/\3', text)
print(new_text)



# add a newline after each comma inside a square-bracketed list


# add english spacing: change ". " to ".  "
# except after Mr./Mrs./Dr., and not creating ".   "

bad_space = re.compile(r'\. ([^ ])')
text = '''
This text is inconsistent. It sometimes uses one space.  It sometimes uses two.
--------------------------1----------------------------123---------------------
'''
new_text = bad_space.sub(r'.  \1', text)
print(new_text)