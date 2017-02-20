if 'cheese':
    print('yum')
else:
    print('I want cheese')

# All things have truthiness
# nothing is false

print(bool(1), bool(-12), bool(0), bool('hi'), bool(''))


def working_age2(age):
    if 14 <= age < 70:
        return 'True'
    else:
        return 'False'

age = int(input('How old are you? '))
if working_age2(age):
    print("why aren't you at work?")
else:
    print('enjoy loafing at home')
