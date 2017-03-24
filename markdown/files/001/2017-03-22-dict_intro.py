d = {"three":3}
d[3.14] = "pi"
print(d)
d[3] = "three"
print(d)
d['3'] = 'Three'
print(d)


phone_book = {'Tychonievich': 33789, 'Help!': 911}
# print('We have numbers for:', list(phone_book.keys()))
# name = input('Who do you want to call? ')
#
# if name in phone_book:
#     print(phone_book[name])
# else:
#     print("We don't have that number")
#
# number = int(input('Type a phone number: '))
# if number in phone_book.values():
#     print('We know that number')
# else:
#     print('We don\'t know that number')
#

for something in phone_book:
    print('We found', phone_book[something])

for something in phone_book.items():
    key, value = something
    print('We found', key, ':', value, 'which we got from', something)


for key, value in phone_book.items():
    print('We found', key, ':', value)
