from sys import argv
# # read the WYSS section for how to run this
# script, first, second, third = argv
#
# print("This script is called:", script)
# print("your first variable is:", first)
# print("your second variable is:", second)
# print("your third variable is:", third)


first_name = input("Enter the first name")
last_name = input("Enter the last name")
script_name = argv[0]
age = argv[1]


print(f"your first name is {first_name}\nYour last name is ", last_name, "and the name of this script is" , script_name, "and your age is", age)
