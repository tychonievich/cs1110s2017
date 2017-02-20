# x = 5
# y = 10
# b = x < y
#
# print(b, type(b))
#
# print(x < y)
# print(x > y)
# print(x <= y) # ≤
# print(x >= y) # ≥
# print(x == y) # =
# print(x != y) # ≠
#
#
# name = input('Type your name: ')
#
# if name == 'Luther':
#     print('you are a swell guy!')
# else:
#     print('nice to meet you')
#
#
#
# print('"3" == 3', "3" == 3)
# print('3.0 == 3', 3.0 == 3)


number = int(input('Type an integer: '))

if number < 10:
    print(number, 'is a small number')
elif number < 100:
    print(number, 'is a medium-sized number')
else:
    print(number, 'is big')
