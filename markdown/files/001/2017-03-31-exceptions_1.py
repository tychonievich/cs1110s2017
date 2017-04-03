def get_number():
    n = input('Type a number: ')
    n = int(n)
    return n

try:
    n = get_number()
    print(n ** 2)
except:
    print('Aaa!')

