x = int(input('type a number: '))

while x < 0: # infinite loop
    print(x, 'is negative')
    x = x - 1

print('done!')

questions = '''

define "guard"
    expression
    after while, before :
    boolean value (True or False)
    if True, do the loop body again
    if False, move on with the progrma

'''

