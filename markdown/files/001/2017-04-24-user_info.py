import os.path

def get_name():
    # check the file first,
    if os.path.exists('about_the_user.txt'):
        f = open('about_the_user.txt')
        name = f.read().strip()
    else:
        # if not there, ask the user and save the file
        name = input('What is your name? ')
        with open('about_the_user.txt', 'w') as s:
            print(name, file=s)
    return name

name = get_name()
color = input('What is a color you like? ')
print('Hi,', name+", I'm thinking", color, "thoughts about you")

