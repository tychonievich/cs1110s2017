def has_an_x(s):
    # look at each character
    # if it was an x, return True
    # if none were x, return False
    index = 0
    while index < len(s): # stop if index >= len(s)
        if s[index] == 'x':
            new_s = s[0:index] + '_☺_' + s[index+1:len(s)]
            print(new_s)
            return True
        index += 1
    return False

print(has_an_x('elephant'))
print(has_an_x('excited'))
print('x' in 'elephant')
print('x' in 'excited')