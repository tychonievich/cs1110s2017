import this

x = 3
y = 5
print(x,y)

# swap them
x += y
y = x - y
x -= y

print(x, y)

tmp = x
x = y
y = tmp

print(x, y)

x, y = y, x

print(x, y)