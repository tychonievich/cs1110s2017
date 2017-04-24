# create a file containing friends' favorite cartoon characters


def write_file():
    outfile = open('cartoon.txt', 'w')
    for i in range(3):
        user_input = input("What is your favorite cartoon character? ")
        outfile.write(user_input + '\n')    # must write string with write()
    outfile.close()


def with_open():
    # to show that the file is opened and closed without an explicit .close()
    for i in range(3):
        user_input = input("What is your favorite cartoon character? ")
        # for each iteration, after entering the user_input, observe what is in the file
        with open('cartoon2.txt', 'w') as myoutfile:
            myoutfile.write(user_input + '\n')  # must write string with write()


    # the following code will produce the same output file as write_file() function
    # with open('cartoon2.txt', 'w') as myoutfile:
    #     for i in range(3):
    #         user_input = input("What is your favorite cartoon character? ")
    #         myoutfile.write(user_input + '\n')    # must write string with write()


# write_file()
with_open()




