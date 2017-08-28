from sys import argv


def add():
    c = argv[1] + argv[2]
    return c

def subtract():
    c = argv[1] - argv[2]
    return c

def multiply():
    c = argv[1] * argv[2]
    return c

def divide():
    c = argv[1]/argv[2]
    return c



func_list = {
            'Addition': add(),
            'Subtraction': subtract(),
            'Multiplication': multiply(),
            'Division': divide(),
            }



def operation():

    choice = input("""which of the following operations do you want
                  to perform?
                  1) Addition
                  2) Subtraction
                  3) Multiplication
                  4) Division\n\n>""")

    if choice == '1':
        return 'Addition'
    elif choice == '2':
        return 'Subtraction'
    elif choice == '3':
        return 'Multiplication'
    elif choice == '4':
        return 'Division'
    else:
        print("Invalid option")


def run():
    final = func_list.get(operation())
    print(final)




run()
