print(list(range(10)))
print(list(range(3,10)))
print(list(range(3,10,2)))

# repeat 10 times
for i in range(10):
    print('Yay!')

# look at the letters of one word
text = 'Hi there, I am happy to meet you.'
start = text.find('happy')
end = text.find(' ', start)
print(text[start:end])
for i in range(start, end):
    print(text[i])


print(list(range(100, -10, -7)))