
def full_name():
    name = str(input("Enter your full name : "))
    name_split = name.split(' ')

    for i in range(len(name_split)):
        if i == 0:
            print("First name: {:s}".format(name_split[0]))
        elif i == len(name_split) - 1:
            print("Last name: {:s}".format(name_split[len(name_split)-1]))
        else:
            middle_name = name_split[i]
            print("Middle name: {:s}".format(middle_name))


full_name()
