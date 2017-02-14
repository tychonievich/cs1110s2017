def f(x, b):
    global a
    print(x, a-b)
    a = 3

def g(a, b):
    f(b, a)
    print(a, b)

a = 1
b = 2
g(2, a)
print(a, b)
