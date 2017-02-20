def absolute(x):
    b = x < 0
    if b:
        return -x
    else:
        return x

print(absolute(-3))

def working_age(age):
    if age >= 14 and age < 70:
        return True
    else:
        return False

def working_age2(age):
    if 14 <= age < 70:
        return True
    else:
        return False

def working_age3(age):
    return 14 <= age < 70

age = int(input('How old are you? '))
if working_age(age):
    print("why aren't you at work?")
else:
    print('enjoy loafing at home')


print(1 < 3 > 4 < 5 > 0)
