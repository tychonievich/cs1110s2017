# 1. open file (for writing)
# 2. write stuff
# 3. close the file -- makes sure all data we wrote is on disk

# 1
f = open('text.txt', 'w')
# 2
f.write('Did also this work too?')
# 3
f.close()

# use print not write
# 1
f = open('text.txt', 'w')
# 2
print('the value of f is', f, file=f)
print('2 * 3 =', 2*3, file=f)
# 3
f.close()


# use the with statement
# 1 use with
with open('text.txt', 'w') as f:
    # 2 print stuff
    print('the value of f is', f, file=f)
    print('2 * 3 =', 2*3, file=f)
# 3 by exiting the with indent, the file is closed
