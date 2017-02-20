b1 = True
b2 = 2 < 3
answer = b1 and b2
print(answer)

if 'cheese':
    print('yum')
else:
    print('give me cheese')

# everything has a truthiness
# nothing if false

print(bool('cheese'), bool(42), bool(0), bool(None), bool(''))


def working_age2(age):
    if 14 <= age < 70:
        return 'True'
    else:
        return 'False'

age = int(input('How old are you? '))
if working_age2(age) == True:
    print('you should be a work!')
else:
    print('enjoy loafing at home')



