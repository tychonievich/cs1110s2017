def get_number():
    while True:
        n = input('Type a number: ')
        try:
            n = int(n)
            return n
        except:
            print('Type an actual number!')



n = get_number()
print(n ** 2)

