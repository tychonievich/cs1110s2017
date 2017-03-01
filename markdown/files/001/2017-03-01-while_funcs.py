def yes_or_no():
    '''use input() to get either Yes or No'''
    user_typed = input('Type yes or no: ')
    # if they did not type yes or no,
    #   ask again
    #   check again

    while user_typed != 'yes' and user_typed != 'no':
#    while not (user_typed == 'yes' or user_typed == 'no'):
        print('that was not yes or no')
        user_typed = input('Type yes or no: ')

    return user_typed


print(yes_or_no(), 'should have been either yes or no')


# log_a(b) means the number of times a can be multiplied by itself to get b
def log(a, b):
    power_raised = a
    answer = 0
    while True:
        if power_raised > b:
            return answer
        power_raised *= a
        answer += 1

def log(a, b):
    power_raised = a
    answer = 0
    while power_raised <= b:
        power_raised *= a
        answer += 1
    return answer

print(log(10, 10))
print(log(10, 100))
print(log(10, 1000))
print(log(10, 10000))
print(log(10, 100000000000000000000000000000))


# want to print a lot of values on one line
number = int(input('How many do you want? '))
line = ''
num = 1
# repeatedly
#    add square of num to the line
#    increase num by 1
while num <= number:
    line = line + str(num**2) + " "
    num += 1
print(line)
