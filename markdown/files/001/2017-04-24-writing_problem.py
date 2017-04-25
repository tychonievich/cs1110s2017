f = open('ticker.txt', 'w')

try:
    running_total = 0
    for i in range(10):
        num = int(input('Type an integer: '))
        print(running_total, '+', num, file=f)
        running_total += num
    print('=', running_total, file=f)
    f.close()
finally:
    f.close()
