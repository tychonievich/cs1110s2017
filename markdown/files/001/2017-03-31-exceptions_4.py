def get_number():
    while True:
        n = input('Type a number: ')
        try:
            n = int(n)
            return n
        except:
            print('Type an actual number!')


def get_number_and_divide():
    have_answer = False
    while not have_answer:
        n = get_number()
        d = get_number()
        try:
            answer = n / d
            have_answer = True
        except ZeroDivisionError:
            print("The second number can't be zero (sorry)")
    return answer

try:
    d = get_number_and_divide()
    print('inverse =', 1 / d)
except:
    print('We failed...')
