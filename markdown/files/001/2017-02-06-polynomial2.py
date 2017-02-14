'''
Get A, B, and C of the polynomial A x**2 + B x  C    (from the user, using input)
Then get x   (also from the user)
and print the value of the polynomial
'''

print('Let us solve A x^2 + B x + C for you.')

# inputs for A, B, C
# get input for A
A = input('What is the value of A? ')
A = float(A)

# get input for B
B = input('What is the value of B? ')
B = float(B)

# get input for C
C = input('What is the value of C? ')
C = float(C)

print('The polynomial is', A, 'x^2 +', B, 'x +', C)

def get_number(name):
    ...

x = get_number('x')

x = input('What is the value of x? ')
x = float(x)

# debug
print(A, B, C, x)

answer = A * x**2 + B * x + C
print(answer)
