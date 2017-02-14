'''
Get A, B, and C of the polynomial A x**2 + B x  C    (from the user, using input)
Then get x   (also from the user)
and print the value of the polynomial
'''

print('Let us solve A x^2 + B x + C for you.')

# inputs for A, B, C
A = input('What is the value of A? ')
B = input('What is the value of B? ')
C = input('What is the value of C? ')

print('The polynomial is', A, 'x^2 +', B, 'x +', C)


x = input('What is the value of x? ')

A, B, C, x = float(A), float(B), float(C), float(x)

# debug
print(A, B, C, x)

answer = A * x**2 + B * x + C
print(answer)
