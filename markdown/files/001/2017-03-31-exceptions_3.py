def get_number_and_divide():
    have_answer = False
    while not have_answer:
        n = input('Type a number: ')
        d = input('Type another number: ')
        try:
            n = int(n)
            d = int(d)
            answer = n / d
            have_answer = True
        except ValueError:
            print("Those weren't both numbers!")
        except ZeroDivisionError:
            print("The second number can't be zero (sorry)")
    return answer



print(get_number_and_divide())

questions = '''
can we scatter except: after try:
why can you have try: anywhere (functions)

'''
